// spread operator(...) ,expands arrays and object literals into individual elements
function names(){
    let x=["Akello","Olga","Esther"]
    console.log(...x)
}
names()

// for ..of loop iterates items of an array
function toolbox(){
    const metals=["Hammer","nails","iron sheets",]
    for (const metals in toolbox);
    console.log(metals)
}
toolbox()

// include() is a case sensitive method used to findout if an element exists in a collections of elements
// It returns true or false
function cars(){
    let car=["benz","BMW","ferrari","land cruiser"];
    let findcar=car.includes("BMW");
    console.log(findcar)
}
cars()

// some() checks the presence of elements in an array only that the arguement is a function not a string
// IT DIDNT RUN
function age(){
   let x= [13,14,15,16,17,18];
  x.some((age)=>age >=18); 
}
age()
//  the filter ()methods picks the items that confirm the conditions inthe function and puts the in a new array
//  IT DIDNT RUN

let prices=[30,40,45,20,25, 35];
let newprices=  prices.filter((shop)=> shop>=30);
    prices.map((shop)=> shop*25 )

//  The map () method return items in a new array when are modified
// IT DIDNT RUN
function money(){
    const weeklyExpenses=[3000,2000,40000,3000];
    weeklyExpenses.reduce((first,last)=>first+last);
}
money()



