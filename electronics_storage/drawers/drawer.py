from build123d import *

with BuildPart() as handle:
    height = 10

    with BuildSketch() as handle_sk:
        Rectangle(5, 5)
    extrude(amount=5)

with BuildPart() as drawer:
    height = 35
    length = 220
    wall = 2.5

    with BuildSketch() as drawer_sk:
        Rectangle(length, length)
    extrude(amount=height)

    edges = drawer.edges().filter_by(Axis.Z)

    fillet(edges, radius=5)

    top_face = drawer.faces().sort_by(Axis.Z)[-1]
    offset(amount=-wall, openings=top_face)

with BuildPart() as fastener:
    height = 1.5
    length = 5
    inset = 1.5
    wall = 1.5

    with BuildSketch(Plane.XZ) as fastener_sk:
        with BuildLine() as fastener_line:
            Polyline(
                (0, 0),
                (inset, -height),
                (length - inset, -height),
                (length, 0),
                (0, 0)
            )
        make_face()
    extrude(amount=wall)

with BuildPart() as cabinet:
    height = 50
    length = 230
    wall = 2.5

    with BuildSketch() as cabinet_sk:
        Rectangle(length, length)
    extrude(amount=height)
    top_face = cabinet.faces().sort_by(Axis.Z)[-1]
    front_face = cabinet.faces().sort_by(Axis.X)[-1]

    offset(amount=-wall, openings=[top_face, front_face])

    edges = cabinet.edges().filter_by(Axis.Z)

    fillet(edges, radius=1)

    with Locations(
        (-100, -113, 50),
        (-100, 114.5, 50),
        (100, -113, 50),
        (100, 114.5, 50)
    ):
        add(fastener, mode=Mode.SUBTRACT)

    with Locations(
        (-100, -113, 0),
        (-100, 114.5, 0),
        (100, -113, 0),
        (100, 114.5, 0)
    ):
        add(fastener)

def main():
    return {
        "drawer": handle 
    }
