from backend.db_connection import connect_to_db
from sqlalchemy import text

dist_h = 90000
PI = 0.3

db_conn = connect_to_db()

# tables = [['A', 'B', 'C', 'D', 'E'], ['loc_a', 'loc_b', 'loc_c', 'loc_d', 'loc_e']]
tables = [[], ['a', 'b', 'c']]

count = {}