class Student{
    constructor(name,age,country,date_of_birth){
        this.name=name,
        this.age=age,
        this.country=country,
        this.date_of_birth=date_of_birth
    }
    Introduction(){
        console.log(`My name is ${this.name},I am from ${this.country} and I am ${this.age} years old.I was borth in ${this.date_of_birth}`)
    }
    set setName(newName){
        this.name=newName;
        return this.name
    }
    get (){
        console.log(this.name)

    }
    // residence(room){
    //     return 
    // }
}

let student= new Student("Olga",20,"Uganda","14,03,2001")
let student1=new Student("Faith",20,"Kenya","15,05,2001")
let student2=new Student("Vickie",21,"Kenya","13,01,2000")
console.log(student.name)
console.log(student1.name)
student1.setName="Joy"
student.get
console.log(student1.name)

class Sickly extends Student{
    constructor(name,age,country,date_of_birth,health_status){
        super(name,age,country,date_of_birth)
        this.health_status
    }
    ulcers(country){
        let newUlcers =this.Student.find(newUlcers=>newUlcers.country==country),
        return newUlcers
}
// let student3=new Student("Akello",21,"Rwanda","04,06,1998")
// console.log(Student.ulcers("Kenya"));
