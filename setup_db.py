import sqlite3

# Function to create the SQLite database
def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('population_data.db')
    cursor = conn.cursor()

    # Create table for population data
    cursor.execute('''CREATE TABLE IF NOT EXISTS population_data (
                        id INTEGER PRIMARY KEY,
                        series_name TEXT,
                        country_name TEXT,
                        country_code TEXT,
                        year INTEGER,
                        value REAL
                    )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to insert sample data into the database
def insert_sample_data():
    # Sample data to insert
    data = [
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2001, 9.4),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2002, 9.4),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2003, 9.5),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2004, 9.8),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2005, 9.6),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2006, 9.6),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2007, 9.7),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2008, 9.8),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2009, 9.6),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2010, 9.5),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2011, 9.2),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2012, 9.0),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2013, 8.5),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2014, 8.3),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2015, 8.0),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2016, 7.8),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2017, 7.6),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2018, 7.3),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2019, 7.0),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2020, 6.8),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2021, 6.8),
        ('Birth rate, crude (per 1,000 people)', 'Italy', 'ITA', 2022, None),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2001, 9.3),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2002, 9.2),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2003, 8.9),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2004, 8.8),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2005, 8.4),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2006, 8.7),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2007, 8.6),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2008, 8.7),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2009, 8.5),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2010, 8.5),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2011, 8.3),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2012, 8.2),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2013, 8.2),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2014, 8.0),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2015, 8.0),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2016, 7.8),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2017, 7.6),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2018, 7.4),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2019, 7.0),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2020, 6.8),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2021, 6.6),
        ('Birth rate, crude (per 1,000 people)', 'Japan', 'JPN', 2022, None),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2001, 11.7),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2002, 10.3),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2003, 10.2),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2004, 9.8),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2005, 9.0),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2006, 9.2),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2007, 10.1),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2008, 9.4),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2009, 9.0),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2010, 9.4),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2011, 9.4),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2012, 9.6),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2013, 8.6),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2014, 8.6),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2015, 8.6),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2016, 7.9),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2017, 7.0),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2018, 6.4),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2019, 5.9),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2020, 5.3),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2021, 5.1),
        ('Birth rate, crude (per 1,000 people)', 'Korea, Rep.', 'KOR', 2022, None)

        
    ]

    # Connect to SQLite database
    conn = sqlite3.connect('population_data.db')
    cursor = conn.cursor()

    # Insert sample data into the population_data table
    cursor.executemany('''INSERT INTO population_data (
                            series_name, country_name, country_code, year, value
                          ) VALUES (?, ?, ?, ?, ?)''', data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to query data from the database
def query_data():
    # Connect to SQLite database
    conn = sqlite3.connect('population_data.db')
    cursor = conn.cursor()

    # Query data from the population_data table
    cursor.execute('''SELECT * FROM population_data''')
    rows = cursor.fetchall()

    # Print the queried data
    for row in rows:
        print(row)

    # Close connection
    conn.close()

# Main function to run the script
if __name__ == '__main__':
    # Create the database
    create_database()

    # Insert sample data into the database
    insert_sample_data()

    # Query and print the data from the database
    query_data()
