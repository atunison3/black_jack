from domain import Dealer


class NoActionError(Exception):
    pass


class NoStateError(Exception):
    pass


def decide_player_action(state: str, dealer: Dealer, count: int = 0) -> str:
    """Decides what action to take"""

    count = count > 0
    dv = dealer.upcard

    # Cover the basics
    if state == "7":
        return "H"
    elif state == "17":
        return "S"
    elif state == "8":
        return "H"
    elif state == "12":
        if dv in [2, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [3, 4, 5, 6] and count:
            return "S"
        elif dv in [3, 4, 5, 6] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "13":
        if dv in [7, 8, 9, 10, 11]:
            return "H"
        elif dv in [5, 6]:
            return "S"
        elif dv in [2, 3, 4] and count:
            return "S"
        elif dv in [2, 3, 4] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "14":
        if dv in [7, 8, 9, 10, 11]:
            return "H"
        elif dv in [3, 4, 5, 6]:
            return "S"
        elif dv in [2] and count:
            return "S"
        elif dv in [2] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "15":
        if dv in [7, 8, 9, 10, 11]:
            return "H"
        elif dv in [2, 3, 4, 5, 6]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "16":
        if dv in [7, 8, 9, 11]:
            return "H"
        elif dv in [10] and count:
            return "S"
        elif dv in [10] and not count:
            return "H"
        elif [2, 3, 4, 5, 6]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A7":
        if dv in [11] and count:
            return "S"
        elif dv in [11] and not count:
            return "H"
        elif dv in [9, 10]:
            return "H"
        elif dv in [7, 8]:
            return "S"
        elif dv in [4, 5, 6]:
            return "D"
        elif dv in [2, 3] and count:
            return "D"
        elif dv in [2, 3] and not count:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")

    ## Splits and Pairs
    elif state == "AA":
        return "P"
    elif state == "22":
        if dv in [2, 8, 9, 10, 11]:
            return "H"
        elif dv in [5, 6, 7]:
            return "P"
        elif dv in [3, 4] and count:
            return "P"
        elif dv in [3, 4] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "33":
        if dv in [2, 3, 8, 9, 10, 11]:
            return "H"
        elif dv in [4, 5, 6, 7]:
            return "P"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "66":
        if dv in [7, 8, 9, 10, 11]:
            return "H"
        elif dv in [5, 6]:
            return "P"
        elif dv in [2, 3, 4] and count:
            return "P"
        elif dv in [2, 3, 4] and (not count):
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "77":
        if dv in [8, 9, 11]:
            return "H"
        elif dv == 10 and count:
            return "S"
        elif dv == 10 and not count:
            return "H"
        elif dv in [2, 3, 4, 5, 6, 7]:
            return "P"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "88":
        return "P"
    elif state == "99":
        if dv in [7, 10, 11]:
            return "S"
        elif dv in [4, 5, 6, 8, 9]:
            return "P"
        elif dv in [2, 3] and count:
            return "P"
        elif dv in [2, 3] and not count:
            return "S"

    ## Double Downs
    elif state == "62":
        return "H"
    elif state == "53":
        if dv in [2, 3, 4, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [5, 6] and count:
            return "D"
        elif dv in [5, 6] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "44":
        if dv in [2, 3, 4, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [5, 6] and count:
            return "D"
        elif dv in [5, 6] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "9":
        if dv in [7, 8, 9, 10, 11]:
            return "H"
        elif dv in [5, 6]:
            return "D"
        elif dv in [2, 3, 4] and count:
            return "D"
        elif dv in [2, 3, 4] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "10":
        if dv in [10, 11]:
            return "H"
        elif dv in [8, 9] and count:
            return "D"
        elif dv in [8, 9] and not count:
            return "H"
        elif dv in [2, 3, 4, 5, 6, 7]:
            return "D"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "11":
        if dv in [10, 11] and count:
            return "D"
        elif dv in [10, 11] and not count:
            return "H"
        elif dv in [2, 3, 4, 5, 6, 7, 8, 9]:
            return "D"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A2":
        if dv in [2, 3, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [6]:
            return "D"
        elif dv in [4, 5] and count:
            return "D"
        elif dv in [4, 5] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A3":
        if dv in [2, 3, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [5, 6]:
            return "D"
        elif dv in [4] and count:
            return "D"
        elif dv in [4] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A4":
        if dv in [2, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [5, 6]:
            return "D"
        elif dv in [3, 4] and count:
            return "D"
        elif dv in [3, 4] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A5":
        if dv in [2, 3, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [5, 6]:
            return "D"
        elif dv in [4] and count:
            return "D"
        elif dv in [4] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A6":
        if dv in [7, 8, 9, 10, 11]:
            return "H"
        elif dv in [3, 4, 5, 6]:
            return "D"
        elif dv in [2] and count:
            return "D"
        elif dv in [2] and not count:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A8":
        if dv in [2, 3, 7, 8, 9, 10, 11]:
            return "S"
        elif dv in [4, 5, 6] and count:
            return "D"
        elif dv in [4, 5, 6] and not count:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    else:
        raise NoActionError(f"No action for {state} - {dv} - {count}")


def decide_player_action1(state: str, dealer: Dealer, count: int = 0) -> str:
    """Decides what action to take"""

    count = count > 0
    dv = dealer.upcard

    # Cover the basics
    if state == "8-3":
        return "H"
    elif state == "9":
        if dv in [2, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [3, 4, 5, 6]:
            return "D"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "10":
        if dv in [2, 3, 4, 5, 6, 7, 8, 9]:
            return "D"
        elif dv in [10, 11]:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "11":
        if dv in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            return "D"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "12":
        if dv in [2, 3, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [4, 5, 6]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "13":
        if dv in [7, 8, 9, 10, 11]:
            return "H"
        elif dv in [2, 3, 4, 5, 6]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "14":
        if dv in [7, 8, 9, 10, 11]:
            return "H"
        elif dv in [2, 3, 4, 5, 6]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "15":
        if dv in [7, 8, 9, 10, 11]:
            return "H"
        elif dv in [2, 3, 4, 5, 6]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "16":
        if dv in [7, 8, 9, 10, 11]:
            return "H"
        elif dv in [2, 3, 4, 5, 6]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A-2":
        if dv in [2, 3, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [4, 5, 6]:
            return "D"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A-3":
        if dv in [2, 3, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [4, 5, 6]:
            return "D"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A-4":
        if dv in [2, 3, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [4, 5, 6]:
            return "D"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A-5":
        if dv in [2, 3, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [4, 5, 6]:
            return "D"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A-6":
        if dv in [2, 3, 7, 8, 9, 10, 11]:
            return "H"
        elif dv in [4, 5, 6]:
            return "D"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A-7":
        if dv in [2, 7, 8]:
            return "S"
        elif dv in [3, 4, 5, 6]:
            return "D"
        elif dv in [9, 10, 11]:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A-8":
        if dv in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "A-9":
        if dv in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "2-2":
        if dv in [2, 3, 8, 9, 10, 11]:
            return "H"
        elif dv in [4, 5, 6, 7]:
            return "P"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "3-3":
        if dv in [2, 3, 8, 9, 10, 11]:
            return "H"
        elif dv in [4, 5, 6, 7]:
            return "P"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "4-4":
        if dv in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "5-5":
        if dv in [2, 3, 4, 5, 6, 7, 8, 9]:
            return "D"
        if dv in [10, 11]:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "6-6":
        if dv in [2, 3, 4, 5, 6]:
            return "P"
        elif dv in [7, 8, 9, 10, 11]:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "7-7":
        if dv in [2, 3, 4, 5, 6]:
            return "P"
        elif dv in [7, 8, 9, 10, 11]:
            return "H"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "8-8":
        if dv in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            return "SP"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "9-9":
        if dv in [2, 3, 4, 5, 6, 8, 9]:
            return "P"
        elif dv in [7, 10, 11]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "10-10":
        if dv in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            return "S"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
    elif state == "11-11":
        if dv in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            return "P"
        raise NoActionError(f"No action for {state} - {dv} - {count}")
