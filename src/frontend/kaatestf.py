# pylint: skip-file
from ohtu-miniprojekti import src
from src import backend
from backend.db import dbtest

dbtest.test_connection()


