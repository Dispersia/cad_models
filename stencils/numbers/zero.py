from build123d import *
import math

sides = 75
thickness = 3

pts = [
    (-3,30), 
    (-18, 24),
    (-24, 15),
    (-28, 0),
    (-24, -15),
    (-18,-24),
    (-9, -28),
]

with BuildPart() as guide_1:
    with BuildSketch() as guide_sk:
        with BuildLine() as guide_ln:
            l1 = Bezier(*pts)
            offset(amount=2, side=Side.LEFT)
        make_face()
    extrude(amount=thickness)
    
    offset_amt = 2
    arrow_size = 7
    end = l1 @ 1
    tangent = (l1 % 1).normalized()
    left_normal = Vector(-tangent.Y, tangent.X)   
    angle = math.degrees(math.atan2(tangent.Y, tangent.X))
    base = end + left_normal * (offset_amt / 2)
    tip = base + tangent * arrow_size

    with BuildSketch() as direction:
        with Locations(Location((tip.X, tip.Y), angle)):
            ArrowHead(
                size=arrow_size,
                head_type=HeadType.STRAIGHT,
            )
    extrude(amount=thickness)

guide_2 = guide_1.part.rotate(Axis.Z,180)

with BuildPart() as zero:
    with BuildSketch() as outline:
        Rectangle(sides, sides)
    extrude(amount=thickness)
    
    top_face = zero.faces().filter_by(Axis.Z)[-1]
    face_plane = Plane(top_face)

    with BuildSketch() as n_sk:
        Text("0", font="KG Blank Space Solid", font_size=55, align=(Align.CENTER, Align.CENTER))
    extrude(amount=thickness, mode=Mode.SUBTRACT)

    with BuildSketch() as bridge:
        with Locations((0, 21)):
            Rectangle(width=5, height=25, align=(Align.CENTER, Align.CENTER))
    extrude(amount=thickness)
    
    with Locations(
        (0, 0, 1)
    ):
        add(guide_1, mode=Mode.SUBTRACT)

    with Locations(
        (0, 0, 1)
    ):
        add(guide_2, mode=Mode.SUBTRACT)

"""
def main():
    return {
            "n0": zero
    }
"""

export_stl(zero.part,"stl_files/zero.stl")
