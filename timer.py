from datetime import datetime
import time


def start_timer(minutes):
    """
    This method starts a timer. Counts down from a minutes input.

    :param: minutes
    :return: start_time, end_time
    """

    # initialize the timer amount in seconds * minutes
    seconds = 60 * int(minutes)

    start_time = datetime.utcnow().isoformat("T", "auto")

    while seconds > 0:
        time.sleep(1)
        seconds -= 1

    end_time = datetime.utcnow().isoformat("T", "auto")

    return start_time[11:23], end_time[11:23]


if __name__ == "__main__":
    print(start_timer(1))
