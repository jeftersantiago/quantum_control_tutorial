from qutip import * 
import numpy as np 
import matplotlib.pyplot as plt 

font = { 'weight' : 'bold',
        'size'   : 16}
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
plt.rc('text', usetex=True)
plt.rc('font', **font) 
plt.rcParams['savefig.dpi'] = 300

def g(t, tau):
    return -5 + 10 * t / tau

# Not inputing the time dependent term explicitly here.
def H_LZ(delta, v):
    return delta * sigmax() + v * sigmaz()

def H_CD(delta, v, gamma):
    return H_LZ(delta, v) - gamma * sigmay()

def energy(tau, delta = 1.0, N = 101):
    times = np.linspace(0.0, tau, N)
    E_g, E_e = np.zeros((N)), np.zeros((N))

    for i, t in enumerate(times):
        energy = H_LZ(delta, g(t, tau)).eigenenergies()
        E_g[i], E_e[i] = energy[0], energy[1]
    return E_g, E_e

def cd_energy(tau, delta = 1.0, N = 101):
    times = np.linspace(0.0, tau, N)
    E_g, E_e = np.zeros((N)), np.zeros((N))

    for i, t in enumerate(times):
        
        dv = 10 / tau
        gamma = delta  / (2 * (delta**2 + g(t, tau)**2)) * dv

        energy = H_CD(delta, g(t, tau), gamma).eigenenergies()
        E_g[i], E_e[i] = energy[0], energy[1]
    return E_g, E_e


if __name__ == "__main__":

    tau1 = 1.0
    tau2 = 0.5
    tau3 = 0.7

    N = 101 

    t = np.linspace(0, tau1, N)

    E_g, E_e = energy(tau1)

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    ax.plot(t, E_g, 'k')
    ax.plot(t, E_e, 'k')

    
    Ecd_g, Ecd_e = cd_energy(tau2)
    ax.plot(t, Ecd_g, '--', color="red", label = "$\tau = 1/2$")
    ax.plot(t, Ecd_e, '--', color="red")

    Ecd_g, Ecd_e = cd_energy(tau3)
    ax.plot(t, Ecd_g, '-.', color="green", label = "$\tau = 3/4$")
    ax.plot(t, Ecd_e, '-.', color="green")
