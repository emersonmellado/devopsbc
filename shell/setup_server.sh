#!/bin/bash
Year=`date +%Y`
Month=`date +%m`
Day=`date +%d`
Hour=`date +%H`
Minute=`date +%M`
Second=`date +%S`

# Installing necessary applications
echo "Starting installation of HTOP"
brew install htop
echo "Finished installation of Htop"


echo "Starting installation of mc"
brew install mc
echo "Finished installation of mc"

echo "This was all done on:"
echo `date`
echo "Current Date is: $Day-$Month-$Year"
echo "Current Time is: $Hour:$Minute:$Second"
