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

# Initial condition: u(x,0) = sin(x)
u = np.sin(x)  # array storing current solution

# We'll build two matrices: M1 = (I + lam/2 * A) and M2 = (I - lam/2 * A)
lam = k / (h*h)
M = N - 1  # number of interior points

# Build the standard 2nd-derivative matrix A in size (M x M):
#    A[i,i] = 2, A[i,i-1] = A[i,i+1] = -1, zeros elsewhere
A = np.zeros((M, M))
for i in range(M):
    A[i, i] = 2.0
    if i > 0:
        A[i, i-1] = -1.0
    if i < M - 1:
        A[i, i+1] = -1.0

# Now define M1 and M2:
#   M1 = I + (lam/2) * A
#   M2 = I - (lam/2) * A
I_ = np.eye(M)
M1 = I_ + 0.5 * lam * A
M2 = I_ - 0.5 * lam * A

# --- Set up for plotting/animation ---
fig, ax = plt.subplots()
line, = ax.plot(x, u, label="Crank–Nicolson solution")
ax.set_xlim(0, d)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel("x")
ax.set_ylabel("u(x,t)")
ax.set_title("Heat Equation (Crank–Nicolson)")
ax.legend()

def update(frame):
    global u
    
    # We'll solve M1 * u^{n+1}_interior = M2 * u^{n}_interior
    u_interior = u[1:N]  # old data (for i=1..N-1)
    
    # Right-hand side:
    rhs = M2 @ u_interior
    
    # Solve the linear system for the interior points at next time step
    u_new_interior = solve(M1, rhs)
    
    # Enforce boundary conditions
    u[0] = 0.0
    u[N] = 0.0
    
    # Update interior
    u[1:N] = u_new_interior
    
    # Update the line plot
    line.set_ydata(u)
    return (line,)

anim = FuncAnimation(fig, update, frames=num_frames, interval=80, blit=True)
plt.show()
