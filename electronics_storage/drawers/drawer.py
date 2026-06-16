from build123d import *

with BuildPart() as handle:
    height = 15
    length = 20
    width = 50

    wall = 5

    with BuildSketch(Plane.XZ) as handle_sk:
        with BuildLine() as handle_line:
            l1 = Line((0, 0), (0, height))
            c1 = Bezier(l1 @ 1, (10, 10), (length, height - 5))
            l2 = Line(c1 @ 1, (length, height - 10))
            c2 = Bezier(l2 @ 1, (5, 5), (0, 0))
        make_face()
    extrude(amount=width)

    edges = handle.edges().group_by(Axis.X)[-1]

    fillet(edges, radius=1)

    with BuildSketch() as handle_cut:
        with Locations((10, -25)):
            Rectangle(length - wall, width - 10)
    extrude(amount=height, mode=Mode.SUBTRACT)


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

    with Locations((110, 25, 10)):
        add(handle)

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

with BuildPart() as roof:
    wall = 2.5
    length = 230

    with BuildSketch() as roof_sk:
        Rectangle(length, length)
    extrude(amount=wall)

    with Locations(
        (-100, -113, 0),
        (-100, 114.5, 0),
        (100, -113, 0),
        (100, 114.5, 0)
    ):
        add(fastener)

export_stl(cabinet.part, "cabinet.stl")
export_stl(drawer.part, "drawer.stl")
export_stl(roof.part, "roof.stl")
