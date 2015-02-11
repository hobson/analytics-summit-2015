#!/usr/bin/bash
# run redis db server, flask webapp server, and ngrok secure tunnel for Predictive Analytics War Stories Choose Your Own Adventure (paws)
redis-server&
python manage.py runserver&
./ngrok 5001&



