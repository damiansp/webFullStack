#!/bin/bash

echo Initializing database...
python3 database_setup.py

echo Populating tables...
python3 lots_of_menus.py
