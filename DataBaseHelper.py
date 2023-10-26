import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con=con = connector.connect(host="localhost", port="3306", user ="root", password="", database="crud_op_python")
        query='create table if not exists crudOp(userId int primary key, userName varchar(150), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

    # insert data
    def insert_data(self, userId, userName, phone):
        query="insert into crudOp(userId, userName, phone) values({}, '{}', '{}' )".format(
            userId, userName, phone
        )
      
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("data is saved")

    # fetching data
    def fetchAllData(self):
        query="select * from crudOp"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            
            print("User Id :", row[0])
            print("User Name : ", row[1])
            print("phone : ", row[2])
            print("\n")
    
    # deleting data
    def deleteUser(self, userId):
        del_query="delete from crudOp where userId={}".format(userId)
       
        cur = self.con.cursor()
        cur.execute(del_query)
        self.con.commit()
        print("user deleted")

    # updating data
    def updateData(self, userId, userName):
        query="update crudOp set userName='{}' where userId={}".format(userName, userId)
    
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("data updated")
