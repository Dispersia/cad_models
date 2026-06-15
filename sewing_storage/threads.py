from build123d import *

with BuildPart() as box:
    with BuildSketch() as box_sk:
        Rectangle(4, 10)
    extrude(amount=2)

def main():
    return {
        "box": box
    }
