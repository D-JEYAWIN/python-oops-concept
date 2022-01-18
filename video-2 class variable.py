class Employee:
    
    num_of_emp=0
    extra_amt=1.04
    def __init__(self,fname,lname,phno,address,pay):
        self.fname = fname 
        self.lname = lname
        self.phno = phno
        self.address = address
        self.pay= pay
        self.mail = fname + lname + '@company.com'
        
        Employee.num_of_emp +=1
        
    def fullname(self):
        return 'full name :{} {}'.format(self.fname,self.lname)
    
    def raises(self):
        
        self.pay= int(self.pay * Employee.extra_amt)
    
emp_1=Employee('JEYAWIN','alok',9876543211,'erode',5000)
emp_2=Employee('alok','alok',9872342211,'erode',60000)   
emp_3=Employee('JEY','alok',9878543211,'erode',5600)
emp_4=Employee('ads','alok',98723489211,'erode',6000)        

emp_1.extra_amt=5

print(emp_1.pay)
emp_1.raises()
print(emp_1.pay)

print(emp_1.extra_amt)


print(Employee.num_of_emp)