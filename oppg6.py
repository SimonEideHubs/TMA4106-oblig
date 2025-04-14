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

lam = k / (h*h)
M = N - 1 

# A[i,i] = 2, A[i,i-1] = A[i,i+1] = -1
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

fig, ax = plt.subplots()
line, = ax.plot(x, u, label="Crank–Nicolson solution", color='C2')
ax.set_xlim(0, d)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel("x")
ax.set_ylabel("Temperatur u(x, t)")
ax.set_title("Varmelikningen (Crank–Nicolson)")
ax.legend()

def update(frame):
    global u
    u_interior = u[1:N]
    
    rhs = M2 @ u_interior
    u_new_interior = solve(M1, rhs)
    
    u[0] = 0.0
    u[N] = 0.0
    
    u[1:N] = u_new_interior
    line.set_ydata(u)
    return (line,)

interval = 50
fps = 1000/interval

anim = FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=True)
anim.save("oppg6.gif", writer="pillow", fps=fps)
plt.show()