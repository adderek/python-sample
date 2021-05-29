Static analysis is
a set of static rules
to analyze your code and suggest improvements

`pip install pylint pyflakes pycodestyle`
`python3 -m pylint ./before/*.py`
`python3 -m pyflakes ./before/*.py`
`python3 -m pycodestyle ./before/*.py`


All the commands would analyze file by file suggesting fixes/improvements.
You might wish to run them on a project/directory scope to get deeper analysis including relations between them.

Such tools often offer internal rating for the code (example: pylint).
For example my code at start usually had rating 2-8 out of 10.
Until I received code from someone else and then I realized that 10 is the max but minimum can be less than 0 ;)

They often teach you how to write better code.
I have learned MUCH thanks to them.

You might wish to create a custom config file(s) for your project(s) to either enforce some more strict rules or use less strict checks.
I often enforced some naming conventions and indentation rules for my (not necessary python) projects
while loosening anything conflicting with "what I already received"
and increasing screen width to 120 columns (as most people nowawayd are using 1920x1080 or higher resolution).


Have you notices that first example had an error with `a_tuple` that had comma inside first argument?

In the basics there is a logging-not-lazy.
This is because we should avoid concatenation to message and pass arguments as-is so the logger
itself would do whatever required (for example convert to string or add as attachment)
