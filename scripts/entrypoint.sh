#!/bin/sh
set -e
for arg in "$@"
do
    mode=$arg
done

if [ "$mode" = "shell" ]
then
    exec /bin/bash
elif [ "$mode" = "lint" ]
then
	exec flake8 app/ --statistics
elif [ "$mode" = "dev" ]
then
	exec uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
elif [ "$mode" = "test" ]
then
	exec pytest --cov=app --cov-report term-missing -vv --showlocals
elif [ "$mode" = "prod" ]
then
	exec circusd config/workflow-api.init
else
	echo "Unknown command"
fi
