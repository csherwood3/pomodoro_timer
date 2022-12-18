from datetime import datetime
from datetime import timedelta


def start_timer(minutes):
    """
    This method starts a timer. Counts down from a minutes input. Displays time in MM:SS format.

    :param: minutes
    :return: start_time, end_time
    """

    print("\nTime Remaining:")
    start_time = datetime.utcnow()
    end_time = start_time + timedelta(minutes=minutes)

    while datetime.utcnow() < end_time:
        print(str(end_time - datetime.utcnow())[2:7], end="\r")

    end_time = datetime.utcnow().isoformat("T", "auto")

    return start_time.isoformat("T", "auto")[11:19], end_time[11:19]


if __name__ == "__main__":
    print(start_timer(25))
