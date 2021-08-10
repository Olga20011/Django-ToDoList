class Student{
    constructor(name,age,nationality){
        this.name=name,
        this.age=age,
        this.nationality=nationality


    }
    welcome(height){
        console.log( `Hello ${this.name} of ${this.age}years old ,your height is ${height}`)
    }
    set setName(newName){
        this.name=newName
        return this.name
    }
    get getName(){
        console.log(this.name)
    }
}
let student=new Student("Olga",20,"Ugandan")

console.log(student.name)
student.setName="Vickie"
student.getName
// student.welcome(12);

class Fresher extends Student{
constructor(name,age,nationality,gender){
    super(name,age,nationality)
    this.gender=gender
}
}
let fresher= new Fresher("lkif",45,"lokijhgfd","female")
fresher.welcome(15)

let laptops=true;
let promise =new Promise((resolve,reject)=>{
    if(laptops){
     let result="We get laptops"
     resolve(result)

    }else{
      let  answer=new Error ("You dont have a laptop")
        reject(answer)
    }

})
.then((result)=>{
    console.log(result)
})
.catch((error)=>{
    console.log(error)
})
.finally(()=>{
    console.log("we get to go home")
})