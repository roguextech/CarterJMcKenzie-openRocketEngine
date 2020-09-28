import numpy as np
import math

def circle_area(diameter):
    return np.pi * diameter**2 / 4


def circle_diameter(area):
    return (4 * area / np.pi)**0.5


def volume_cone(d, h):
    return np.pi * (d/2)**2 * h / 3


def cylinder_volume(d, h):
    return np.pi * (d/2)**2 *h


def nozzle_volume(large_diam, small_diam, angle):
    if large_diam <= small_diam:
        print("input for nozzle volume wrong")
    r1 = large_diam/2
    r2 = small_diam/2
    h2 = np.tan(angle) * r2
    h1 =  np.tan(angle) * r1
    cone1 = volume_cone(r1*2, h1)
    cone2 = volume_cone(r2*2, h2)
    return cone1-cone2


def calculate_char_velocity(specific_heat, gas_const, burn_temp):
    char_velocity = (specific_heat * gas_const * burn_temp) ** (1 / 2) /\
             specific_heat * ((2 / (specific_heat + 1)) ** ((specific_heat + 1) / (specific_heat - 1)))
    return char_velocity


def deg2rad(degrees):
    return np.pi * degrees / 180

def calculate_mass_flow(thrust, c_star, CF):
    mass_flow = thrust / (c_star * CF)
    return mass_flow


def calculate_fuel_mass_flow(MR, mass_flow):
    fuel_mass_flow = mass_flow * 1/(MR + 1)
    return fuel_mass_flow


def calculate_oxidizer_mass_flow(MR, mass_flow):
    oxidizer_mass_flow = mass_flow * (1 - (1/(MR + 1)))
    return oxidizer_mass_flow


def calculate_propellant_mass(m_dot,t):
    return m_dot*t


def calculate_volume(density,mass):
    return mass/density


def calculate_specific_vol(p, R, t):
    specific_volume = R*t/p
    return specific_volume


def calculate_gas_tank_volume(propellant_volume, propellant_pressure, gas_pressure):
    return (propellant_volume * propellant_pressure) / (gas_pressure - propellant_pressure)


def calc_gas_mass(p_vol, p_p, R, gas_temp, gas_p_final, gas_p_init):
    return p_p*p_vol/(R*gas_temp) * (1/(1-gas_p_final/gas_p_init))


def calculate_gas_mass(gas_vol, gas_pres, gas_const, gas_temp):
    return (gas_pres) * gas_vol / (gas_const * gas_temp)


def calculate_tank_vol(specific_vol, mass):
    return specific_vol * mass


def calculate_tank_height(diameter, volume):
    ellipsoid_volume = 4/3 * diameter**2 /2
    height = (volume - ellipsoid_volume) / (math.pi * (diameter/2)**2)
    return height


def tank_thickness(pressure, diameter, tensile_strength, saftey_factor):
    thickness = (pressure*diameter) / (2*tensile_strength*saftey_factor)
    return thickness


def surface_area_ellipsoid(length,width,height):
    a = length/2
    b = width/2
    c = height/2
    SA = 4* math.pi * ((a**1.6 + b**1.6 + c**1.6)/3)**(1/1.6)
    return SA


def surface_area_tube(d, h):
    return np.pi * d * h


def mass_tank_half_ellipse(density, thickness, diameter, height):
    sa1 = surface_area_ellipsoid(diameter, diameter, diameter/2)
    sa2 = np.pi * diameter * height
    mass = density * thickness * (sa1 + sa2)
    return mass

# if __name__ == "__main__":