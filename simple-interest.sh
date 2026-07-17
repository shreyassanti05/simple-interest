#!/bin/bash

# Simple Interest Calculator

echo "Simple Interest Calculator"

echo -n "Enter the Principal Amount: "
read principal

echo -n "Enter the Rate of Interest: "
read rate

echo -n "Enter the Time Period (in years): "
read time

# Calculate Simple Interest
interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)

echo ""
echo "Principal Amount : $principal"
echo "Rate of Interest : $rate%"
echo "Time Period      : $time years"
echo "Simple Interest  : $interest"
