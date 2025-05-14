import numpy as np
import matplotlib.pyplot as plt



def euler(h):
    #i want the time be the same for all of my functions
    #omega=1
    time = np.arange(0, 60, h)
    l=len(time)
    xs = [1]
    vs = [0]
    for n in range(l - 1):
        x_new = xs[n] + h * vs[n]
        v_new = vs[n] - h * xs[n]
        xs.append(x_new)
        vs.append(v_new)

    return time, np.array(vs), np.array(xs)


def real_sol(h):
    #i want the time be the same for all of my functions
    #omega=1
    time = np.arange(0, 60, h)
    xs = np.cos(time)
    vs = -np.sin(time)
    return time, vs, xs


#other solution with cromer
def euler_cromer(h):
    #i want the time be the same for all of my functions
    #omega=1
    time = np.arange(0, 60, h)
    l=len(time)
    xs = [1]
    vs = [0]
    for n in range(l - 1):
        v_new = vs[n] - h * xs[n]
        vs.append(v_new)
        x_new = xs[n] + h * vs[n+1]
        xs.append(x_new)
        

    return time, np.array(vs), np.array(xs)

#leap frog
def leap(h):
    #a=-1
    time = np.arange(0, 60, h)
    xs = [1]
    #vs_full=[0]
    #we need to use euler for the first step as explained
    vs_half=[0.5*h*1]
    
    for n in range(len(time) - 1):
        #v_full_new=vs_full[n]-xs[n]*h
        #vs_full.append(v_full_new)
        vs_half_new = vs_half[n]-xs[n]* h
        vs_half.append(vs_half_new)
        x_new = xs[n] + vs_half[n + 1] * h
        xs.append(x_new)
    #an average
    vs_full = []
    for i in range(1,len(time)):
        v_full = (vs_half[i-1] + vs_half[i]) / 2
        vs_full.append(v_full)
    vs_full.append(vs_half[-1] - 0.5 * h * xs[-1])
    
        
    return time, np.array(vs_full), np.array(xs)


def verlet(h):
    # a = -x 
    time = np.arange(0, 60, h)
    xs = [1] 
    vs = [0] 
    #again i need to use euler for derving another value
    x1 = xs[0] + h * vs[0]
    xs.append(x1)
    v1=(xs[1]-xs[0])/(2*h)
    vs.append(v1)
    for n in range(1, len(time)-1):
        x_new = 2*xs[n]-xs[n-1] -xs[n]*h*h
        xs.append(x_new)
        v_new = (xs[n+1] - xs[n-1]) / (2 * h)
        vs.append(v_new)
    
    return time, np.array(vs), np.array(xs)


def Vverlet(h):
    # a = -x 
    time = np.arange(0, 60, h)
    xs = [1] 
    vs = [0] 
    
    for n in range(len(time)-1):
        x_new = xs[n]+h*vs[n] -0.5*xs[n]*h*h
        xs.append(x_new)
        v_new = vs[n]-0.5*h*(xs[n]+xs[n+1])
        vs.append(v_new)
    
    return time, np.array(vs), np.array(xs)

def beeman(h):
   
    time = np.arange(0, 60, h)
    xs = [1] 
    vs = [0]

    #use VV for the first step calculation for less error instead of euler
    x1 = xs[0] + h * vs[0] + (1/2) * (-xs[0]) * h**2
    xs.append(x1)
    #let's get the first velocity too
    v1 = vs[0] + (1/2) * (-xs[0] + -xs[1]) * h 
    vs.append(v1)

   
    for n in range(1, len(time)-1):
       
        x_new = xs[n] + vs[n] * h + (1/6) * (4 * (-xs[n]) - (-xs[n-1])) * h**2
        xs.append(x_new)

       
        v_new = vs[n] + (1/6) * (2 * (-xs[n+1]) + 5 * (-xs[n]) - (-xs[n-1])) * h
        vs.append(v_new)

    return time, np.array(vs), np.array(xs)

    
h=0.01
T_real, V_real, X_real = real_sol(h)
T_euler, V_euler, X_euler = euler(h)
T_cromer, V_cromer, X_cromer =  euler_cromer(h)
T_leap, V_leap, X_leap = leap(h)
T_verlet, V_verlet, X_verlet = verlet(h)
T_Vverlet, V_Vverlet, X_Vverlet = Vverlet(h)
T_B, V_B, X_B = beeman(h)


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(T_real, X_real, label='exact', linestyle='--')
plt.plot(T_euler, X_euler, label='euler', alpha=0.7)
plt.plot(T_cromer, X_cromer, label='cromer', alpha=0.7)
plt.plot(T_leap, X_leap, label='leap', alpha=0.7)
plt.plot(T_verlet, X_verlet, label='verlet', alpha=0.7)
plt.plot(T_Vverlet, X_Vverlet, label='Vverlet', alpha=0.7)
plt.plot(T_B, X_B, label='beeman', alpha=0.7)
plt.xlabel("T")
plt.ylabel("X")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(X_real, V_real, label='exact', linestyle='--')
plt.plot(X_euler, V_euler, label='euler', alpha=0.7)
plt.plot(X_cromer, V_cromer, label='cromer', alpha=0.7)
plt.plot(X_leap, V_leap, label='leap', alpha=0.7)
plt.plot(X_verlet, V_verlet, label='verlet', alpha=0.7)
plt.plot(X_Vverlet, V_Vverlet, label='Vverlet', alpha=0.7)
plt.plot(X_B, V_B, label='beeman', alpha=0.7)
plt.xlabel("X")
plt.ylabel("V")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




'''
import numpy as np
import matplotlib.pyplot as plt



def euler(h):
    #i want the time be the same for all of my functions
    #omega=1
    time = np.arange(0, 60, h)
    l=len(time)
    xs = [1]
    vs = [0]
    for n in range(l - 1):
        x_new = xs[n] + h * vs[n]
        v_new = vs[n] - h * xs[n]
        xs.append(x_new)
        vs.append(v_new)

    return time, np.array(vs), np.array(xs)


def real_sol(h):
    #i want the time be the same for all of my functions
    #omega=1
    time = np.arange(0, 60, h)
    xs = np.cos(time)
    vs = -np.sin(time)
    return time, vs, xs


#other solution with cromer
def euler_cromer(h):
    #i want the time be the same for all of my functions
    #omega=1
    time = np.arange(0, 60, h)
    l=len(time)
    xs = [1]
    vs = [0]
    for n in range(l - 1):
        v_new = vs[n] - h * xs[n]
        vs.append(v_new)
        x_new = xs[n] + h * vs[n+1]
        xs.append(x_new)
        

    return time, np.array(vs), np.array(xs)

#leap frog
def leap(h):
    #a=-1
    time = np.arange(0, 60, h)
    xs = [1]
    #vs_full=[0]
    #we need to use euler for the first step as explained
    vs_half=[0.5*h*1]
    
    for n in range(len(time) - 1):
        #v_full_new=vs_full[n]-xs[n]*h
        #vs_full.append(v_full_new)
        vs_half_new = vs_half[n]-xs[n]* h
        vs_half.append(vs_half_new)
        x_new = xs[n] + vs_half[n + 1] * h
        xs.append(x_new)
    #an average
    vs_full = []
    for i in range(1,len(time)):
        v_full = (vs_half[i-1] + vs_half[i]) / 2
        vs_full.append(v_full)
    vs_full.append(vs_half[-1] - 0.5 * h * xs[-1])
    
        
    return time, np.array(vs_full), np.array(xs)


def verlet(h):
    # a = -x 
    time = np.arange(0, 60, h)
    xs = [1] 
    vs = [0] 
    #again i need to use euler for derving another value
    x1 = xs[0] + h * vs[0]
    xs.append(x1)
    v1=(xs[1]-xs[0])/(2*h)
    vs.append(v1)
    for n in range(1, len(time)-1):
        x_new = 2*xs[n]-xs[n-1] -xs[n]*h*h
        xs.append(x_new)
        v_new = (xs[n+1] - xs[n-1]) / (2 * h)
        vs.append(v_new)
    
    return time, np.array(vs), np.array(xs)


def Vverlet(h):
    # a = -x 
    time = np.arange(0, 60, h)
    xs = [1] 
    vs = [0] 
    
    for n in range(len(time)-1):
        x_new = xs[n]+h*vs[n] -0.5*xs[n]*h*h
        xs.append(x_new)
        v_new = vs[n]-0.5*h*(xs[n]+xs[n+1])
        vs.append(v_new)
    
    return time, np.array(vs), np.array(xs)

def beeman(h):
   
    time = np.arange(0, 60, h)
    xs = [1] 
    vs = [0]

    #use VV for the first step calculation for less error instead of euler
    x1 = xs[0] + h * vs[0] + (1/2) * (-xs[0]) * h**2
    xs.append(x1)
    #let's get the first velocity too
    v1 = vs[0] + (1/2) * (-xs[0] + -xs[1]) * h 
    vs.append(v1)

   
    for n in range(1, len(time)-1):
       
        x_new = xs[n] + vs[n] * h + (1/6) * (4 * (-xs[n]) - (-xs[n-1])) * h**2
        xs.append(x_new)

       
        v_new = vs[n] + (1/6) * (2 * (-xs[n+1]) + 5 * (-xs[n]) - (-xs[n-1])) * h
        vs.append(v_new)

    return time, np.array(vs), np.array(xs)


#needs improvment'''
'''#accuracy calculation
hs=[0.5 ,0.1, 0.05, 0.01, 0.005, 0.001]
deltahE=[]
deltahC=[]
for h in hs:
    T_real, V_real, X_real = real_sol(h)
    T_euler, V_euler, X_euler = euler(h)
    T_cromer, V_cromer, X_cromer =  euler_cromer(h)
    #T_leap, V_leap, X_leap = leap(h)
    #T_verlet, V_verlet, X_verlet = verlet(h)
    #T_Vverlet, V_Vverlet, X_Vverlet = Vverlet(h)
    #T_B, V_B, X_B = beeman(h)

    dif_eulerx=(X_real[-1]-X_euler[-1])**2
    dif_eulerv=(V_real[-1]-V_euler[-1])**2
    dif_Cx=(X_real[-1]-X_cromer[-1])**2
    dif_Cv=(V_real[-1]-V_cromer[-1])**2
    
    delta_euler=np.sqrt(dif_eulerx+dif_eulerv)
    delta_cromer=np.sqrt(dif_Cx+dif_Cv)
    deltahE.append(delta_euler)
    deltahC.append(delta_cromer)
#plt.plot(hs, deltahE)
plt.plot(hs, deltahC)
plt.show()'''



'''hs =[0.001,0.005,0.01,0.05,0.1]
#i will creat a dictionary to save each algorithm's error with its own label
All_errors = {'euler': [], 'cromer': [], 'leapfrog': [], 'verlet': [], 'Vverlet': [], 'beeman': []}

for h in hs:
    T_real, V_real, X_real = real_sol(h)
    T_euler, V_euler, X_euler = euler(h)
    T_cromer, V_cromer, X_cromer = euler_cromer(h)
    T_leap, V_leap, X_leap = leap(h)
    T_verlet, V_verlet, X_verlet = verlet(h)
    T_Vverlet, V_Vverlet, X_Vverlet = Vverlet(h)
    T_B, V_B, X_B = beeman(h)
    
    #each key is an array
    All_errors['euler'].append(np.sqrt((X_real[-1]-X_euler[-1])**2 + (V_real[-1]-V_euler[-1])**2))
    All_errors['cromer'].append(np.sqrt((X_real[-1]-X_cromer[-1])**2 + (V_real[-1]-V_cromer[-1])**2))
    All_errors['leapfrog'].append(np.sqrt((X_real[-1]-X_leap[-1])**2 + (V_real[-1]-V_leap[-1])**2))
    All_errors['verlet'].append(np.sqrt((X_real[-1]-X_verlet[-1])**2 + (V_real[-1]-V_verlet[-1])**2))
    All_errors['Vverlet'].append(np.sqrt((X_real[-1]-X_Vverlet[-1])**2 + (V_real[-1]-V_Vverlet[-1])**2))
    All_errors['beeman'].append(np.sqrt((X_real[-1]-X_B[-1])**2 + (V_real[-1]-V_B[-1])**2))


plt.figure(figsize=(12, 8))
plt.loglog(hs, All_errors['euler'], label='euler')
plt.loglog(hs, All_errors['cromer'], label='cromer')
plt.loglog(hs, All_errors['leapfrog'], label='leapfrog')
plt.loglog(hs, All_errors['verlet'], label='verlet')
plt.loglog(hs, All_errors['Vverlet'], label='velocity verlet')
plt.loglog(hs, All_errors['beeman'], label='beeman')
ae, be=np.polyfit(np.log(hs), np.log(All_errors['euler']), 1)
ac,bc=np.polyfit(np.log(hs), np.log(All_errors['cromer']), 1)
al, bl=np.polyfit(np.log(hs), np.log(All_errors['leapfrog']),1)
av,bv=np.polyfit(np.log(hs), np.log(All_errors['verlet']), 1)
avv,bvv=np.polyfit(np.log(hs), np.log(All_errors['Vverlet']), 1)
ab, bb=np.polyfit(np.log(hs), np.log(All_errors['beeman']), 1)
print(f"slop for euler=={ae}, cromer={ac},leapfrog={al},verlet={av}, Vverlet={avv}, beeman={ab} ")
plt.xlabel('h')
plt.ylabel('error with the real result in the phase space')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()'''
    
    
    
    

