#!/usr/bin/python3
from dmenu import dmenu

from courses import Courses

courses = Courses()
current = courses.current

try:
    current_index = courses.index(current)
    preselected_item = courses[current_index].info['title']
except ValueError:
    args = []

code, index, selected = dmenu('Select course', [c.info['title'] for c in courses], [
    '-l', len(courses)
] + args)

if index >= 0:
    courses.current = courses[index]
