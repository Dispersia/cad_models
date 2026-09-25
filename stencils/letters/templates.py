from build123d import *

sides = 75
thickness = 2

bridges = {
    "A": [[
        (-.75,-25),
        (.75,-25),
        (.5,-8),
        (-.5,-8),
        ]],
    "a": [[
        (6,-6),
        (7.6, 0),
        (8.59, -19),
        (9, -28)
        ]]
        }

def letter(n):
    with BuildPart() as box:
        Box( sides, sides, thickness )
        top_face = box.faces().filter_by(Axis.Z)[-1]

        with BuildSketch(top_face):
            Text(n, font="KG Blank Space Solid", font_size=55, align=(Align.CENTER, Align.CENTER))
        extrude(amount=-thickness, mode=Mode.SUBTRACT)
        
        for pts in bridges.get(n, []):
            with BuildSketch(box.faces().filter_by(Axis.Z)[-1]):
                with BuildLine():
                    Polyline(*pts, close = True)
                make_face()
            extrude(amount=-thickness)

    return box
"""
def main():
    return {
            n: letter(n)
            for n in "a"

            }
"""
if __name__ == "__main__":
    export_stl(letter("a").part, "letter_a.stl")
