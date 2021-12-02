import pymysql


def insert_data(data):
    # Establish connection to database

    connection = pymysql.connect(
        # specify host name
        
        host="mysql",
        
        # specify username
        user="root",
        
        # enter password for above user
        password="Pi1",
        
        # default port number for MySQL is 3306
        port=3306,
        
        # specify database name
        db="GrafanaDB"
    )

    # Make cursor for establish connection

    cursor = connection.cursor()

    # Query to insert data into database

    for d in data:
        
        query = "INSERT IGNORE INTO grafanadb\
                        (date,property,value)\
                    VALUES\
                        ('" + d[0] + "', '" + d[1] + "', " + d[2] + ");"
            
        # Execute query here
        cursor.execute(query)
        
    # Execute query to commit changes
    connection.commit()
    cursor.close()




# Create Table
create = """CREATE TABLE grafanadb(
    date DATETIME NOT NULL,
    property VARCHAR(250) NOT NULL,
    value FLOAT(10,6) NOT NULL,
    PRIMARY KEY ( date, property, value )
 );"""