from build123d import *

desk_height = 40
desk_width = 65
bag_hook_height = desk_height + 70
bag_hook_angle = 15
hook_stop = 30
thickness = 10


with BuildPart() as hook:
    with BuildSketch() as hook_sk:
        with BuildLine() as hook_line:
            Polyline([
                (0,0),
                (0, desk_width),
                (-desk_height, desk_width),
                (-desk_height, 0),
            ])
            offset(amount=thickness, side=Side.LEFT)
        make_face()
        with BuildLine() as hook_hook:
            FilletPolyline (
                (-desk_height, 0),
                (-bag_hook_height, 0),
                (-bag_hook_height, desk_width),
                radius=bag_hook_angle
            )
            offset(amount = thickness, side=Side.RIGHT)
        make_face()
        with BuildLine() as hook_end:
            Polyline([
                (-bag_hook_height + thickness, desk_width),
                (-bag_hook_height + hook_stop, desk_width),
            ])
            offset(amount=thickness, side=Side.RIGHT)
        make_face()
    extrude(amount=25)
    fillet(hook.edges(), radius=1.5)

"""
def main():
    return {
        "hook": hook
    }
"""

export_stl(hook.part, "hook.stl")
