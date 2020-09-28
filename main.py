import engine
import stage

# assumptions:
# factor of safety for tanks is 1.25

engine = engine.PreconfiguredEngine('engines\Merlin.ini')
stage_3 = stage.LiquidStage(engine, 3, 2.7*60, 3.66)

stage_3.mesh()
