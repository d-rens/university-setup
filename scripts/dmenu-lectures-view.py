#!/usr/bin/python3
import subprocess
from courses import Courses
from dmenu import dmenu

lectures = Courses().current.lectures

commands = ['last', 'prev-last', 'all', 'prev']
options = ['current lecture', 'last two lectures', 'all lectures', 'previous lectures']

key, index, selected = dmenu('Select view', options, [
    '-l', 4,
])

if index >= 0:
    command = commands[index]
else:
    command = selected

lecture_range = lectures.parse_range_string(command)
lectures.update_lectures_in_master(lecture_range)
lectures.compile_master()

# Check if master.pdf is already open
pdf_viewer_process = subprocess.run(["pgrep", "-f", "master.pdf"], stdout=subprocess.PIPE)

if pdf_viewer_process.returncode != 0:
    # Open master.pdf with your preferred PDF viewer
    subprocess.run(["zathura ~/current_course/master.pdf"], shell=True)

