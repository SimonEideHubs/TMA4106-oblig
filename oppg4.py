import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# parametre for metoden (Set rimelige verdier for rimelige resultater)
d = np.pi
N = 100                      # punkter i rom
h = d / N                   # punkter i tid
k = 0.001                   # steglengde i tid
num_frames = 200            # antall steg i tid
x = np.linspace(0, d, N+1)

# Sjekke stabilitet for metoden
if k > h**2 / 2:
    print("Warning: time step k is too large for stability! Reduce k or increase N.")

# Lag romlig punktnett (I en dimensjon, så bare en linje)
x = np.linspace(0, d, N+1)
u = (np.sin(x)) # Startstilstand (sin(x) fra oppgaven, men andre former er gøyere)

# Forrige verdier for å lage de neste
u_prev = u.copy()
u_next = u.copy()

def update(frame):
    global u_prev, u_next

    for i in range(1, N):
        u_next[i] = u_prev[i] + (k/h**2) * (u_prev[i+1] - 2*u_prev[i] + u_prev[i-1])
    
    # Randbetingelser (Også litt gøy å leke rundt med)
    u_next[0] = 0.0
    u_next[N] = 0.0
    
    # Det nye lagres som det gamle
    u_prev, u_next = u_next, u_prev
    
    # send data til plot
    line.set_ydata(u_prev)
    return line,

fig, ax = plt.subplots()
line, = ax.plot(x, u, color='red', label='Varmefordeling')
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0, d)
ax.set_xlabel('x')
ax.set_ylabel('Temperatur u(x, t)')
ax.set_title('1D Varmelikning: eksplisitt Euler')
ax.legend()

interval = 50
fps = 1000/interval

anim = FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=True)
anim.save(f'oppg4_{N}.gif', writer='pillow', fps=fps)
plt.show()