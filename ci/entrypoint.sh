#!/bin/bash
set -e

AVIALABLE=0
RESULT_NAME="${RESULT_NAME:-front_test}"
SELNAME="${SELNAME:-localhost}"
SELPORT="${SELPORT:-4444}"

while [ $AVIALABLE = 0 ]
do
    result=$(curl http://$SELNAME:$SELPORT/status | jq .[].nodes[].availability)
    if [ $result = '"UP"' ]
    then
        echo "Selenoid available now!"
        AVIALABLE=1
    else
        echo "Selenoid not available yet..."
        sleep 2
    fi
done

py.test storage -p no:cacheprovider --junitxml=../results/$RESULT_NAME.xml --alluredir=storage/results_allure $@
python3 storage/GetTestData.py