import backend

# backend.queries.print_all_entries()
backend.queries.drop_all_tables(['loc_a', 'loc_b', 'loc_c', 'loc_d', 'loc_e'])
backend.queries.drop_all_tables(['ab', 'ac', 'bc'])
backend.queries.create_all_tables()
backend.queries.load_initial_data()
backend.generate_size_two_tables()