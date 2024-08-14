#!/bin/bash
if [ "$1" = 'debug' ];then
  sleep infinity
elif [ "$1" = 'runserver' ];then
  sleep infinity
fi

exec "$@"
