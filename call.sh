#!/bin/bash

# Include the support functions
SCRIPT_DIR=`dirname $0`

. $SCRIPT_DIR/functions.sh

SOURCE_DIR="${SCRIPT_DIR}/python_source"
INPUT_DIR="${SOURCE_DIR}/input/"

# Check if there was any input
if [ $# -eq 0 ]
then
	run_range 1-100
fi

# Loop through all of the inputs
while test $# -gt 0; do
	case "$1" in
		--range | -r)
			shift
			run_range $1
			shift
			;;
		--test | -t)
			INPUT_DIR="${INPUT_DIR}t."
			shift
			;;
		*)
			validate_int $1
			run_number $1
			shift
			;;
	esac
done

