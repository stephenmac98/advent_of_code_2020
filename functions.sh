#!/bin/sh

# Ensures an input is a valid
validate_int()
{
	echo $1 | grep [a-z,A-Z]
	if [ $? -eq 0 ]
	then
		echo "$1 is not a valid number"
		exit 1
	fi
}

# Runs the python script associated with the number it is called with
# run_number 7 calls day07 with the correct input
run_number()
{
	echo "\n***** Calling Script $1 *****\n"
	# Add a leading zero if one is required
	if [ $1 -lt 10 ]
	then
		python3 ${SOURCE_DIR}/day0${1}.py -i ${INPUT_DIR}day0$1
	else
		python3 ${SOURCE_DIR}/day${1}.py -i ${INPUT_DIR}day$1
	fi

	# Make sure the script executed successfully
	if [ $? -ne 0 ]
	then
		echo "\n*****Script $1 failed*****\n"
		exit 1
	fi
}

# Checks that a provided range is valid
# Calls run_number for every value in range
run_range()
{
	# Extract the range bounds
	lower=$(echo $1 | cut -f1 -d-)
	upper=$(echo $1 | cut -f2 -d-)

	# Confirm that the range values we have pulled out are in fact integers
	validate_int $lower
	validate_int $upper

	# Make sure that the range requested is logical
	if [ $lower -ge $upper ]
	then
		echo "$1 is not a valid range"
	fi

	for n in $( seq $lower $upper )
	do
		run_number $n
	done
}
