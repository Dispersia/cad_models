from build123d import *

ribbon_width=25

with BuildPart() as base:
    with BuildSketch() as right:
        Circle(40)
    extrude(amount=2)
    with BuildSketch(Plane.XY.offset(2)) as center:
        Circle(25 / 2)
    extrude(amount=ribbon_width+1)
    with BuildSketch(Plane.XY.offset(28)) as connections:
        with PolarLocations(9, 5):
            Rectangle(3,3)
    extrude(amount=-8, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(28)) as topHole:
        Circle(6)
    extrude(amount=-28, mode=Mode.SUBTRACT)
    fillet(
        base.edges().filter_by(GeomType.CIRCLE), radius=.5
    )

with BuildPart() as top:
    with BuildSketch() as top_sk:
        Circle(40)
    extrude(amount=2)
    with BuildSketch() as connectors:
        with PolarLocations(9,5):
            Rectangle(2.95, 2.95)
    extrude(amount=7.8)
    with BuildSketch() as topHole:
        Circle(6)
    extrude(amount=2, mode=Mode.SUBTRACT)
    fillet(
        top.edges().filter_by(GeomType.CIRCLE), radius=.5
    )
""""
def main():
    return {
            "top": top
    }
"""
export_stl(base.part, "ribbonSpool_base.stl")
export_stl(top.part, "ribbonSpool_top.stl")

