import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy.linalg import solve


# parametre for metoden (Set rimelige verdier for rimelige resultater)
d = 3
N = 1000                     # Number of intervals => N+1 grid points in [0,1]
h = d / N                   # Spatial step size
k = 0.00001                   # Time step
num_steps = 500             # Number of frames in the animation
x = np.linspace(0, d, N+1)

u = np.sin(x)

# Build the matrix (I + λA), where λ = k/h^2
lam = k / (h**2)
M = N - 1                   # number of interior points
A = np.zeros((M, M))
for i in range(M):
    A[i, i] = 1 + 2*lam
    if i > 0:
        A[i, i-1] = -lam
    if i < M - 1:
        A[i, i+1] = -lam

# --- Set up the figure for animation ---
fig, ax = plt.subplots()
line, = ax.plot(x, u, label="u(x,t)")
ax.set_xlim(0, d)
ax.set_ylim(-1, 1)
ax.set_xlabel("x")
ax.set_ylabel("u(x,t)")
ax.set_title("Heat Equation (Implicit Euler)")
ax.legend()

def update(frame):
    global u

    # Solve for interior points 1..N-1
    u_interior = u[1:N]  # old values
    u_new_interior = solve(A, u_interior)
    
    # Apply boundary conditions
    u[0] = 0.0
    u[N] = 0.0
    
    # Update interior points
    u[1:N] = u_new_interior

    # Update the plot data
    line.set_ydata(u)
    return (line,)

# Create the animation
anim = FuncAnimation(fig, update, frames=num_steps, interval=100, blit=True)

plt.show()