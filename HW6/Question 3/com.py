import numpy as np

def center_of_mass(R,N):
    # random points in a cube
    x = np.random.uniform(-R, R, N)
    y = np.random.uniform(-R, R, N)
    z = np.random.uniform(-R, R, N)

    #for making the spherical boundaries
    boundary=x**2+y**2+z**2
    true_false=boundary<=R
    x_filtered=x[true_false]
    y_filtered=y[true_false]
    z_filtered=z[true_false]

    #define density
    rho_0=2
    rho_z=3/4*rho_0+(rho_0/(4*R))*z_filtered

    total_mass_integral=
    
        
    
    
    
    
    return x_com

