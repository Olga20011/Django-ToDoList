import os

class Budget:
    def __init__(self,name):
        self.name=name

    def budget(self):

        print("The program uses a 50-20-30 method of budgeting, Do you want to save or spend ?")
        print(int(input(f"How much do you want to budget for ?")))
        # return f"Lets get started"
        # try:
        #     0+int
        # except TypeError:
        #     print(f"The amount must be in figures") 
        # if int <800:
        #     print(f"Amount must be greater than {int} for easy budgeting " )   
        # else:
        #     return f"Your total amount is {int}"

    def main(self): 
        print ("Enter 1 for save and 2 for spend")
        input()
        choice=["save","spend"]
        for i in choice:
            if choice==1:
                print("save")
            elif choice==2:
                print ("spend")
            else:
                quit  
                      

    def saving(self):
        options=int(input("What percentage do you want to save \n1) 20% \n2) 30%"))
        if options==1:
            self.Saving=0.2
        elif options==2:        
            self.Saving=0.3 
        else:
            print( f"Please select 1 or 2")
        return f'You are saving '    
            
               
    
buget1=Budget("salary")
# buget1.main() 
# buget1.budget()
buget1.main() 
# buget1.saving()  
 

    

    

        