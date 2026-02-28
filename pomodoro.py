'''
Pomodoro CLI
'''

from datetime import datetime, timedelta
from utils import pomo_start, parser

try:
    while True:
       usr_input = input("")
       parser(usr_input)
except KeyboardInterrupt:
    print("\nStopwatch stopped.")
