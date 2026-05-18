from build123d import Box, Color

def main():
    box = Box(50, 50, 50)
    box.color = Color("steelblue")

    return {
        "Box": box,
    }
