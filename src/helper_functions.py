import re

RESET = "\033[0m"
BLACK_TEXT = "\033[30m"

RED_BG = "\033[41m"
YELLOW_BG = "\033[43m"
BLUE_BG = "\033[44m"
WHITE_BG = "\033[47m"
GREEN_BG = "\033[42m"

BACKGROUND_COLORS = {
    "H": "\033[41m",  # red
    "D": "\033[44m",  # blue
    "S": "\033[43m",  # yellow
    "P": "\033[42m",  # green
}


def format_suits(colorized: str) -> str:
    """Convert colorized suit text into a background-colored display."""
    suits = re.findall(r"([HDSP])", colorized)

    if len(suits) != 2:
        raise ValueError("Expected exactly two suits")

    left, right = suits

    if left == right:
        bg = BACKGROUND_COLORS[left]
        text = f"  {left}  "
    else:
        bg = WHITE_BG
        text = f" {left} {right} "

    return f"{bg}{BLACK_TEXT}{text}{RESET}"


def format_cell(value: str) -> str:
    """Return a formatted cell with ANSI background colors."""

    backgrounds = {
        "S S": YELLOW_BG,
        "H H": RED_BG,
        "D D": BLUE_BG,
        "P P": GREEN_BG,
    }

    if value == "|":
        return f"{WHITE_BG}{BLACK_TEXT}|{RESET}"

    if value in backgrounds:
        bg = backgrounds[value]
        text = f"  {value[0]}  "
    elif value in {"S H", "D S", "D H"}:
        bg = WHITE_BG
        text = f" {value} "
    else:
        bg = WHITE_BG
        text = f"{value:^5}"

    return f"{bg}{BLACK_TEXT}{text}{RESET}"
