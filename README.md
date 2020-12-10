# Advent of Code 2020 Solutions
#### By Stephen Blackwell

This was done for fun, and not particularly well.

If you want to reproduce anything in here, go ahead. You can probably find better solutions elsewhere.

If you just want to see some python that reads like plain english, enjoy!

## call.sh
This script can be used to handle calling the tests

	sh call.sh
will call every script from 1-25 until a script fails

	sh call.sh 4
will call day04 on the full input data

	sh call.sh -r 1-4 --range 6-10
ranges can be specified with the -r or --range flag

	sh call.sh -t -r 6-8
the -t flag will try to run test data
stored as python\_source/input/t.day06

## manually calling a script
Any of the python scripts can be run manually:

	python3 day04.py -i input/day04
The -i flag is necessary to specify the input file

