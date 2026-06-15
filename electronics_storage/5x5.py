from build123d import *
from gridfinity_build123d import (
    BaseEqual,
    BasePlateEqual,
    Bin,
    Compartment,
    BaseEqual,
    CompartmentsEqual,
)

plate = BasePlateEqual(
    size_x=5,
    size_y=5
)

bin = Bin(
    BaseEqual(grid_x=1, grid_y=2),
    height_in_units=4,
    compartments=CompartmentsEqual(compartment_list=[Compartment()])
)

"""
def main():
    return {
        "part1": plate,
        "bin": bin
    }
"""

#export_stl(plate, "5x5.stl")
export_stl(bin, "bin.stl")
