#!/usr/bin/python3
from courses import Courses
from dmenu import dmenu
from utils import generate_short_title, MAX_LEN
from pynput import keyboard

lectures = Courses().current.lectures
listener = None  # Initialize the listener variable

def on_press(key):
    global listener
    try:
        if key.char == '|': # here i have used pipe because that is hopefully not used in a filename
            new_lecture = lectures.new_lecture()
            new_lecture.edit()
            listener.stop()  # Stop the listener after an action
    except AttributeError:
        pass

# Set up the listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

sorted_lectures = sorted(lectures, key=lambda l: -l.number)

options = [
    "{number: >2}. {title: <{fill}} {date}  ({week})".format(
        fill=MAX_LEN,
        number=lecture.number,
        title=generate_short_title(lecture.title),
        date=lecture.date.strftime('%a %d %b'),
        week=lecture.week
    )
    for lecture in sorted_lectures
]

key, index, selected = dmenu('Select lecture', options, [ '-l', 5, ])

# Stop the listener after an action
listener.stop()

if key == 0:
    sorted_lectures[index].edit()
elif key == 1:
    new_lecture = lectures.new_lecture()
    new_lecture.edit()

