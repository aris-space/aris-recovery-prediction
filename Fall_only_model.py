''' fall model only'''
import numpy as np
import matplotlib.pyplot as plt

'''alle Angaben sind in den si Einheiten'''

WS = 5.5  #float(input("Windspeed\n >>>"))
H = 80    #float(input("Fall height\n >>>"))
V = 8    #float(input("velocity of fall\n>>>"))
Theta_deg = 0 #float(input("angle of wind in deg\n>>>"))

T = H/V 

''' C_d ist der Wiederstandskoefizient'''
WindSpeed = WS
roh = 1.002
C_d = 0.45


def WindForce(WindSpeed, roh, A, C_d):
    ''' Funktion der Kraft des Windes auf den Körper.
    Für die Kraft wird die Formel des Windwiederstandes genutzt'''
    
    v = WindSpeed
    
    wind_force = C_d * roh * A * (v**2)/2
    
    # print (wind_force)
    return wind_force
    
def WindEffect (WindSpeed, Theta_deg, C_d, T):
    ''' Effekt der Windkraft auf die Rakete
    A enspricht der Fläche, roh der Dichte der Luft, m der Masse des körpers'''
    roh = 1.002
    A = 0.20
    m = 0.45
    
    '''winkel zu radians konvertieren'''
    Theta_rad = np.radians(Theta_deg)
    
    '''aufsetzten der verschiedenen Variablen und arrays'''
    v_x = WindSpeed * np.sin(Theta_rad)
    v_y = WindSpeed * np.cos(Theta_rad)
    

    a_x = (WindForce(roh, v_x, C_d, A) / m) * np.cos(Theta_rad)
    a_y = (WindForce(roh, v_y, C_d, A) / m) * np.sin(Theta_rad)
    
   
    s_x = 0
    s_y = 0
   
    s_x_array = np.array ([0])
    s_y_array = np.array ([0])
    
    v_x_array = np.array([0])
    v_y_array = np.array([0])
    counter = 0
    
    t_array = np.array([0])
    t_total = 0 
    while t_total < T:
        
        '''veränderung über Zeit'''
        intervall = 0.01 
        t = intervall 
        t_total = t_total + t
        counter += t
        
        v_x += a_x * t
        v_y += a_y * t
        
        s_x += v_x * t
        s_y += v_y * t
        
        v_x_array = np.append(v_x_array, v_x)
        v_y_array = np.append(v_y_array, v_y)
        
        s_x_array = np.append(s_x_array, s_x)
        s_y_array = np.append(s_y_array, s_y)
        
        
        t_array = np.append(t_array, t_total)
        
    return v_x_array, v_y_array, s_x_array, s_y_array, t_array

v_x_values, v_y_values, s_x_values, s_y_values, t_values = WindEffect(WindSpeed, Theta_deg, C_d, T)

  

#plt.plot (t_values, v_y_values)
plt.plot (s_x_values, s_y_values)
#plt.plot (t_values, v_x_values)








#print (len (t_values))

#print (v_x_values, v_y_values, s_x_values, s_y_values)  

#s_x_values_len = len(s_x_values)
#s_x_values_last_element = s_x_values [s_x_values_len - 1]
#
#s_y_values_len = len(s_y_values)
#s_y_values_last_element = s_y_values [s_y_values_len - 1]
#
#distance =np.sqrt( s_x_values_last_element**2 + s_y_values_last_element**2)
#sin_of_angle = s_y_values_last_element / distance
#heading = np.round( 90 - (np.degrees(np.arcsin(sin_of_angle))), 0)

#print (sin_of_angle)
#print (heading)
#print (s_x_values_last_element)
#print (s_y_values_last_element)     
#print (distance, heading)       
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        