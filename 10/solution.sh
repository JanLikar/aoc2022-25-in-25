#!/usr/bin/bash

set -euo pipefail


tick () {
    x=$1
    cycle=$2

    # Convert var name to actual variable
    local -n sig=$3

    modulo=$((cycle % 40))

    if (( modulo >= x && modulo <= (x + 2)  )); then
        echo -n "#"
    else
        echo -n "."
    fi

    if [[ $((cycle % 40)) == 0 ]]; then
        echo
    fi

    if [[ $(((cycle - 20) % 40)) == 0 ]]; then
        sig=$((signal + cycle * x))
    fi
}

x=1
cycle=0
signal=0

while read line; do 
    command=($line)
    
    if [[ "${command[0]}" == "noop" ]]; then
        cycle=$((cycle + 1))
        tick $x $cycle signal
    elif [[ "${command[0]}" == "addx" ]]; then
        cycle=$((cycle + 1))
        tick $x $cycle signal
        cycle=$((cycle + 1))
        tick $x $cycle signal
        x=$((x + command[1]))
    fi
done < input.txt

echo "$signal"
