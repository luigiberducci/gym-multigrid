class Actions:
    available = [
        "still",
        "left",
        "right",
        "forward",
        "pickup",
        "drop",
        "toggle",
        "done",
    ]

    still = 0
    # Turn left, turn right, move forward
    left = 1
    right = 2
    forward = 3

    # Pick up an object
    pickup = 4
    # Drop an object
    drop = 5
    # Toggle/activate an object
    toggle = 6

    # Done completing task
    done = 7

class MediumActions:
    available = [
        "still",
        "left",
        "right",
        "forward",
        "pickup",
        "toggle",
    ]

    still = 0       # no action
    left = 1        # turn left
    right = 2       # turn right
    forward = 3     # move forward
    pickup = 4      # pick up an object
    toggle = 5      # toggle/activate an object


class SmallActions:
    available = ["still", "left", "right", "forward"]

    # Turn left, turn right, move forward
    still = 0
    left = 1
    right = 2
    forward = 3


class MineActions:
    available = ["still", "left", "right", "forward", "build"]

    still = 0
    left = 1
    right = 2
    forward = 3
    build = 4