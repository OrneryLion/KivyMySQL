from kivy.lang import Builder
from kivymd.app import MDApp

import mysql.connector


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # define database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="F@rmers123",
            database="first_db"
        )

        # Create a cursor
        c = mydb.cursor()

        # Create an actual database
        c.execute("CREATE DATABASE IF NOT EXISTS first_db")

        # Check to see if database was created
        # c.execute("SHOW DATABASES")
        # for db in c:
        #     print(db)

        # Create A Table
        c.execute("""CREATE TABLE if not exists familyMembers(
        name VARCHAR(50))
        """)

        # Check if table is created
        # c.execute("SELECT * FROM familyMembers")
        # print(c.description)

        # Commit our changes
        mydb.commit()

        # Close our connection
        mydb.close()



        return Builder.load_file('first_db.kv')

    def submit(self):
        # define database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="F@rmers123",
            database="first_db"
        )

        # Create a cursor
        c = mydb.cursor()

        # Add a record
        sql_command = "INSERT INTO familyMembers (name) VALUES (%s)"
        values = (self.root.ids.word_input.text,)

        # Execute SQL command
        c.execute(sql_command, values)

        # Add a little message
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

        # Clear the input box

        self.root.ids.word_input.text = ''


        # Commit our changes
        mydb.commit()

        # Close our connection
        mydb.close()

    def show_records(self):
        # define database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="F@rmers123",
            database="first_db"
        )

        # Create a cursor
        c = mydb.cursor()

        # Grab records from database
        c.execute("SELECT * FROM familyMembers")
        records = c.fetchall()

        word = ''
        # Loop thru records
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text = f'{word}'

        # Commit our changes
        mydb.commit()

        # Close our connection
        mydb.close()


MainApp().run()
