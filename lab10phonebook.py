import psycopg2
import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()




"""
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
	VALUES (22030314, 'Gaziza', 'BurundaiTrain', 7475558442);
--------------------------------------------------------
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
	VALUES (22030305, 'Amina', 'Artroz', 7028570664);
--------------------------------------------------------
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
	VALUES (22030280, 'Aisha', 'FromHaterToLover', 7017663356);
--------------------------------------------------------
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
	VALUES (22031168, 'Arai', 'DanceBreaker', 7029545990);
--------------------------------------------------------
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
	VALUES (22030315, 'Sabina', 'SuicideGirl', 7073002710);
--------------------------------------------------------
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
	VALUES (22030520, 'Kamila', 'Panic', 7017478878);
--------------------------------------------------------
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
	VALUES (22030292, 'Dina', 'Flyer', 7029545990);
"""







"""
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
select 22030314, 'Gaziza', 'BurundaiTrain', 7475558442
--------------------------------------------------------
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
select 22030305, 'Amina', 'Artroz', 7028570664
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
select 22030280, 'Aisha', 'FromHaterToLover', 7017663356
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
select 22031168, 'Arai', 'DanceBreaker', 7029545990
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
select 22030315, 'Sabina', 'SuicideGirl', 7073002710
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
select 22030520, 'Kamila', 'Panic', 7017478878
INSERT INTO phonebook."book of num"(
	"ID", "Name", "Nickname", "Phone num")
select 22030292, 'Dina', 'Flyer', 7029545990
"""