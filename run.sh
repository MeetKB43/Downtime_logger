#!/bin/bash
cd /home/admin/Documents/Downtime_logger
source venv/bin/activate

LOCKFILE="/tmp/dt_logger.lock"
exec 200>$LOCKFILE

flock -n 200 || {
	echo "Script already running. Exiting..."
	sleep 5
	exit 1
}

python src/test_index.py