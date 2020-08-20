#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="pp01db", user="postgres",
                        password="q1w2e3r4", host="172.23.79.43", port="5432")

print("Opened database successfully")
