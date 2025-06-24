#Program for Reading Employee Deatils and save then File by using Pickling Concpt
#EmpPickEx1.py
import pickle
with open("emp.pick","ab") as fp:
    while(True):
        print("-"*50)
        #get Emp details from KBD
        empno=int(input("Enter Employee Number:"))
        empname=input("Enter Employee Name:")
        empsal=float(input("Enter Employee Salary:"))
        empdsg=input("Enter Employee Designation:")
        print("-"*50)
        #create an empty list and the place the above values
        lst=[]
        lst.append(empno)
        lst.append(empname)
        lst.append(empsal)
        lst.append(empdsg)
        #dump the object in the file as Record
        pickle.dump(lst,fp)
        print("Emp Record Saved in a File")
        print("-" * 50)
        ch=input("Do u want to enter another record(yes/no):")
        if(ch.lower()=="no"):
            print("Thx for this program")
            break


