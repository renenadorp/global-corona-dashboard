#!/bin/bash
cd /Users/rnadorp/Documents/Privé/python/GlobalCoronaDashboard/global-corona-dashboard
export SECRET_KEY='5f352379324c22463451387a0aec5d2f'
export DATABASE_URL="postgresql://localhost/medium-ml"
flask run 