#!/usr/bin/python3
from courses import Courses
from dmenu import dmenu
from utils import generate_short_title, MAX_LEN

lectures = Courses().current.lectures

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

key, index, selected = dmenu('Select lecture', options, [
    '-l', 5,
])

if key == 0:
    sorted_lectures[index].edit()
elif key == 1:
    new_lecture = lectures.new_lecture()
    new_lecture.edit()
