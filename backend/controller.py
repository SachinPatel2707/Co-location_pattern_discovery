import geopandas as gpd
from backend.data import *
import sqlalchemy as alc
import os

def get_counts_of_each_class():
    for i in range(len(tables[1])):
        count[tables[1][i]] = db_conn.execute(text('select count(*) from {}'.format(tables[1][i]))).fetchone()[0]

def spatial_join(x, y):
    sql = alc.text("select {}.geog, {}.gid as gid1, {}.gid as gid2 from {} join {} on ST_DWithin({}.geog, {}.geog, {})".format(x, x, y, x, y, x, y, dist_h))
    listings = gpd.GeoDataFrame.from_postgis(sql, db_conn, geom_col='geog')
    return listings

def fill_size_two_table(col1, col2, data):
    table_name = col1+col2
    sql = alc.text("create table {} (id serial primary key, {} integer, {} integer)".format(table_name, col1, col2))
    db_conn.execute(sql)

    if (data.shape[0] > 0):
        for i in range(data.shape[0]):
            sql = alc.text("insert into {} ({}, {}) values ({}, {})".format(table_name, col1, col2, data['gid1'][i], data['gid2'][i]))
            db_conn.execute(sql)

def generate_size_two_tables():
    new_tables = []
    for i in range(len(tables[1])):
        for j in range(i+1, len(tables[1])):
            join_res = spatial_join(tables[1][i], tables[1][j])
            col1 = tables[1][i]
            col2 = tables[1][j]
            new_tables.append(col1+col2) 
            fill_size_two_table(col1, col2, join_res)
    tables.append(new_tables)
    verify_PI(2)

def verify_PI(size):
    for t in tables[size]:
        cols = [x for x in t]
        cur_count = {}
        for i in range(len(t)):
            cur_count[t[i]] = db_conn.execute(alc.text("select count(distinct {}) from {}".format(cols[i], t))).fetchone()[0]
        cur_PI = getPI(cols, cur_count)
        # print(cur_PI)
        if (cur_PI < PI):
            db_conn.execute(text('drop table {}'.format(t)))

def getPI(cols, cur_count):
    min_pr = 10
    for col in cols:
        pr = cur_count[col]/count[col]
        min_pr = min(min_pr, pr)
    return min_pr
