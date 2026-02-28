import time, sys
from datetime import datetime, timedelta

start_time = datetime.now()

default_work = 10
default_break = 5

def pomo_start():
    while True:
        # calculate elapsed time
        elapsed_time = datetime.now() - start_time
        # format the time for display (hours, minutes, seconds, milliseconds)
        # use a timedelta to easily access components
        # note: timedelta doesn't have a direct millisecond format, so we calculate it
        total_seconds = int(elapsed_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = int(elapsed_time.microseconds / 1000)

        # format the string to display
        time_str = f"\r⏳ Work: {minutes:02}:{seconds:02}"

        # write the time string and flush the output immediately
        if (total_seconds == default_work):
            sys.stdout.write("\nDONE!\n")
            return

        sys.stdout.write(time_str)
        sys.stdout.flush()
        time.sleep(0.01) # prevent high cpu usage