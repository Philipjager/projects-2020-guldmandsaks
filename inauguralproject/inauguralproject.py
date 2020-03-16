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
    c = m + w*l - tau0*w*l - tau1*max(w*l-kappa,0)
    return -u_func(l,c,V,epsilon)

sol_case1 = optimize.minimize_scalar(
value_of_choice,method='bounded',
bounds=(0,1),args=(m,V,epsilon,tau0,tau1,kappa))

l_svar = sol_case1.x
c_svar = m + w*l_svar - tau0*w*l_svar + tau1*max(w*l_svar-kappa,0)
u = u_func(l_svar,c_svar,V,epsilon)

# print(f'l_svar = {l_svar:.3f}',f'c_svar = {c_svar:.3f} ->', f'u = {u:.3f}')

# Verificerer at det er et max

print(f'u1 = {np.log(m + w*0.40 - tau0*w*0.40 - tau1*max(w*0.40-kappa,0))- V*(0.40**(1+1/epsilon)/(1+1/epsilon)):.5f}')
print(f'u2 = {np.log(m + w*0.45 - tau0*w*0.45 - tau1*max(w*0.45-kappa,0))- V*(0.45**(1+1/epsilon)/(1+1/epsilon)):.5f}')
print(f'u3 = {np.log(m + w*0.42 - tau0*w*0.42 - tau1*max(w*0.42-kappa,0))- V*(0.42**(1+1/epsilon)/(1+1/epsilon)):.5f}')

# opgave 2

w_values = []
l_values = []
c_values = []

for w in np.linspace(0.5,1.5,1000):
    sol_case1 = optimize.minimize_scalar(
    value_of_choice,method='bounded',
    bounds=(0,1),args=(m,V,epsilon,tau0,tau1,kappa))
    
    l_svar = sol_case1.x
    c_svar = m + w*l_svar - tau0*w*l_svar - tau1*max(w*l_svar-kappa,0)
    

    w_values.append(w)

    l_values.append(l_svar)

    c_values.append(c_svar)

#print(w_values,l_values,c_values)
#print(f'w = {w:.3f}' , f'l_svar = {l_svar:.3f}',f'c_svar = {c_svar:.3f} ->', f'u = {u:.3f}')


# Plot figur
fig = plt.figure(figsize=(14,6))

# left plot
ax_left = fig.add_subplot(1,2,1)

ax_left.plot(w_values,c_values)
#ax_left.scatter(w_values,c_values)

ax_left.set_title('Optimalt forbrug ved forskellig realløn')
ax_left.set_xlabel('$w$')
ax_left.set_ylabel('$c$')
ax_left.grid(True)

# right plot
ax_left = fig.add_subplot(1,2,2)

ax_left.plot(w_values,l_values)
#ax_left.scatter(w_values,l_values)

ax_left.set_title('Optimalt arbejdsudbud ved forskellig realløn')
ax_left.set_xlabel('$w$')
ax_left.set_ylabel('$l$')
ax_left.grid(True)
<<<<<<< HEAD

# Opgave 3
m = 1
V = 10
epsilon = 0.3
tau0 = 0.4
tau1 = 0.1
kappa = 0.4

w_values = []
l_values = []
c_values = []

np.random.seed(2020)

for w in np.random.uniform(low=0.5,high=1.5,size=10000):
    sol_case1 = optimize.minimize_scalar(
    value_of_choice,method='bounded',
    bounds=(0,1),args=(m,V,epsilon,tau0,tau1,kappa))
    
    l_svar = sol_case1.x
    c_svar = m + w*l_svar - tau0*w*l_svar - tau1*max(w*l_svar-kappa,0)
    

    w_values.append(w)

    l_values.append(l_svar)

    c_values.append(c_svar)

w_i = np.array(w_values)
l_i = np.array(l_values)
c_i = np.array(c_values)

number = 0.4
elements = 10000
tau0_i = np.array([number] * elements)

hej = 0.1
tau1_i = np.array([hej] * elements)

hallo = 0.4
kappa_i = np.array([hallo] * elements)



T = sum(tau0_i*w_i*l_i+tau1_i*np.max(w_i*l_i-kappa_i,0))
print(T)
print(l_svar, c_svar)

# Opgave 4
m = 1
V = 10
epsilon = 0.1
tau0 = 0.4
tau1 = 0.1
kappa = 0.4

w_values = []
l_values = []
c_values = []

np.random.seed(2020)

for w in np.random.uniform(low=0.5,high=1.5,size=10000):
    sol_case1 = optimize.minimize_scalar(
    value_of_choice,method='bounded',
    bounds=(0,1),args=(m,V,epsilon,tau0,tau1,kappa))
    
    l_svar = sol_case1.x
    c_svar = m + w*l_svar - tau0*w*l_svar - tau1*max(w*l_svar-kappa,0)
    

    w_values.append(w)

    l_values.append(l_svar)

    c_values.append(c_svar)

w_i = np.array(w_values)
l_i = np.array(l_values)
c_i = np.array(c_values)

number = 0.4
elements = 10000
tau0_i = np.array([number] * elements)

hej = 0.1
tau1_i = np.array([hej] * elements)

hallo = 0.4
kappa_i = np.array([hallo] * elements)



T = sum(tau0_i*w_i*l_i+tau1_i*np.max(w_i*l_i-kappa_i,0))
print(T)



Master Coda

=======
