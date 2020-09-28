import molmass
import math
from rocketcea.cea_obj_w_units import CEA_Obj
import configparser
import gmsh
import build
import equations as eq


class PreconfiguredEngine:

    def __init__(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)
        self.oxidizer = config['propellant']['oxidizer']
        self.fuel = config['propellant']['fuel']
        self.mix_ratio = float(config['propellant']['ratio'])
        self.engine_thrust = float(config['performance']['thrust'])
        self.chamber_pressure = float(config['chamber']['pressure'])
        self.expansion_ratio = float(config['nozzle']['ratio'])
        self.exit_diameter = float(config['nozzle']['exit'])


        # calculate nozzle characteristics (15 deg conic)
        Kn = 5
        divergence_angle = eq.deg2rad(15)  # deg
        convergence_angle = eq.deg2rad(60)  # deg

        exit_area = eq.circle_area(self.exit_diameter)
        throat_area = exit_area / self.expansion_ratio
        chamber_area = Kn * throat_area
        self.throat_diameter = eq.circle_diameter(throat_area)
        self.chamber_diameter = eq.circle_diameter(chamber_area)
        self.nozzle_divergence_length = ((self.exit_diameter - self.throat_diameter) / 2) * math.tan(
            math.pi / 2 - divergence_angle)
        self.nozzle_convergence_length = ((self.chamber_diameter - self.throat_diameter) / 2) * math.tan(
            math.pi / 2 - convergence_angle)
        self.chamber_length = self.chamber_diameter*2


class CustomEngine:

    def __init__(self, oxidizer, fuel, mix_ratio, engine_thrust, chamber_pressure, expansion_ratio, exit_diameter):
        # intialize_values
        self.oxidizer = oxidizer
        self.fuel = fuel
        self.mix_ratio = mix_ratio
        self.engine_thrust = engine_thrust
        self.chamber_pressure = chamber_pressure
        self.expansion_ratio = expansion_ratio
        self.exit_diameter = exit_diameter

        # calculate nozzle characteristics (15 deg conic)
        Kn = 5
        divergence_angle = eq.deg2rad(15)  # deg
        convergence_angle = eq.deg2rad(60)  # deg

        exit_area = eq.circle_area(self.exit_diameter)
        throat_area = exit_area / self.expansion_ratio
        chamber_area = Kn * throat_area
        self.throat_diameter = eq.circle_diameter(throat_area)
        self.chamber_diameter = eq.circle_diameter(chamber_area)
        self.nozzle_divergence_length = ((self.exit_diameter - self.throat_diameter) / 2) * math.tan(
            math.pi / 2 - divergence_angle)
        self.nozzle_convergence_length = ((self.chamber_diameter - self.throat_diameter) / 2) * math.tan(
            math.pi / 2 - convergence_angle)
        self.chamber_length = self.chamber_diameter*2


# if __name__ == "__main__":