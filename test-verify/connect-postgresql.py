#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="pp01", user="pp01",
                        password="q1w2e3r4", host="127.0.0.1", port="5432")

print("Opened database successfully")
