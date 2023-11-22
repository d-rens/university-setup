#!/usr/bin/python3
from dmenu import dmenu

from courses import Courses

courses = Courses()
current = courses.current

try:
    args = [courses.index(current)]
except ValueError:
    args = []

course_titles = [c.info['title'] for c in courses]

dmenu_args = ['-l', len(courses)] + args

code, index, selected= dmenu('Select course', course_titles)

if index >= 0:
    courses.current = courses[index]
