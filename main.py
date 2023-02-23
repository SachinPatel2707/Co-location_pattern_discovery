import backend

# backend.queries.print_all_entries()
backend.queries.drop_all_tables(['a', 'b', 'c', 'd', 'e'])
backend.queries.drop_all_tables(['ab', 'ac', 'bc'])
backend.queries.create_all_tables()
backend.queries.load_initial_data()
backend.controller.get_counts_of_each_class()
backend.controller.generate_size_two_tables()