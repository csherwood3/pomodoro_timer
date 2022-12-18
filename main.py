import timer
from datetime import datetime
import entry_writer
import winsound
import os


def main(subject='algorithms'):
    """
    Main timer function. Tracks each pomodoro check and enters the checks into the database.

    :return: None
    """
    print('Checking local log directory...')
    if len(os.listdir("offline_logs/")) != 0:
        user_input = input('Local logs found. Append logs to database? (y/n)')

        if user_input.lower() == "y":
            print('Appending logs to database...\n')
            entry_writer.append_locals_to_db()
        else:
            print('Local logs not appended.\n')
    else:
        print('No local logs.\n')

    print('Starting pomodoro timer.')

    entries = []

    while True:

        minutes = input("Input timer minutes. Enter a non-integer minutes input to exit: ")

        try:
            minutes = int(minutes)

        # non-integer input. exit the program if this happens.
        except ValueError:
            print("Non-integer minutes input. Attempting to append logs to database...")
            break

        # set document details
        subject = input("Enter subject studying: ").lower() or subject
        notes = input("Enter notes (optional): ")

        # run the timer
        date = datetime.utcnow()

        time_period = timer.start_timer(minutes)
        winsound.PlaySound("chime.wav", winsound.SND_NODEFAULT)
        print("\n")

        # create a database entry if the minutes input are 25
        if minutes == 25:
            entry = {"date": date,
                     "start": time_period[0],
                     "end": time_period[1],
                     "subject": subject,
                     "notes": notes}
            entries.append(entry)

    # append all entries to the database
    if len(entries) > 0:
        entry_writer.write_entries_db(entries)
    else:
        print('No entries.')

    print('Ending Pomodoro timer.')


if __name__ == "__main__":
    main()
