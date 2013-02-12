#! /bin/bash

ROOT_UID="0"

# Check if run as root
if [ "$UID" -ne "$ROOT_UID" ] ; then
	echo "update reqires root access"
	exit 1
fi

# Update from git
git stash
git pull

cd code
./manage.py collectstatic
./manage.py syncdb

echo ""
echo "** Update complete **"