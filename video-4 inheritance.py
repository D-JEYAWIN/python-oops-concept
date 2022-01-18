class Employee:
    
    extra_amt=1.04
    def __init__(self,fname,lname,pay):
        self.fname = fname 
        self.lname = lname
        self.pay= pay
        self.mail = fname + lname + '@company.com'
        
        
    def fullname(self):
        return 'full name :{} {}'.format(self.fname,self.lname)
    
    def raises(self):
        
        self.pay= int(self.pay * Employee.extra_amt)
        
class Developer(Employee):
    pass
    
emp_1 = Developer('JEYAWIN','alok', 5000)
emp_2 = Developer('alok','alok', 60000)   
        

print(emp_1.mail)
print(emp_2.mail)
