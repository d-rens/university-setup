## Changes
Based on [this](https://github.com/gillescastel/university-setup).

This fork aims to remove stuff that makes it unnecessary complex like the google calendar integration.
But on the other hand add features to make it more effective.

The programs used will also change **from rofi to dmenu** and **from polybar
also to dwmblocks**. dmenu will be usable under all unix variants and the dwm
statusbar will be a script so that one can also embed it into other bars.

# Managing LaTeX lecture notes
This repository complements the original author's [third blog post about his and my note taking setup](https://castel.dev/post/lecture-notes-3).


#### File structure

```
ROOT
├── riemann-surfaces
│   ├── info.yaml
│   ├── master.tex
│   ├── lec_01.tex
│   ├── ...
│   ├── lec_13.tex
│   ├── figures
│   │   ├── analytical-continuation-algebraic-equations.pdf
│   │   ├── analytical-continuation-algebraic-equations.pdf_tex
│   │   ├── analytical-continuation-algebraic-equations.svg
│   │   └── ...
│   └── UltiSnips
│       └── tex.snippets
├── selected-topics
└── ...
```

Contents of `info.yaml`
```yaml
title: 'Riemann Surfaces'
short: 'RSurf'
url: 'https://'
```

Contents of  `master.tex`:

```tex
\documentclass[]{report}
\input{~/notes/preamble.tex}
...
\title{Riemann surfaces}
\begin{document}
    \maketitle
    \tableofcontents
    \clearpage
    % start lecture
    \input{lec_01.tex}
    ...
    \input{lec_12.tex}
    % end lectures
\end{document}
```

Here `% start lectures` and `% end lectures` are important.

A lecture file contains a line
```latex
\lecture{1}{02-06-2024}{Introduction to our current Techno-Feudalism}
```
which is the lecture number, date an title of the lecture. Date format is configurable in `config.py`.

#### `init-all-courses.py`
**This is the first file you should run. After creating the directory and the
`info.yaml` file for each course, it creates all `master.tex` files.**

#### `config.py`
This is where you configure the
root folder of the file structure, and similar stuff. You can also configure
the date format used in some places (lecture selection dialog and LaTeX files).

#### `courses.py`
This file defines `Course` and `Courses`.
`Courses` is a list of `Course`s in the `ROOT` folder.
A `Course` is a python object that represents a course.
It has a `name`, a `path`, and some `info` (which reads from `info.yaml`).
You can also access its lectures.

`Courses` also has a `current` property which points to the current course.
When setting this property, the script updates the `~/current_course` symlink
to point to the current course (configurable in `config.py`)
Furthermore, it writes the short course code to `/tmp/current_course`.
This way, when using dwmblocks, polybar or most other similar statusbars you
can add the script to show the current course short code in your panel.

##### dwmblocks
*will arrive shortly*

##### polybar
```ini
[module/currentcourse]
interval = 5
type = custom/script
tail = true
exec = cat /tmp/current_course
```

#### `lectures.py`
This file defines `Lectures`, the lectures for one course and `Lecture`, a
single lecture file `lec_xx.tex`.
A `Lecture` has a `title`, `date`, `week`, which get parsed from the LaTeX
source code. It also has a reference to its course.
When calling `.edit()` on a lecture, it opens up lecture in Vim.

`Lectures` a is class that inherits from `list` that represents the lectures in one course.
It has a method `new_lecture` which creates a new lecture,
`update_lectures_in_master`, which when you call with `[1, 2, 3]` updates
`master.tex` to include the first three lectures, `compile_master` which
compiles the `master.tex` file.

#### `dmenu-courses.py`
When you run this file, it opens dmenu which allows you to activate a course.

#### `dmenu-lectures.py`
When you run this file, it will show you lectures of the current course.
Selecting one opens up the file in Vim, pressing `|` creates a new lecture.

#### `dmenu-lectures-view.py`
This opens up a rofi dialog to update which lectures are included in `master.tex`

Defined options are `current lecture`, `last two lectures`, `all lectures` and `previous lectures`.

#### `dmenu.py`
Wrapper function for dmenu.

#### `utils.py`
Some utility functions.

#### `compile-all-masters.py`
This script updates the `master.tex` files to include all lectures and compiles
them. I use it when syncing my notes to other devices.

> issues and prs are most welcome
