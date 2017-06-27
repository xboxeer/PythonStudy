import person
import car
import cycle
myPerson=person.person("elendil")
myDoctor=person.Doctor("Elendil")
myLawyer=person.Lawyer("Elendil")
print(myPerson.name)
print(myDoctor.name)
print(myLawyer.name)
myCar=car.car()
myCar.exclaim()
myYogoCar=car.Yugo()
myYogoCar.exclaim()
myYogoCar.push()
myEmailPerson=person.EmailPerson("elendil","zy4182@sina.com")
print(myEmailPerson.name)
print(myEmailPerson.email)
car.car.exclaim(myCar)
myDuck=person.Duck("Elendil Zheng")
print(myDuck.name)
myDuck.name="Zheng Elendil"
print(myDuck.name)
myCycle=cycle.cycle(10)
print(myCycle.diameter)
myCycle.diameter=10
print(myCycle.diameter)
print(myCycle.radius)
#Hack to visit private variable
print(myCycle._cycle__radius)
