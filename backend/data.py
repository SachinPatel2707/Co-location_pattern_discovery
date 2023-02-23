from backend.db_connection import connect_to_db
from sqlalchemy import text

dist_h = 90000

db_conn = connect_to_db()

# tables = [['A', 'B', 'C', 'D', 'E'], ['loc_a', 'loc_b', 'loc_c', 'loc_d', 'loc_e']]
tables = [['a', 'b', 'c'], ['loc_a', 'loc_b', 'loc_c']]

count = {}
for i in range(len(tables[1])):
    count[tables[0][i]] = db_conn.execute(text('select count(*) from {}'.format(tables[1][i]))).fetchone()[0]

PI = 0.3