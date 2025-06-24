#EmpView.py<---File Name and Module Name
import pickle
def viewemployee():
    #get employee number from KBD
    empno=int(input(("Enter Employee Number:")))
    #Get the Data from the File
    emplist=[]
    with open("employee.data","rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                emplist.append(record)
            except EOFError:
                break
        res="NotFound"
        for emprec in emplist:
            if(emprec[0]==empno):
                res="found"
                rec=emprec
                break
        if(res=="found"):
            print("----------------------------------")
            print("\tEmployee Number:{}".format(rec[0]))
            print("\tEmployee Name:{}".format(rec[1]))
            print("\tEmployee Salary:{}".format(rec[2]))
            print("----------------------------------")
        else:
            print("\t{} Employee Number Does not Exist".format(empno))

def viewallemployees():
    with open("employee.data","rb") as fp:
        print("----------------------------------")
        print("List of Employee Records")
        print("----------------------------------")
        while(True):
            try:
                record = pickle.load(fp)
                for val in record:
                    print(val,end="\t\t")
                print()
            except EOFError:
                print("----------------------------------")
                break

