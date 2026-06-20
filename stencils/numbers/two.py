from build123d import *
import math

sides = 75
thickness = 3
guide_height = 1

pts = [
    (-20, 10),
    (-18, 18),
    (-10, 34),
    (0, 25),
    (10, 30),
    (18, 30),
    (20, 25),
    (25, 18),
    (20, 0),
    (13, -4),
    (11, -7),
        ]

wts = [
    1.0,
    1.8,
    1.5,
    1.5,
    1.5,
    1.0,
    1.0,
    1.5,
    1.5,
    2.0,
    1.5,
        ]

with BuildPart() as guide_1:
    with BuildSketch() as guide_sk:
        with BuildLine() as guide_ln:
            l1 = Bezier(*pts, weights= wts)
            offset(amount=2, side=Side.LEFT)
        make_face()
    extrude(amount=thickness)

with BuildPart() as two:
    Box (sides, sides, thickness)
    top_face = two.faces().filter_by(Axis.Z)[-1]

    with BuildSketch(top_face) as two_sk:
        Text("2", font="KG Blank Space Solid", font_size=55, align=(Align.CENTER, Align.CENTER))
    extrude(amount=-thickness, mode=Mode.SUBTRACT)

    with Locations(
            (0, 0, 1)
        ):
            add(guide_1, mode=Mode.SUBTRACT)

def main():
    return{
            "n2" : two
            } 
