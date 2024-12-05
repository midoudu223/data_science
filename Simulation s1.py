import numpy as np 
from scipy.integrate import odeint 
def our_system(variables, t, beta, theta, gamma_E, gamma_I, pi_1, gamma_1, pi_2, gamma_Ih, gamma_Iicu, gamma_H, gamma_icu, gamma_Hicu, ):
    S, E, I, Is, Im, Ih, Iicu, H1, H2, Hicu, ICU1, ICU2, R=variables
    dS=-beta*S*(I+Is+Im)+theta*R
    dE= beta*S*(I+Is+Im)-gamma_E*E 
    dI=gamma_E*E-gamma_I*I 
    dIs=pi_1*gamma_I*I-gamma_1*Is 
    dIm=(1-pi_1)*gamma_I*I-gamma_1*Im 
    dIh=pi_2*gamma_1*Is-gamma_Ih*Ih 
    dIicu=(1-pi_2)*gamma_1*Is-gamma_Iicu*Iicu 
    dH1=gamma_Ih*Ih-gamma_H*H1 
    dH2=gamma_H*H1-gamma_H*H2 
    dHicu=gamma_icu*Iicu-gamma_Hicu*Hicu 
    dICU1=gamma_Hicu*Hicu-gamma_icu*ICU1 
    dICU2=gamma_icu*ICU1-gamma_icu*ICU2 
    dR=gamma_1*Im+gamma_H*H2+gamma_icu*ICU2-theta*R
    return [dS,dE,dI,dIs,dIm,dIh,dIicu,dH1,dH2,dHicu,dICU1,dICU2,dR]
#Parameters for R0 < 1
beta = 100.98e-4 #(R0>1)
#beta = 1.98e-4 #(R0<1)
theta = 0.3
gamma_E = 0.25
gamma_I = 1
pi_1 = 0.2
gamma_1 = 0.3
pi_2 = 0.215
gamma_Ih = 0.16
gamma_Iicu = 0.5
gamma_H = 0.16
gamma_Hicu = 0.3
gamma_icu = 0.66
#Time
time=np.linspace(0,60,1000)
#Initial values
IV=[150,100,56,100,20,6.9,5,4,1.5,1,1,1,0]
#Resolution
solution=odeint(our_system, IV, time, args=(beta,theta, gamma_E, gamma_I, pi_1, gamma_1, gamma_Ih, pi_2, gamma_Iicu, gamma_H, gamma_icu, gamma_Hicu))
#Plotting
import matplotlib.pyplot as plt
S=solution[:, 0]
E=solution[:, 1]
I=solution[:, 2]
Is=solution[:, 3]
Im=solution[:, 4]
Ih=solution[:, 5]
Iicu=solution[:, 6]
H1=solution[:, 7]
H2=solution[:, 8]
Hicu=solution[:, 9]
ICU1=solution[:, 10]
ICU2=solution[:, 11]
R=solution[:, 12]
plt.figure(figsize=(12,8), layout='constrained')
plt.subplot(121)
plt.plot(time, S, '--', label='S')
plt.plot(time, E, label='E')
plt.plot(time, I, label='I')
#plt.plot(time, Is, label='Is')
#plt.plot(time, Im, label='Im')
#plt.plot(time, Ih, label='Ih')
#plt.plot(time, Iicu, label='Iicu')
#plt.plot(time, H1, label='H1')
#plt.plot(time, H2, label='H2')
#plt.plot(time, Hicu, label='Hicu')
#plt.plot(time, ICU1, label='ICU1')
#plt.plot(time, ICU2, label='ICU2')
plt.plot(time, R, label='R')

plt.title('System evolution for R0<1')
plt.xlabel('Time (days)')
plt.ylabel('Population number')
plt.legend()
plt.grid(True)
plt.subplot(122)
#plt.plot(time, S, '--', label='S')
#plt.plot(time, E, label='E')
#plt.plot(time, I, label='I')
plt.plot(time, Is, label='Is')
plt.plot(time, Im, label='Im')
plt.plot(time, Ih, label='Ih')
plt.plot(time, Iicu, label='Iicu')
plt.plot(time, H1, label='H1')
plt.plot(time, H2, label='H2')
plt.plot(time, Hicu, label='Hicu')
plt.plot(time, ICU1, label='ICU1')
plt.plot(time, ICU2, label='ICU2')
#plt.plot(time, R, label='R')

plt.title('System evolution for R0<1')
plt.xlabel('Time (days)')
plt.ylabel('Population number')
plt.legend()
plt.grid(True)
plt.show()