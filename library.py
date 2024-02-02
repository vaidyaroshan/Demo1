class Student:
    def __init__(self,studid,studname,studclass):
        self.studid=studid
        self.studname=studname
        self.studclass=studclass
class Library:
    def __init__(self):
        self.Booklist=dict()
    def Addbook(self,Bookname):
        if Bookname in self.Booklist.keys():
            self.Booklist[Bookname]+=1
        else:
            self.Booklist[Bookname]=1
    
    def issue(self,issuedate,Bookname,student):
        if self.Booklist[Bookname] >=1:
            print(f"{Bookname} is Issued To {student.studname}")
            self.Booklist[Bookname] -=1
        else:
            print(f"{Bookname} Is not available !")
   
    def submission(self,returndate,Bookname,student):
        self.Booklist[Bookname]+=1
    
             
        
        
   
        
   
    
    
        
        