#! /bin/sh
set -e

if [ -z $1 ]
then
  echo "USAGE: start_venv.sh venv [workdir]"
  exit 2
fi

VENV=$(pwd)

if [ -z $2 ]
then
  STARTDIR=$VENV/$1
else
  STARTDIR=$VENV/$2
fi

if [ ! -f $VENV/production ]
then
  echo "Could not find $VENV/production"
  exit 2
fi

source $VENV/bin/activate
cd $STARTDIR
source $VENV/production
python manage.py $MANAGE_COMMAND
