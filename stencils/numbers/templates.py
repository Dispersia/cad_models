from build123d import *

sides = 75
thickness = 3

bridges = {
    "0": [[
        (-2, 14.5),
        (2, 14.5),
        (2, 27.5),
        (-2, 27.5)
    ]],

    "6": [[
        (-3.9, -9.5),
        (-6.5, 5), 
        (-8.962, 1.1),
        (-6.9, -10.2)
    ]],

    "8": [[
        (-2, -30),
        (2, -30),
        (2, -12),
        (-2, -12)
    ],
    [
        (-2, 30),
        (2, 30),
        (2, 12),
        (-2, 12)
        ]
          ],

    "9": [[
        (3.3, 9),
        (7.475, 4.8),
        (7.5905, 22.1),
        (3.3, 26)
    ]],
}

def number(n):
    with BuildPart() as box:
        Box( sides, sides, thickness )
        top_face = box.faces().filter_by(Axis.Z)[-1]

        with BuildSketch(top_face):
            Text(n, font="KG Blank Space Solid", font_size=55, align=(Align.CENTER, Align.CENTER))
        extrude(amount=-thickness, mode=Mode.SUBTRACT)
       
        for pts in bridges.get(n, []):
            with BuildSketch(top_face):
                with BuildLine():
                    Polyline(*pts, close=True)
                make_face()
            extrude(amount=-thickness)

    return box

def main():
    spacing = sides + 10
    cols = 5
    parts = {}
    for i in range(10):
        col, row = i % cols, i // cols
        loc = Location((col * spacing, -row * spacing, 0))
        parts[str(i)] = number(str(i)).part.moved(loc)
    return parts

if __name__ == "__main__":
    for i in range(10):
        export_stl(number(f"{i}").part, f"stl_files/{i}.stl")
