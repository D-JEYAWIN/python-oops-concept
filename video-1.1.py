class Employee:
    def __init__(self,fname,lname,phno,address):
        self.fname = fname 
        self.lname = lname
        self.phno = phno
        self.address = address
        self.mail = fname + lname + '@company.com'
        
    def fullname(self):
        return 'full name :{} {}'.format(self.fname,self.lname)
    
emp_1=Employee('JEYAWIN','alok',9876543211,'erode')
emp_2=Employee('alok','alok',9872342211,'erode')        

print(emp_1.mail)
print(emp_2.mail)

print(emp_1.fullname())
print(emp_2.fullname())