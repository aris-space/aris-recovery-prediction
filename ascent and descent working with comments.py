# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:09:52 2020

@author: alexd
"""

'''import der benötigten Bibliotheken'''
import numpy as np
import matplotlib.pyplot as plt
from pyowm.owm import OWM


'''aufsetzten der Wetter-API'''
owm = OWM("3da867753ae4a50709b6ee69016a6330")
mgr = owm.weather_manager()
observation = mgr.weather_at_place("Maienfeld, CH")
wind = observation.weather.wind()
# wind ["gust"]
print (wind)


'''Deklarieren der Variablen'''
roh = 1.22
C_d = 1.28
t_b = 1.2
F = 4.5
m = 0.095
a_burn = F / m
A = 0.20
A_Para = 0.216
dt = 0.01
D = 0.5 * C_d * roh * A_Para


'''Daten der Api in das Programm integrieren'''
Theta_deg = wind["deg"]
WindSpeed = wind["speed"]

g = 9.81
v_z = a_burn * t_b

h_max = v_z**2 / (2 * g)

# t_s = v0 / g
# t_f = np.sqrt (h_max / g - a_para)
# t_total = t_s + t_f



def WindForce(WindSpeed, roh, A, C_d):
    ''' Funktion der Kraft des Windes auf den Körper.
    Für die Kraft wird die Formel des Windwiederstandes genutzt'''
    
    v = WindSpeed
    
    wind_force = C_d * roh * A * ( v**2 ) /2
    
    # print (wind_force)
    return wind_force


def AccelerationWithDrag(g, m, D, v_z):
    '''Fallschirm als eine Funktion Definieren'''
    a_z = g - (D * v_z ** 2) / m
    
    return a_z


def VerticalFlight (v0, g, WindSpeed, Theta_deg, C_d):
    
    Theta_rad = np.radians(Theta_deg)
    
    '''aufsetzen der verschiedenen Dimensionen'''
    t1 = 0
    t2 = 0
    
    v_x = WindForce (WindSpeed, roh, A, C_d) * dt / m * np.sin(Theta_rad)
    v_y = WindForce (WindSpeed, roh, A, C_d) * dt / m * np.cos(Theta_rad)
    v_z = a_burn * t_b
    
    a_x = (WindForce(roh, v_x, C_d, A) / m) * np.cos(Theta_rad)
    a_y = (WindForce(roh, v_y, C_d, A) / m) * np.sin(Theta_rad)
    
    s_x = 0
    s_y = 0
    
    ''''Arrays aufsetzten um die Werte zu speichern'''
    s_x_array = np.array ([0])
    s_y_array = np.array ([0])
    s_z_array = np.array ([0])
   
#    
    v_x_array = np.array([0])    
    v_y_array = np.array([0])    
    v_z_array = np.array([0])    
    
    t_array = np.array([0])
    h1 = 0

    while round(h1, 3) < round(h_max, 3):
        ''' While-Loop für den start'''
        
        t1 += dt
        
        h1 = v0 * t1 - g / 2 * t1 ** 2
        
        
        '''errechnung der neunen Geschwindigkeiten und Speicherung in Arrays'''
        v_x += a_x * dt
        v_y += a_y * dt
        v_z -= g * dt

        s_x += v_x * dt
        s_y += v_y * dt

        v_x_array = np.append(v_x_array, v_x)
        v_y_array = np.append(v_y_array, v_y)

        s_x_array = np.append(s_x_array, s_x)
        s_y_array = np.append(s_y_array, s_y)

        t_array = np.append(t_array, t1 + t2)
        v_z_array = np.append(v_z_array, v_z)
        s_z_array = np.append(s_z_array, h1)
        # print(max(s_z_array), end=", ")

    s_z = h1
    v_t = np.sqrt((2 * m * g) / (roh * C_d * A_Para))
    print(v_t)
    print("up")

    while s_z > 0:
        
        '''While-Loop für den Gleitflug'''
        t2 += dt
        ''' Berechnung der Fallbeschleunigung'''
        a_z = -AccelerationWithDrag(g, m, D, v_z)
        '''Berechnung neuer Geschwindigkeiten'''
        v_x += a_x * dt
        v_y += a_y * dt
        v_z += a_z * dt

        s_x += v_x * dt
        s_y += v_y * dt
        s_z += v_z * dt

        v_x_array = np.append(v_x_array, v_x)
        v_y_array = np.append(v_y_array, v_y)
        v_z_array = np.append(v_z_array, v_z)

        s_x_array = np.append(s_x_array, s_x)
        s_y_array = np.append(s_y_array, s_y)
        s_z_array = np.append(s_z_array, s_z)

        t_array = np.append(t_array, t1 + t2)

    print("done")
    return t_array, v_x_array, v_y_array, v_z_array, s_x_array, s_y_array, s_z_array


t_values, v_x_values, v_y_values, v_z_values, s_x_values, s_y_values, s_z_values = VerticalFlight(v_z, g, WindSpeed,
                                                                                            Theta_deg, C_d)

'''erstellen des Grafes'''
x_array_length = len(s_x_values)
x_coordinate = s_x_values [x_array_length - 1]
y_array_length = len(s_y_values)
y_coordinate = s_y_values [y_array_length - 1]
print (x_coordinate)
print (y_coordinate)

r = np.sqrt((x_coordinate ** 2) + (y_coordinate ** 2))
rad_alpha = np.arctan(y_coordinate / x_coordinate)
deg_alpha = np.degrees(rad_alpha)

print (r)
print (deg_alpha)


#plt.plot(t_values, s_z_values)
plt.plot (s_x_values, s_y_values)
plt.show()