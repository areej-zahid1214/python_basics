class software():
    def modal(self):
        print("What modal of software is avaible?")
class laptop(software):
    def colour(self):
        print("colour of laptop is black")  
class computer(laptop): 
      def weight(self):
       print("weight of computer is 25 kg")     
s=computer()
s.weight()
s.modal()
s.colour()            