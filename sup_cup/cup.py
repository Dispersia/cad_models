from build123d import *

diameter = 85
height = 115
bottom_hole_diameter = 51
bottom_hole_height = 25
wall = 4

hook_width = 10

with BuildPart() as cup_holder:
    with BuildSketch() as small_bottom:
        Circle(radius=diameter / 2 + wall)
    extrude(amount=5)
    chamfer(cup_holder.edges().group_by(Axis.Z)[-1], length=4)
    with BuildSketch() as cup_holder_base:
        Circle(radius=diameter / 2)
    extrude(amount=height)
    with BuildSketch(Plane.XY.offset(bottom_hole_height + wall * 2)) as top_hole:
        Circle(radius=diameter / 2 - wall)
    extrude(amount=height, mode=Mode.SUBTRACT)
    fillet(cup_holder.edges().group_by(Axis.Z)[-1], 0.5)
    with BuildSketch() as bottom_hole:
        Circle(radius=bottom_hole_diameter / 2)
    extrude(amount=bottom_hole_height, mode=Mode.SUBTRACT)
    with BuildSketch() as hook_cut:
        with Locations((0, 35, 0)):
            Rectangle(bottom_hole_height/ 2, bottom_hole_height)
    extrude(amount=bottom_hole_height, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XZ.offset(-20)) as hook:
        with BuildLine() as line:
            l1 = Line((-hook_width / 2, bottom_hole_height), (hook_width / 2, 2))
            l2 = Line((hook_width / 2, bottom_hole_height), (hook_width / 2, 2))
            #l3 = ThreePointArc((hook_width / 2, hook_width / 2), (hook_width / 2, hook_width / 2 * 1.5), (0.0, hook_width / 2))
            #l4 = Line((0.0, hook_width / 2), (0, 0))
        make_face()
    extrude(amount = wall * 2)


def main():
    return {
        "cup_holder": cup_holder,
    }
