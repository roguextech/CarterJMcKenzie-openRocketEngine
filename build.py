import gmsh
import math


def nozzle(x, y, chamber_length, nozzle_convergence_length, nozzle_divergence_length, chamber_diameter, throat_diameter,
           exit_diameter):
    gmsh.model.occ.addCone(x, y, chamber_length, 0, 0, nozzle_convergence_length, chamber_diameter / 2,
                           throat_diameter / 2)
    gmsh.model.occ.addCone(x, y, chamber_length + nozzle_convergence_length, 0, 0, nozzle_divergence_length,
                           throat_diameter / 2, exit_diameter / 2)


def combustion_chamber(x, y, chamber_length, chamber_diameter):
    gmsh.model.occ.addCylinder(x, y, 0, 0, 0, chamber_length, chamber_diameter/2)


def engines(chamber_length, nozzle_convergence_length, nozzle_divergence_length, chamber_diameter, throat_diameter,
           exit_diameter, engine_count, stage_diameter):

    x,y = place_engine(stage_diameter,exit_diameter,engine_count)

    for i in range(0, engine_count):
        nozzle(x[i], y[i], chamber_length, nozzle_convergence_length, nozzle_divergence_length, chamber_diameter,
               throat_diameter, exit_diameter)
        combustion_chamber(x[i], y[i], chamber_length, chamber_diameter)


def oxidizer_tank(tank_height, tank_diameter):
    gmsh.model.occ.addCylinder(0, 0, -tank_height, 0, 0, tank_height, tank_diameter/2)


def fuel_tank(fuel_tank_height, ox_tank_height, tank_diameter):
    gmsh.model.occ.addCylinder(0, 0, -fuel_tank_height -ox_tank_height, 0, 0, fuel_tank_height, tank_diameter/2)


def place_engine(stage_diameter, engine_diameter, engine_count):
    """returns list of x, y coordinates for engines"""
    x = [0]
    y = [0]

    if engine_count == 2:
        x = [0,0]
        y = [-stage_diameter/4, stage_diameter/4]

    if engine_count == 3:
        x = [-engine_diameter/2, 0, engine_diameter/2]
        y = [-engine_diameter/2, engine_diameter/2, -engine_diameter/2]

    if engine_count == 4:
        x = [-engine_diameter/2, -engine_diameter/2,  engine_diameter/2, engine_diameter/2]
        y = [-engine_diameter/2,  engine_diameter/2, -engine_diameter/2, engine_diameter/2]

    if engine_count == 5:
        for i in range(0, engine_count):
            X = engine_diameter * 1.5 * math.cos(math.pi * 2 / (engine_count-1) * i)
            Y = engine_diameter * 1.5 * math.sin(math.pi * 2 / (engine_count-1) * i)
            y.append(Y)
            x.append(X)

    if engine_count == 6:
        for i in range(0, engine_count):
            X = engine_diameter * 1.5 * math.cos(math.pi * 2 / (engine_count-1) * i)
            Y = engine_diameter * 1.5 * math.sin(math.pi * 2 / (engine_count-1) * i)
            y.append(Y)
            x.append(X)

    if engine_count == 7:
        for i in range(0, engine_count):
            X = engine_diameter * 1.5 *math.cos(math.pi*2/ (engine_count-1) * i)
            Y = engine_diameter * 1.5 *math.sin(math.pi*2/ (engine_count-1) * i)
            y.append(Y)
            x.append(X)

    if engine_count == 8:
        for i in range(0, engine_count):
            X = engine_diameter * 1.5 *math.cos(math.pi*2/ (engine_count-1) * i)
            Y = engine_diameter * 1.5 *math.sin(math.pi*2/ (engine_count-1) * i)
            y.append(Y)
            x.append(X)

    if engine_count == 9:
        for i in range(0, engine_count):
            X = engine_diameter * 1.5 *math.cos(math.pi*2/ (engine_count-1) * i)
            Y = engine_diameter * 1.5 *math.sin(math.pi*2/ (engine_count-1) * i)
            y.append(Y)
            x.append(X)

    return x, y


# if __name__ == '__main__':

