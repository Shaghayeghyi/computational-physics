import numpy as np

def center_of_mass(R,N):
    # random points in a cube
    x = np.random.uniform(-R, R, N)
    y = np.random.uniform(-R, R, N)
    z = np.random.uniform(-R, R, N)

    #for making the spherical boundaries
    boundary=x**2+y**2+z**2
    true_false=boundary<=R**2
    x_filtered=x[true_false]
    y_filtered=y[true_false]
    z_filtered=z[true_false]
    N_filtered=len(z_filtered)

    #define density
    rho_0=2
    rho_z=3/4*rho_0+(rho_0/(4*R))*z_filtered

    #mass  
    total_mass_integral=(4/3*np.pi*R**3)*np.mean(rho_z)
    #z_com
    z_com=(4/3*np.pi*R**3)*np.mean(rho_z*z_filtered)/total_mass_integral
    #x_com
    x_com=(4/3*np.pi*R**3)*np.mean(rho_z*x_filtered)/total_mass_integral
    #y_com
    y_com=(4/3*np.pi*R**3)*np.mean(rho_z*y_filtered)/total_mass_integral



    #error
    #z
    z_er=(4/3*np.pi*R**3)*np.std(rho_z*z_filtered)/total_mass_integral/np.sqrt(N_filtered)
    #x
    x_er=(4/3*np.pi*R**3)*np.std(rho_z*x_filtered)/total_mass_integral/np.sqrt(N_filtered)
    #y
    y_er=(4/3*np.pi*R**3)*np.std(rho_z*y_filtered)/total_mass_integral/np.sqrt(N_filtered)
    
    
    
    
    
        
    
    
    
    
    return z_com, x_com, y_com, z_er,x_er,y_er

# Example usage
R = 15
z,x,y,z_er,x_er,y_er = center_of_mass(R,1000000)
print(f"Numerical z,x,y: {z,x,y}")
print(f"Exact z,x,y: {R/15,0,0}")
print(f"Error for z,x,y:{z_er,x_er,y_er}")
