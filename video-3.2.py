class Employee:
    
    num_of_emp=0
    extra_amt=1.04
    def __init__(self,fname,lname,pay):
        self.fname = fname 
        self.lname = lname
        self.pay= pay
        self.mail = fname + lname + '@company.com'
        
        Employee.num_of_emp +=1
        
    def fullname(self):
        return 'full name :{} {}'.format(self.fname,self.lname)
    
    def raises(self):
        
        self.pay= int(self.pay * Employee.extra_amt)
        
    @classmethod
    def set_extra(cls, amount):
        cls.extra_amt=amount
        
    @classmethod
    def from_str(cls, emp_str):
        fname,lname,pay = emp_str.split('-')
        return cls(fname,lname,pay)
    
    @staticmethod
    def is_work(day):
        if day.weekday==5 or day.weekday==6:
            return False 
        return True
            
            
emp_1=Employee('JEYAWIN','alok',5000)
emp_2=Employee('alok','alok',60000)   
#emp_3=Employee('JEY','alok',5600)
#emp_4=Employee('ads','alok',6000)

import datetime
my_date=datetime.date(2022, 1, 12)

print(Employee.is_work(my_date))





  