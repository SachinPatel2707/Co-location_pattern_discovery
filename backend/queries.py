from sqlalchemy import text
from backend.data import *
import os

create_all_tables_queries = []
create_all_tables_queries.append(text("create table if not exists a (gid serial primary key, longitude varchar(50), latitude varchar(50), geog geography(point));"))
create_all_tables_queries.append(text("create table if not exists b (gid serial primary key, longitude varchar(50), latitude varchar(50), geog geography(point));"))
create_all_tables_queries.append(text("create table if not exists c (gid serial primary key, longitude varchar(50), latitude varchar(50), geog geography(point));"))
create_all_tables_queries.append(text("create table if not exists d (gid serial primary key, longitude varchar(50), latitude varchar(50), geog geography(point));"))
create_all_tables_queries.append(text("create table if not exists e (gid serial primary key, longitude varchar(50), latitude varchar(50), geog geography(point));"))

create_indexes_queries = []
create_indexes_queries.append(text("create index a_idx on a using GIST (geog);"))
create_indexes_queries.append(text("create index b_idx on b using GIST (geog);"))
create_indexes_queries.append(text("create index c_idx on c using GIST (geog);"))
create_indexes_queries.append(text("create index d_idx on d using GIST (geog);"))
create_indexes_queries.append(text("create index e_idx on e using GIST (geog);"))

def create_all_tables():
    for q in create_all_tables_queries:
        db_conn.execute(q)
    create_indexes()

def create_indexes():
    for q in create_indexes_queries:
        db_conn.execute(q)

def drop_all_tables(arr):
    for name in arr:
        db_conn.execute(text("drop table if exists {}".format(name)))

def load_initial_data():
    for table in tables[1]:
        path = os.getcwd() + "/data/small_dataset/" + table + ".txt"
        file = open(path, 'r')
        data = file.readlines()
        for line in data:
            long, lat = line.split(",")
            db_conn.execute(text("insert into {} (longitude, latitude, geog) values ({}, {}, 'POINT({} {})')".format(table, long, lat, long, lat)))
        file.close()