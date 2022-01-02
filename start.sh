#!/bin/bash

# Start the first process
python manage.py runserver 0.0.0.0:8000 &
  
# Start the second process
celery -A backend worker --beat --scheduler django --loglevel=info &
  
# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?