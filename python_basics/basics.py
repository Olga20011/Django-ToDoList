print(f"Twinkle ,twinkle ,little stars, \n\t How i wounder what you are! \n\t\t Up above the world so high \n\t\t Like a diamond in the sky ")

x=[1,2,3,4,5,6,7,8,10]
print(sum(x))

def multiply(list):
    total=1
    for i in list:
        total=total*i
    return total    
x=[1,2,3,4,5,6,7,8,9,10]
print(multiply(x))

def same_words(list):
    count=0
    for i in list:
        if len(i)>=2 and i[0]==i[-1]:
            count+=1 
    return count        
Sample = ['abc', 'xyz', 'aba', '1221']
print(same_words(Sample))

a={6,7,8,9,10}
b={5,6,7,8,9}
a.add (4)
print(a)
b.add (3)
print(b)

x=range(2020,2070)
for i in x:
    if i%4==0:
        print("leap year")
    else:
        print(i)    

y=range(1000,2000)
for x in y:
    if x%7==0 and x%5 !=0:
        print(x)
        
class Rectangle:
    def __init__(self, width,length):
        self.width=width
        self.length=length

    def area(self):
        A= self.width *self.length 
        return A

    def perimeter(self):
        P=2*(self.length+self.width)
        return P
   
rectangle1 = Rectangle(23,20) 
print(rectangle1.area())
print(rectangle1.perimeter())

# A function that flattens the list
def nums():
    y=[]
    x=[[1,2],[3,4],[4,5]]
    for i in x:
        for num in i:
            print(num)
            y.append(num)
    print(y)  
nums()
