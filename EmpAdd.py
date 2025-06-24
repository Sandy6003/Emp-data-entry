#EmpAdd.py<----File Name and Module Name
import pickle,sys
def uniquevalues(empno):
    with open("employee.data","rb") as fp:
        emplist = []
        while (True):
            try:
                record = pickle.load(fp)
                emplist.append(record)
            except EOFError:
                break
    duplicate=False
    for record in emplist:
        if(record[0]==empno):
            duplicate=True
            break
    return duplicate

#Programmere-Defined Exceptions
class InvalidNameError(Exception):pass
class SpaceError(Exception):pass
class ZeroLengthNameError(Exception):pass
# Hitting the Programmere-Defined Exceptions
def validate(name:str): #name=123Guido Van Rossum
    if(len(name)==0):
        raise ZeroLengthNameError
    elif(name.isspace()):
        raise SpaceError
    else:
        words=name.split() # words=['123Guido','Van','Rossum']
        res=True
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            return name
        else:
            raise InvalidNameError
#We are Defining Our Function for  Handling the Exceptions.
def addemp():
    with open("employee.data","ab") as fp:
        while(True):
            try:
                print("-"*50)
                #get Emp details from KBD
                empno=int(input("Enter Employee Number:"))
                empname=validate(input("Enter Employee Name:"))
                empsal=float(input("Enter Employee Salary:"))
                print("-"*50)
                #create an empty list and the place the above values
                lst=[]
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                #dump the object in the file as Record
                dup=uniquevalues(empno) # Function call
                if(not dup):
                    pickle.dump(lst,fp)
                    print("Emp Record Saved in a File")
                else:
                    print("\t{} Employee Number already exist".format(empno))
                print("-" * 50)
                ch=input("Do u want to enter another record(yes/no):")
                if(ch.lower()=="no"):
                    break
            except ValueError:
                print("\tDon't enter alnums,strs and symbols for Empno and salary")
            except InvalidNameError:
                print("\tInvalid Emp Name / Designation--try again")
            except SpaceError:
                print("\tDon't Give Space for Emp Name / Designation--try again")
            except ZeroLengthNameError:
                print("\tU Must Enter Ur Name / Designation--try again")


