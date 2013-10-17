#! /bin/bash

VENV=$(pwd)
source $VENV/production
kill `cat $PID_FILE`