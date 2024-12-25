#!/usr/bin/env python3

import mysql.connector


Myquery = ''' INSERT INTO Listing VALUES
    (1, NULL, 'Oshodi Axis', 'This is a good property at a very good location', '3, Oshodi Lane, Lagos', '16000', '2023-09-10 14:00', '2024-10-09 22:30'),
    (2, 1, 'Obalende Luxury', 'This is a luxurious property, best for your relaxation', '4, Ajao Obalende, Lagos', '20000', '2023-09-10 14:10', '2024-10-09 22:40'),
    (3, 2, 'Palm Avenue Estate', 'A perfect place to enjoy light 24/7', '124, Isolo Road, Mushin', '500000', '2023-09-10 14:10', '2024-10-09 22:40');

INSERT INTO Booking VALUES
    (1, 2, 1, '1996-12-09', '1996-12-11', 2000000, 'pending', '2024-12-01 18:21'),
    (2, 1, 1, '2008-12-09', '2008-12-11', 3000000, 'confirmed', '2024-12-01 18:50'),
    (3, 2, 3, '2008-12-09', '2008-12-11', 3000000, 'confirmed', '2024-12-01 18:50');

INSERT INTO Review VALUES
    (1, 1, 1, 4, 'Had a nice time at this property', '2024-10-28 18:00'),
    (2, 2, 1, 3, 'Not so bad', '2024-11-10 23:00'),
    (3, 3, 3, 5, 'Great property I must say', '2024-10-28 18:00'); 
'''


def connect_db():
    try:
        newConnection = mysql.connector.connect(
        user='root', password = '@Olanej1996',
        host='localhost',
        database = 'Alx_prodevv'
        )
        print("Connected successfully")
        return newConnection
        
    except mysql.connector.Error as err:
            print(f"Error is {err}")
            return None


def insert_data(connection= None, data=None):
    
    if connection == None and data == None:
        try:
            query = Myquery.strip().split(';')
            for queries in query:
                if queries.strip():
                    connection = connect_db()
                    if connection and connection.is_connected():
                        with connection.cursor() as cursor:
                            cursor.execute(queries)
                            print("Data Inserted successfully")
                            connection.commit()
                    
        except mysql.connector.Error as err:
            print(f"Error is {err}")

connect_db()
insert_data()