from scipy import optimize
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import ipywidgets as widgets

# Opgave. 1

w = 1
m = 1
V = 10
epsilon = 0.3
tau0 = 0.4
tau1 = 0.1
kappa = 0.4

def u_func(l,c,V,epsilon):
    return np.log(c) - V*(l**(1+1/epsilon)/(1+1/epsilon))

def value_of_choice(l,m,V,epsilon,tau0,tau1,kappa):
    c = m + w*l - tau0*w*l + tau1*max(w*l-kappa,0)
    return -u_func(l,c,V,epsilon)

sol_case1 = optimize.minimize_scalar(
value_of_choice,method='bounded',
bounds=(0,1),args=(m,V,epsilon,tau0,tau1,kappa))

l_svar = sol_case1.x
c_svar = m + w*l_svar - tau0*w*l_svar + tau1*max(w*l_svar-kappa,0)
u = u_func(l_svar,c_svar,V,epsilon)

print(f'l_svar = {l_svar:.3f}',f'c_svar = {c_svar:.3f} ->', f'u = {u:.3f}')

# Verificerer at det er et max
print(f'u1 = {np.log(m + w*0.40 - tau0*w*0.40 + tau1*max(w*0.40-kappa,0))- V*(0.40**(1+1/epsilon)/(1+1/epsilon)):.3f}')
print(f'u2 = {np.log(m + w*0.45 - tau0*w*0.45 + tau1*max(w*0.45-kappa,0))- V*(0.45**(1+1/epsilon)/(1+1/epsilon)):.3f}')
print(f'u3 = {np.log(m + w*0.42 - tau0*w*l_svar + tau1*max(w*0.42-kappa,0))- V*(0.42**(1+1/epsilon)/(1+1/epsilon)):.3f}')

for w in np.linspace(0.5,1.5,20):
    sol_case1 = optimize.minimize_scalar(
    value_of_choice,method='bounded',
    bounds=(0,1),args=(m,V,epsilon,tau0,tau1,kappa))

    l_svar = sol_case1.x
    c_svar = m + w*l_svar - tau0*w*l_svar + tau1*max(w*l_svar-kappa,0)
    u = u_func(l_svar,c_svar,V,epsilon)
    
    #print(f'w = {w:.3f}' , f'l_svar = {l_svar:.3f}',f'c_svar = {c_svar:.3f} ->', f'u = {u:.3f}')

for w in np.linspace(0.5,1.5,20):
    values = []
    values.append(w)
    values.append(l_svar)
    values.append(c_svar)
    print(values)

# Plot figur
fig = plt.figure(figsize=(10,4))

# left plot
ax_left = fig.add_subplot(1,2,1)

ax_left.plot(values[0], values[2])
ax_left.scatter(values[0], values[2])

ax_left.set_title('value of choice, $u(x_1,x_2)$')
ax_left.set_xlabel('$x_1$')
ax_left.set_ylabel('$u(x_1,(I-p_1 x_1)/p_2)$')
ax_left.grid(True)
plt.show()

Master Coda

pik∏
