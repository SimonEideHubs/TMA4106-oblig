import numpy as np
import matplotlib.pyplot as plt

steps = []
results = []

for i in range(1, 16):
    step = 1/(10**i)
    steps.append(step)
    result = (np.exp(1.5 + step) - np.exp(1.5)) / step
    results.append(result)
    print(f'Step: {step}, result: {result}')


# Leser av print at steg: 1e-08 gir best resultat på: 4.481689064306238 sammenliknet med forventet resultat på ca 4.48168907034

plt.figure()
plt.plot(steps[:-1], results[:-1], marker="o", label="Estimat per steglengde")
plt.hlines(np.exp(1.5), steps[0], steps[-1], linestyle="dotted", color="black", label="Forventet: 4.48168907034")
plt.xlabel("steglengde")
plt.ylabel("Verdi")
plt.yscale('symlog')
plt.xscale('log')
plt.ylim(min(results[:-1])-0.1, max(results[:-1])+0.1)
plt.legend()
plt.savefig("oppg1_1", dpi=200)
plt.show()

results = [abs(a - np.exp(1.5)) for a in results]
print(min(results))

plt.figure()
plt.loglog(steps, results, marker="o", label="Avvik per steglengde")
# plt.hlines(0, steps[0], steps[-1], linestyle="dotted", color="black", label="0")
plt.xlabel("steglengde")
plt.ylabel("Avvik")
plt.ylim(min(results)-0.1, max(results)+0.1)
plt.legend()
plt.savefig("oppg1_2", dpi=200)
plt.show()