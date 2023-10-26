import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

import mysql.connector as connector
from DataBaseHelper import DBHelper

def main():
    print("how many times you want to perform operation")
    speaker.Speak("how many times you want to perform operation")
    times = int(input())
    count=1
    db = DBHelper()

    while count<=times:
        try:
            print("***********PRESS VALID KEY TO PERFORM REQUIRED TASK************")
            print
            print("Press 1 to insert data")
            speaker.Speak("Press 1 to insert data")
            print("Press 2 to fetch all data")
            speaker.Speak("Press 2 to fetch all data")
            print("Press 3 to delete data")
            speaker.Speak("Press 3 to delete data")
            print("Press 4 to update data")
            speaker.Speak("Press 4 to update data")
            print()
        
            num = int(input("enter valid number "))
            match num:
                case 1:
                    print("enter valid credential ")
                    userId=int(input("ID : "))
                    userName=input("Name : ")
                    userPhone=input("Phone : ")
                    db.insert_data(userId, userName, userPhone)
                    speaker.Speak("Congratulation! your data is saved to DB")

                case 2:
                    db.fetchAllData()
                    speaker.Speak("here, you have your fetched data")
                
                case 3:
                    print("enter ID of which you want to delete data")
                    userId=int(input("ID : "))
                    db.deleteUser(userId)
                    speaker.Speak("data is succesfully deleted")

                
                case 4:
                    print("enter ID of which you want to update User Name ")
                    userId=int(input("ID : "))
                    print("set name what you want...")
                    setName=input("Name : ")
                    db.updateData(userId, setName)
                    speaker.Speak("your data succesfully updated ")

                case _:
                    print("You did not give valid num")  
        
            count +=1  
        except Exception as e:
                
            print("your maximum time out ")

    
if __name__ == "__main__":      
    main()
    print("Bye Bye !!\n Thanks for using me ...\n")
    speaker.Speak("Bye Bye! Thanks for using me")

 








