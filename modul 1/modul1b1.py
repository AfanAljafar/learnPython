class Bio:
    
    def __init__(self):
        self.name = input("enter name : ")
        self.clas = input("enter class : ")
        self.faculty = input("enter faculty : ")
        self.study = input("enter program study of faculty : ")
    
    def DisplayBio (self):
        print('your bio')
        print('the name', self.name, 'class', self.clas, 'faculty', self.faculty,'study',self.study)

bio1 = Bio()
bio1.DisplayBio()
