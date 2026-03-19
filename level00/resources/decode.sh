#!/bin/bash

input="cdiiddwpgswtgt"
shift=11

alphabet=abcdefghijklmnopqrstuvwxyz
rotated=${alphabet:$shift}${alphabet:0:$shift}

echo "$input" | tr "$alphabet" "$rotated"
