class Student:
   def set_data(self, org, code):
       self.org = org
       self.code = code

class Sports(Student):
   def set_name(self, sport, marks ):
      self.sport = sport
      self.marks = marks

class Test(Student):
   def set_name1(self, subject, marks1):
       self.subject = subject
       self.marks1 = marks1

class Result(Sports, Test):
   def get_data(self, id, name):
       self.id = id
       self.name = name

def display(self):
    print(f'Student ID:{self.code}{self.id}')
    print(f'Student name: {self.name}')
    print(f'Department:{self.org}')
    print(f'Sports marks:{self.sport} - {self.marks}')
    print(f'Subject marks:{self.subject} - {self.marks1}')

stu1 = Result()
stu1.get_data(1101,"Asmita" )
stu1.set_name("Tennis", "40/50")
stu1.set_name1("Advanced Python", "48/50")
stu1.set_data("MIT ADT University","MITU19IMBI0012")
stu1.display()

