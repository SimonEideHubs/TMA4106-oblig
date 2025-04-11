import numpy as np
import matplotlib.pyplot as plt

expected = np.exp(1.5)  # exact derivative at x=1.5 is also e^(1.5)

steps = []
results = []

# Loop over powers of 10 for the step size
for i in range(1, 17):
    h = 1/(10**i)
    steps.append(h)
    approx = (-np.exp(1.5 + 2*h) 
              + 8*np.exp(1.5 + h) 
              - 8*np.exp(1.5 - h) 
              + np.exp(1.5 - 2*h)) / (12*h)
    results.append(approx)
    print(f"Step: {h}, approx: {approx}")

plt.figure()
plt.loglog(steps, results, marker="o", label="Five-point derivative estimate")
plt.hlines(expected, steps[0], steps[-1], linestyle="dotted", color="black", label=f"Expected: {expected}")
plt.xlabel("Step size (h)")
plt.ylabel("Approximate derivative")
plt.title("Five-point derivative of e^x at x=1.5")
plt.ylim(min(results) - 0.1, max(results) + 0.1)
plt.legend()
plt.savefig("oppg3_values.png", dpi=200)
plt.show()

errors = np.array(results) - expected

plt.figure()
plt.loglog(steps, np.abs(errors), marker="o", label="Absolute error")
plt.xlabel("Step size (h)")
plt.ylabel("Error = |approx - exact|")
plt.title("Error for five-point derivative of e^x at x=1.5")
plt.legend()
plt.savefig("oppg3_error.png", dpi=200)
plt.show()
