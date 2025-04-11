import numpy as np
import matplotlib.pyplot as plt

expected = np.exp(1.5)

steps = []
results = []

for i in range(1, 15):
    h = 1/(10**i)
    steps.append(h)
    approx = (-np.exp(1.5 + 2*h) 
              + 8*np.exp(1.5 + h) 
              - 8*np.exp(1.5 - h) 
              + np.exp(1.5 - 2*h)) / (12*h)
    results.append(approx)
    print(f"Step: {h}, approx: {approx}")

plt.figure()
plt.loglog(steps, results, marker="o", label="Estimat per steglengde")
plt.hlines(expected, steps[0], steps[-1], linestyle="dotted", color="black", label=f"Analytisk: {expected}")
plt.xlabel("Steglengde (h)")
plt.ylabel("Estimat")
plt.ylim(min(results) - 0.001, max(results) + 0.001)
plt.legend()
plt.savefig("oppg3_1", dpi=200)
plt.show()

errors = abs(np.array(results) - expected)

plt.figure()
plt.loglog(steps, np.abs(errors), marker="o", label="avvik per steglengde")
plt.xlabel("Steglengde (h)")
plt.ylabel("Error = |approx - exact|")
plt.legend()
plt.savefig("oppg3_2", dpi=200)
plt.show()
