import timer
from datetime import datetime
import entry_writer
import winsound


def main(subject='algorithms'):
    """
    Main timer function. Tracks each pomodoro check and enters the checks into the database.

    :return: None
    """
    print('Starting pomodoro timer.')

    entries = []

    while True:

        minutes = input("Input timer minutes. Enter a non-integer minutes input to exit: ")

        try:
            minutes = int(minutes)

        # non-integer input. exit the program if this happens.
        except ValueError:
            print("Non-integer minutes input. Ending program.")
            break

        # set document details
        subject = input("Enter subject studying: ").lower() or subject
        notes = input("Enter notes (optional): ")

        # run the timer
        date = datetime.utcnow()
        period = timer.start_timer(minutes)
        winsound.PlaySound("chime.wav", winsound.SND_NODEFAULT)

        # create a database entry if the minutes input are 25
        if minutes == 25:
            entry = {"date": date,
                     "start": period[0],
                     "end": period[1],
                     "subject": subject,
                     "notes": notes}
            entries.append(entry)

    # append all entries to the database
    print('Appending entries to database.')
    entry_writer.write_entries_db(entries)


if __name__ == "__main__":
    main()
