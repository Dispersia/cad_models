from build123d import *

sides = 75
thickness = 3
guide_height = 1 

pts = [
    (-10, 24),
    (-13, 24),
    (-13,-20),
    (-10, -20),
    (-10, 24),
]

arrow_size = 7

with BuildPart() as one:
    Box( sides, sides, thickness )
    top_face = one.faces().filter_by(Axis.Z)[-1]

    with BuildSketch(top_face) as one_sk:
        Text("1", font="KG Blank Space Solid", font_size=55, align=(Align.CENTER, Align.CENTER))
    extrude(amount=-thickness, mode=Mode.SUBTRACT)

    with BuildSketch(top_face) as guide:
        with BuildLine() as guide_ln:
            Polyline(pts)
        make_face()
    extrude(amount=-guide_height, mode=Mode.SUBTRACT)
    
    with BuildSketch(top_face) as direction:
        with Locations((-11.5,-26)):
            ArrowHead( size=arrow_size, head_type=HeadType.STRAIGHT, rotation=270)
    extrude(amount=-guide_height, mode=Mode.SUBTRACT)

"""
def main():
    return {
            "n1": one
    }
"""

export_stl(one.part, "stl_files/one.stl")
