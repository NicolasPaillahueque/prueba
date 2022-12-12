import mysql.connector


class MyData:

       
    
    @classmethod
    def connect_to_db(cls):
        #Hacer el codigo para la conexion...
        mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword"
        )
        return mydb
        
    @classmethod
    def get_data(cls):
        db = MyData.connect_to_db()
        result = db.query_all_data()
        return result

    