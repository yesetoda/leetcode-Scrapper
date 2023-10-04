import psycopg2

def add_record_if_not_exists(full_name, nick_name, rank, easy, medium, hard, languages, total):
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            database="postgres",
            user="postgres",
            password="1pass"
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Check if the database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='postgres'")
        database_exists = cursor.fetchone()

        # If the database exists, proceed with the operation
        if database_exists:
            # Check if the table exists
            cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'leetcode_profiles')")
            table_exists = cursor.fetchone()[0]

            # If the table exists, proceed with the operation
            if table_exists:
                # Check if the full name already exists in the table
                check_query = "SELECT 1 FROM leetcode_profiles WHERE fullname = %s"
                cursor.execute(check_query, (full_name,))
                result = cursor.fetchone()

                # If the full name does not exist, insert a new record
                if not result:
                    insert_query = """
                        INSERT INTO leetcode_profiles (fullname, nickname, rank, easy, medium, hard, languages, total)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    record_values = (full_name, nick_name, rank, easy, medium, hard, languages, total)
                    cursor.execute(insert_query, record_values)
                    connection.commit()
                    print("New record added successfully!")
                else:
                    print("Record already exists!")
            else:
                print("Table 'leetcode_profiles' does not exist.")
        else:
            print("Database 'postgres' does not exist.")

    except psycopg2.OperationalError as error:
        print("Error connecting to the database:", error)

    except (Exception, psycopg2.Error) as error:
        print("Error executing SQL query:", error)

    finally:
        # Close the cursor and the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()



# import psycopg2

# def create_database():
#     try:
#         # Establish a connection to the default PostgreSQL database
#         connection = psycopg2.connect(
#             host="localhost",
#             port=5432,
#             database="postgres",
#             user="postgres",
#             password="1pass"
#         )
#         connection.autocommit = True  # Enable autocommit for database creation

#         # Create a cursor to execute SQL queries
#         cursor = connection.cursor()

#         # Check if the database exists
#         cursor.execute("SELECT 1 FROM pg_database WHERE datname='leetcode'")
#         database_exists = cursor.fetchone()

#         # If the database does not exist, create it
#         if not database_exists:
#             cursor.execute("CREATE DATABASE leetcode")
#             print("Database 'leetcode' created successfully!")

#     except psycopg2.OperationalError as error:
#         print("Error connecting to the database:", error)

#     finally:
#         # Close the cursor and the database connection
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# def create_table():
#     try:
#         # Establish a connection to the PostgreSQL database
#         connection = psycopg2.connect(
#             host="localhost",
#             port=5432,
#             database="leetcode",
#             user="postgres",
#             password="1pass"
#         )

#         # Create a cursor to execute SQL queries
#         cursor = connection.cursor()

#         # Check if the table exists
#         cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'leetcode_profiles')")
#         table_exists = cursor.fetchone()[0]

#         # If the table does not exist, create it
#         if not table_exists:
#             create_table_query = """
#                 CREATE TABLE leetcode_profiles (
#                     fullname VARCHAR(255) PRIMARY KEY,
#                     nickname VARCHAR(255),
#                     rank VARCHAR(255),
#                     easy INTEGER,
#                     medium INTEGER,
#                     hard INTEGER,
#                     languages VARCHAR(255),
#                     total INTEGER
#                 )
#             """
#             cursor.execute(create_table_query)
#             print("Table 'leetcode_profiles' created successfully!")

#     except (Exception, psycopg2.Error) as error:
#         print("Error executing SQL query:", error)

#     finally:
#         # Close the cursor and the database connection
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# def add_record_if_not_exists(full_name, nick_name, rank, easy, medium, hard, languages, total):
#     try:
#         # Establish a connection to the PostgreSQL database
#         connection = psycopg2.connect(
#             host="localhost",
#             port=5432,
#             database="leetcode",
#             user="postgres",
#             password="1pass"
#         )

#         # Create a cursor to execute SQL queries
#         cursor = connection.cursor()

#         # Check if the table exists
#         cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'leetcode_profiles')")
#         table_exists = cursor.fetchone()[0]

#         # If the table exists, proceed with the operation
#         if table_exists:
#             # Check if the full name already exists in the table
#             check_query = "SELECT 1 FROM leetcode_profiles WHERE fullname = %s"
#             cursor.execute(check_query, (full_name,))
#             result = cursor.fetchone()

#             # If the full name does not exist, insert a new record
#             if not result:
#                 insert_query = """
#                     INSERT INTO leetcode_profiles (fullname, nickname, rank, easy, medium, hard, languages, total)
#                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#                 """
#                 record_values = (full_name, nick_name, rank, easy, medium, hard, languages, total)
#                 cursor.execute(insert_query, record_values)
#                 connection.commit()
#                 print("New record added successfully!")
#             else:
#                 print("Record already exists!")
#         else:
#             print("Table 'leetcode_profiles' does not exist.")

#     except (Exception, psycopg2.Error) as error:
#         print("Error executing SQL query:", error)

#     finally:
#         # Close the cursor and the database connection
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# Usage example
# create_database()
# create_table()
# add_record_if_not_exists("John Doe", "JD", "Senior", 10, 15, 5, "Python, SQL", 30)