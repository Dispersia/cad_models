from build123d import *

side = 210
height = 50.8

with BuildPart() as box:
    Box (210, 210, 3)
    with BuildSketch() as walls:
        Polyline([
            (0,3),
            (side,3).
            (-side,3),
            (3,-side),
            (0,3),
        ])
        extrude(amount=height)

def main():
    return {
        "box": box
    }
