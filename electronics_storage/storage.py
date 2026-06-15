from build123d import *
from gridfinity_build123d import (
    BaseEqual,
    Bin,
    Compartment,
    CompartmentsEqual
)

with BuildPart() as storage:
    with BuildSketch() as storage_sk:
        Rectangle(5, 5)
    extrude(amount = 5)

def main():
    return {
        "storage": storage
    }
