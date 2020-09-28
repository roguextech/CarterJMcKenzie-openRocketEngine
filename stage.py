from rocketcea.cea_obj_w_units import CEA_Obj
import gmsh
import build
import equations as eq


class LiquidStage:
    def __init__(self, engine, engine_quantity, burn_time, stage_diameter):

        # import engine information
        self.stage_diameter = stage_diameter
        self.engine = engine
        self.engine_quantity = engine_quantity
        self.burn_time = burn_time
        self.total_thrust = engine.engine_thrust * engine_quantity
        self.oxidizer = engine.oxidizer
        self.fuel = engine.fuel
        self.mix_ratio = engine.mix_ratio
        self.chamber_pressure = engine.chamber_pressure
        self.expansion_ratio = engine.expansion_ratio
        self.exit_diameter = engine.exit_diameter
        self.throat_diameter = engine.throat_diameter
        # self.nozzle_length = engine.nozzle_length
        self.chamber_diameter = engine.chamber_diameter
        self.nozzle_convergence_length = engine.nozzle_convergence_length
        self.nozzle_divergence_length = engine.nozzle_divergence_length
        self.chamber_length = engine.chamber_length

        # calculate propellant properties
        propellant = CEA_Obj(fuelName=self.fuel, oxName=self.oxidizer, pressure_units='Pa', cstar_units='m/s')
        self.c_star = propellant.get_Cstar(self.chamber_pressure, self.mix_ratio)
        self.CFcea, self.CFamb, self.mode = propellant.get_PambCf(Pamb=101352.932, Pc=self.chamber_pressure, MR=self.mix_ratio, eps=self.expansion_ratio)
        self.isp = propellant.estimate_Ambient_Isp(Pc=self.chamber_pressure, MR=self.mix_ratio, eps=self.expansion_ratio)

        # calculate mass flow properties
        mass_flow = eq.calculate_mass_flow(self.total_thrust, self.c_star, self.CFcea)
        propellant_mass = mass_flow * self.burn_time
        self.fuel_mass = propellant_mass / (self.mix_ratio + 1)
        self.oxidizer_mass = propellant_mass * (1 - 1 / (1 + self.mix_ratio))

        # calculate tank properties
        LOX_density = 976.3 # kg/m**3
        LOX_density = 1200  # kg/m**3
        RP1_density = 810.0 # kg/m**3

        oxidizer_tank_vol = eq.calculate_tank_vol(1/LOX_density, self.oxidizer_mass)
        fuel_tank_vol = eq.calculate_tank_vol(1/RP1_density, self.fuel_mass)
        self.oxidizer_tank_height = eq.calculate_tank_height(self.stage_diameter, oxidizer_tank_vol)
        self.fuel_tank_height = eq.calculate_tank_height(self.stage_diameter, fuel_tank_vol)

        MPa = 10**6
        tank_pressure = 3 * MPa
        tensile_strength = 530 * MPa
        safety_factor = 1.25
        AlLi_alloy_density = 2590  # kg/m^3
        tank_thickness = eq.tank_thickness(tank_pressure, stage_diameter, tensile_strength, safety_factor)
        self.fuel_tank_mass = eq.mass_tank_half_ellipse(AlLi_alloy_density, tank_thickness, self.stage_diameter,
                                              self.fuel_tank_height)

        tank_pressure = 3 * MPa
        self.oxidizer_tank_mass = eq.mass_tank_half_ellipse(AlLi_alloy_density, tank_thickness, self.stage_diameter,
                                              self.oxidizer_tank_height)
        print(f"Fuel mass: {self.fuel_mass}")
        print(f"Oxidizer mass: {self.oxidizer_mass}")
        print(f"Fuel tank mass: {self.fuel_tank_mass}")
        print(f"Oxidizer tank mass: {self.oxidizer_tank_mass}")





    def mesh(self):
        gmsh.initialize()
        # gmsh.option.setNumber("General.Terminal", 1)

        # gmsh.logger.start()

        gmsh.model.add("Stage1")

        build.engines(self.chamber_length, self.nozzle_convergence_length, self.nozzle_divergence_length,
                      self.chamber_diameter, self.throat_diameter, self.exit_diameter, self.engine_quantity,
                      self.stage_diameter)

        build.oxidizer_tank(self.oxidizer_tank_height, self.stage_diameter)

        build.fuel_tank(self.fuel_tank_height,self.oxidizer_tank_height,self.stage_diameter)

        gmsh.model.occ.synchronize()
        gmsh.model.mesh.generate(3)

        # gmsh.write("Practice.msh")
        # log = gmsh.logger.get()
        # print("Logger has recorded " + str(len(log)) + " lines")
        # gmsh.logger.stop()

        gmsh.fltk.run()
        gmsh.finalize()



# if __name__ == "__main__":