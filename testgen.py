import sqlite3

# Create db is does not exist, or just connect
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Test Tables
# transactions: date, site, item_id, price
# purchases: date, site, item_id, item_group, count, unit_cost
# labour: date, site, employee_id, hours, rate
c.execute('''CREATE TABLE transactions
            (date text, site text, item_id text, price real)''')
c.execute('''CREATE TABLE purchases
            (date text, site text, item_id text, item_group text, count real, unit_cost real)''')
c.execute('''CREATE TABLE labour
            (date text, site text, emp_id text, hours real, rate real)''')

# Insert some test data
transactions = [('2019-07-31', 'Burnley', 'A10', 5),
                ('2019-07-31', 'Blackburn', 'A10', 5),
                ('2019-07-31', 'Blackburn', 'A15', 6),
                ('2019-08-01', 'Burnley', 'B10', 5),
                ('2019-08-01', 'Burnley', 'A12', 4),
                ('2019-08-01', 'Blackburn', 'A15', 5),
            ]
c.executemany('INSERT INTO transactions VALUES (?,?,?,?)', transactions)

purchases = [('2019-07-31', 'Blackburn', 'A15', 'drink', 10, 3),
             ('2019-07-31', 'Burnley', 'A10', 'drink', 25, 2),
             ('2019-08-01', 'Blackburn', 'A12', 'food', 4, 1.5),
             ('2019-08-01', 'Burnley', 'A15', 'drink', 12, 3),
            ]
c.executemany('INSERT INTO purchases VALUES (?,?,?,?,?,?)', purchases)

labour = [('2019-07-31', 'Blackburn', '001', 8, 7),
          ('2019-07-31', 'Burnley', '005', 6, 6),
          ('2019-08-01', 'Blackburn', '001', 8, 7),
          ('2019-08-01', 'Burnley', '009', 6, 8),
        ]
c.executemany('INSERT INTO labour VALUES (?,?,?,?,?)', labour)


conn.commit()
conn.close()
