from build123d import *
import math

sides = 75
thickness = 5
curve = 30

with BuildPart() as n:
    with BuildSketch() as outline:
        Rectangle(sides, sides)
    extrude(amount=thickness)
    
    top_face = n.faces().filter_by(Axis.Z)[-1]
    face_plane = Plane(top_face)

    with BuildSketch() as n_sk:
        Text("0", font="Noto Serif", font_size=60, align=(Align.CENTER, Align.CENTER))
    extrude(amount=thickness, mode=Mode.SUBTRACT)

    with BuildSketch() as bridge:
        with Locations((0, 20)):
            Rectangle(width=thickness, height=thickness, align=(Align.CENTER, Align.CENTER))
    extrude(amount=thickness)
    
pts = [
    (-5, 27),
    (-22, 15),
    (-30, 0),
    (-22, -15),
    (-5, -27),
]

wts = [
    3.0,
    1.0,
    .25,
    1.0,
    3.0
]

with BuildPart() as guide:
    with BuildSketch() as guide_sk:
        with BuildLine() as guide_ln:
            l1 = Bezier(*pts, weights=wts)
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
def main():
    return {
            "n0": guide
    }
