from datetime import datetime
from pathlib import Path

def get_week(d=datetime.today()):
    return (int(d.strftime("%W")) + 52 - 5) % 52

USERCALENDARID = 'primary'
CURRENT_COURSE_SYMLINK = Path('/home/daniel/current_course/').expanduser()
CURRENT_COURSE_ROOT = CURRENT_COURSE_SYMLINK.resolve()
CURRENT_COURSE_WATCH_FILE = Path('/tmp/current_course/').resolve()
ROOT = Path('/home/daniel/notes/').expanduser()
DATE_FORMAT = '%d-%m-%Y'
