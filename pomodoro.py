'''
Pomodoro CLI
'''

import time
import sys
from datetime import datetime, timedelta

start_time = datetime.now()

try:
    while True:
        # Calculate elapsed time
        elapsed_time = datetime.now() - start_time
        # Format the time for display (hours, minutes, seconds, milliseconds)
        # Use a timedelta to easily access components
        # Note: timedelta doesn't have a direct millisecond format, so we calculate it
        total_seconds = int(elapsed_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = int(elapsed_time.microseconds / 1000)

        # Format the string to display
        time_str = f"\r⏳ Work: {hours:02}:{minutes:02}:{seconds:02}"

        # Write the time string and flush the output immediately
        if (seconds == 3):
            sys.stdout.write("\nDONE!\n")
            break
        
        sys.stdout.write(time_str)
        sys.stdout.flush()
        time.sleep(0.01) # prevent high cpu usage
except KeyboardInterrupt:
    print("\nStopwatch stopped.")
