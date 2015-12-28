#!/bin/bash
set -e
LOGFILE=/home/xtian/scripts/bot_cards/logs.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=4
# user/group to run as
USER=xtian
GROUP=xtian
VIRTDIR=/home/xtian/venvs/bot_cards
cd /home/xtian/scripts/bot_cards
source $VIRTDIR/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec $VIRTDIR/bin/python /home/xtian/scripts/bot_cards/app.py