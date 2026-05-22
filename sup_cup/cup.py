from build123d import *

diameter = 85
height = 115
bottom_hole_diameter = 51
bottom_hole_height = 25
wall = 4

hook_width = 10

with BuildPart() as cup_holder:
    with BuildSketch() as small_bottom:
        Circle(radius=diameter / 2 + wall * 2)
    extrude(amount=10)
    chamfer(cup_holder.edges().group_by(Axis.Z)[-1], length=9)
    with BuildSketch() as cup_holder_base:
        Circle(radius=diameter / 2)
    extrude(amount=height)
    with BuildSketch(Plane.XY.offset(bottom_hole_height + wall * 2)) as top_hole:
        Circle(radius=diameter / 2 - wall)
    extrude(amount=height, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(2)) as bottom_hole:
        Circle(radius=bottom_hole_diameter / 2)
    extrude(amount=bottom_hole_height - 2, mode=Mode.SUBTRACT)
    with BuildSketch() as ring_hole:
        Rectangle(33, 6)
    extrude(amount=10, mode=Mode.SUBTRACT)
    with BuildSketch() as hook_cut:
        with Locations((0, 38)):
            Rectangle(bottom_hole_height / 2 + 4.5, bottom_hole_height)
    extrude(amount=bottom_hole_height, mode=Mode.SUBTRACT)
    with BuildSketch() as bottom_drain_cut:
        with Locations((0, -35)):
            Rectangle(5, 30)
    extrude(amount=bottom_hole_height / 2, mode=Mode.SUBTRACT)
    with BuildSketch() as bottom_drain_cut:
        with Locations((38, 0), (-38, 0)):
            Rectangle(30, 5)
    extrude(amount=bottom_hole_height / 2, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(bottom_hole_height)) as drain_holes:
        with Locations((40, 0), (0, 40), (0, 0), (-40, 0), (0, -40)):
            Circle(radius=10)
    extrude(amount=20, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XZ.offset(-45)) as drain_hole_tops:
        with Locations((0, 42.5)):
            Circle(radius=9)
    extrude(amount=height, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.YZ.offset(-45)) as drain_hole_tops:
        with Locations((0, 42)):
            Circle(radius=9)
    extrude(amount=height, mode=Mode.SUBTRACT)

    #fillet(cup_holder.edges(), radius = 0.5)
    cup_holder.color = Color("steelblue")
"""
def main():
    return {
            "cup": cup_holder
            }
"""
export_stl(cup_holder.part, "cup.stl")
