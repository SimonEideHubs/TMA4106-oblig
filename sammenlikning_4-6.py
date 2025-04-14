import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy.linalg import solve


'''
    Parametre for alle metodene
'''

d = np.pi
N = 50                      # punkter i rom
h = d / N                   # punkter i tid
k = 0.001                   # steglengde i tid
num_frames = 200            # antall steg i tid
x = np.linspace(0, d, N+1)


'''
    Startstilstand for alle 
'''

u0 = np.sin(x)

# For hver metode:
u_expl = u0.copy()
u_impl = u0.copy()
u_cn   = u0.copy()

time = 0.0


'''
    Matriser til alle
'''

lam = k / (h**2)
M = N - 1  # Antall punkter for matrise

# Lage matrise A for imlpisitt metode og Crank-Nicolson
A = np.zeros((M, M))
for i in range(M):
    A[i, i] = 2.0
    if i > 0:
        A[i, i-1] = -1.0
    if i < M - 1:
        A[i, i+1] = -1.0

I_ = np.eye(M)
M_impl = I_ + lam * A # Implisitt matrise

# De to halvdelene av gjennomsnittene for Crank-Nicolson
M1 = I_ + 0.5 * lam * A
M2 = I_ - 0.5 * lam * A


'''
    Funksjoner for de tre forskjellige metodene til å bruke i animasjonen
'''

def step_explicit(u_old):
    u_new = u_old.copy()
    for i in range(1, N):
        u_new[i] = u_old[i] + lam * (u_old[i+1] - 2*u_old[i] + u_old[i-1])
    u_new[0] = 0.0
    u_new[N] = 0.0
    return u_new

def step_implicit(u_old):
    interior_old = u_old[1:N]  
    interior_new = solve(M_impl, interior_old)
    u_new = u_old.copy()
    u_new[0] = 0.0
    u_new[N] = 0.0
    u_new[1:N] = interior_new
    return u_new

def step_crank_nicolson(u_old):
    interior_old = u_old[1:N]
    rhs = M2 @ interior_old
    interior_new = solve(M1, rhs)
    u_new = u_old.copy()
    u_new[0] = 0.0
    u_new[N] = 0.0
    u_new[1:N] = interior_new
    return u_new

def exact_solution(x, t):
    return np.exp(-t) * np.sin(x)


'''
    Lage plot
'''

fig, ax = plt.subplots()

current_exact_solution = exact_solution(x, time)
line_expl,  = ax.plot(x, abs(u_expl - current_exact_solution),  label="Ekplisitt Euler")
line_impl,  = ax.plot(x, abs(u_impl - current_exact_solution),  label="Implisitt Euler")
line_cn,    = ax.plot(x, abs(u_cn - current_exact_solution),    label="Crank–Nicolson")
# line_exact, = ax.plot(x, current_exact_solution, label="Analytisk (numerisk)", linestyle="dashed", color='black')

ax.set_xlim(0, d)
ax.set_ylim(-0.0001, 0.0005)
ax.set_xlabel("x")
ax.set_ylabel("$\Delta$U")
ax.set_title("Varmelikning - Avvik fra analytisk verdi")
ax.legend()
plt.tight_layout
fig.subplots_adjust(left=0.15)

def update(frame):
    global u_expl, u_impl, u_cn, time
    u_expl = step_explicit(u_expl)
    u_impl = step_implicit(u_impl)
    u_cn   = step_crank_nicolson(u_cn)
    time += k

    current_exact_solution = exact_solution(x, time)
    line_expl.set_ydata(abs(u_expl-current_exact_solution))
    line_impl.set_ydata(abs(u_impl-current_exact_solution))
    line_cn.set_ydata(abs(u_cn-current_exact_solution))
    # line_exact.set_ydata(current_exact_solution)

    return (line_expl, line_impl, line_cn)

interval = 50
fps = 1000/interval

anim = FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=True)
anim.save(f'sammenlikning-{N}.gif', writer='pillow', fps=fps)
plt.show()
