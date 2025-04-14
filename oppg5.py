import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy.linalg import solve


# parametre for metoden (Set rimelige verdier for rimelige resultater)
d = np.pi
N = 30                      # punkter i rom
h = d / N                   # punkter i tid
k = 0.001                   # steglengde i tid
num_frames = 200            # antall steg i tid
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
line, = ax.plot(x, u, label="Temperatur u(x, t)")
ax.set_xlim(0, d)
ax.set_ylim(-1, 1)
ax.set_xlabel("x")
ax.set_ylabel("Temperatur u(x, t)")
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

interval = 50
fps = 1000/interval

anim = FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=True)
anim.save("oppg5.gif", writer="pillow", fps=fps)
plt.show()