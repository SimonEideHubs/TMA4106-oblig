import numpy as np
import matplotlib.pyplot as plt

steps = []
results = []

for i in range(1, 17):
    step = 1/(10**i)
    steps.append(step)
    result = (np.exp(1.5 + step) - np.exp(1.5 - step)) / (2*step)
    results.append(result)
    print(f'Step: {step}, result: {result}')


# Leser av print at steg: 1e-08 gir best resultat på: 4.481689064306238 sammenliknet med forventet resultat på ca 4.48168907034

plt.figure()
plt.loglog(steps[:-1], results[:-1], marker="o", label="Estimat per steglengde")
plt.hlines(np.exp(1.5), steps[0], steps[-1], linestyle="dotted", color="black", label=f"Forventet: {np.exp(1.5)}")
plt.xlabel("steglengde")
plt.ylabel("Verdi")
plt.ylim(min(results[:-1])-0.1, max(results[:-1])+0.1)
plt.legend()
plt.savefig("oppg2_1", dpi=200)
plt.show()

results = [a - np.exp(1.5) for a in results]

plt.figure()
plt.loglog(steps[:-1], results[:-1], marker="o", label="Estimat per steglengde")
plt.hlines(np.exp(1.5), steps[0], steps[-1], linestyle="dotted", color="black", label=f"Forventet: {np.exp(1.5)}")
plt.xlabel("Steglengde")
plt.ylabel("Avvik")
plt.ylim(min(results[:-1])-0.1, max(results[:-1])+0.1)
plt.legend()
plt.savefig("oppg2_2", dpi=200)
plt.show()