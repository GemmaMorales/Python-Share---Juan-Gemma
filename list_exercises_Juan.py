--01.1-----------------------------------------

my_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
# 1. print the item here
print(my_list[4])
# 2. change the position were 'thursday' is to None
my_list[4] = None
print(my_list[4])
# 3. print that position now here
print(my_list[2])

extra info:---------------------------

my_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
# 1. print the item here
print(my_list[4])
# 2. change the position were 'thursday' is to None
my_list[4] = None
# 3. printing 3rd. element
print(my_list[2])
#list elementes form right to left (-1 is the last element)
print(my_list[-1])
# printing the updated list
print(my_list)


--01.2------------------------------------------
my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45,3,100,4,56,23]
# Print in the console the 1st element on the list
print(my_list[0])
# Print in the console the 4th element on the list
print(my_list[3])

--01.3------------------------------------------
# import the random package here "import random"
import random

def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)

    for i in range(randonlength):
        aux_list.append(randonlength)
        i += i
    return aux_list
my_stupid_list = generate_random_list()

# Feel happy to write the code below this comment, good luck!:
the_last_one = my_stupid_list[-1]
print(the_last_one)

--01.4------------------------------------------
#Remember import random function here:
import random
my_list = [4,5,734,43,45]
#The magic is here:
for i in range(10):
    my_list.append(random.randrange(100))

print(my_list)

#profersor solution

import random
my_list = [4,5,734,43,45]
#The magic is here:
for i in range(10):
    my_list.append(random.randint(0, 100))

print(my_list)

--01.5------------------------------------------

# Your code here, have fun:
for i in range(1,18):
    print(i)

--02------------------------------------------
my_list = [232,32,1,4,55,4,3,32,3,24,5,5,5,34,2,35,5365743,52,34,3,55]
#Your code go here:
for i in range(len(my_list)):
   print(my_list[i])

--02.1------------------------------------------

my_sample_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]
# The magic pass below:
# Create a variable, like "i", that uses the last index position in the array "my_sample_list". Remember we can access the length property of an array using len, and that the position will always be 1 less than the item number (item one is index 0, item 5653 would be one less...) 
# You can now use the variable holding the last position to iterate until you get to the first position- which will always be 0. Create a for loop using that variable, make sure the value of the variable is modified on each iteration of the loop.
# while some_variable_reference > 0:
#     print(my_sample_list[some_variable_reference])
#     chage after doing what we wanted, change the variables value so that the next pass it references the new index position
#for i in range(len(my_sample_list)):
# or:  :)
for i in range(1, ((len(my_sample_list)))+1):
    print(my_sample_list[-i])

    # professor solution

for i in range(len(my_sample_list)-1, -1, -1):
    print(my_sample_list[i])

    # professor solution sing while

    i = len(my_sample_list)-1
    while i >=0:
    	print(my_sample_list[i])
    	i -= 1



--02.2------------------------------------------

my_sample_list= [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]
#your code go below of this line, nothing change above:
for i in range(0, len(my_sample_list), 2):
    print(my_sample_list[i])

--02.3------------------------------------------

my_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]
#Your code here:
inicialValue = 7
stopValue = 14
increaseValue = 1

for i in range(inicialValue, stopValue):
    if i == my_list[i]:
        i += increaseValue
    print(my_list[i])
--02.4------------------------------------------

my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']
#Your code here:
my_sample_list[1]= 'Steven'
my_sample_list[-1]= 'Pepe'
my_sample_list[0]=my_sample_list[2]+my_sample_list[4]

for i in range(1, ((len(my_sample_list)))+1):
    print(my_sample_list[-i])
--02.5------------------------------------------

people = [ 'Lebron','Aaliyah','Diamond','Dominique','Aliyah','Jazmin','Darnell','Hatfield','Hawkins','Hayden','Hayes','Haynes','Hays','Head','Heath','Hebert','Henderson','Hendricks','Hendrix','Henry','Hensley','Henson','Herman','Hernandez','Herrera','Herring','Hess','Hester','Hewitt','Hickman','Hicks','Higgins','Hill','Hines','Hinton','Hobbs','Hodge','Hodges','Hoffman','Hogan','Holcomb','Holden','Holder','Holland','Holloway','Holman','Holmes','Holt','Hood','Hooper','Hoover','Hopkins','Hopper','Horn','Horne','Horton','House','Houston','Howard','Howe','Howell','Hubbard','Huber','Hudson','Huff','Wally','Hughes','Hull','Humphrey','Hunt','Hunter','Hurley','Hurst','Hutchinson','Hyde','Ingram','Irwin','Jackson','Jacobs','Jacobson','James','Jarvis','Jefferson','Jenkins','Jennings','Jensen','Jimenez','Johns','Johnson','Johnston','Jones','Jordan','Joseph','Joyce','Joyner','Juarez','Justice','Kane','Kaufman','Keith','Keller','Kelley','Kelly','Kemp','Kennedy','Kent','Kerr','Key','Kidd','Kim','King','Kinney','Kirby','Kirk','Kirkland','Klein','Kline','Knapp','Knight','Knowles','Knox','Koch','Kramer','Lamb','Lambert','Lancaster','Landry','Lane','Lang','Langley','Lara','Larsen','Larson','Lawrence','Lawson','Le','Leach','Leblanc','Lee','Leon','Leonard','Lester','Levine','Levy','Lewis','Lindsay','Lindsey','Little','Livingston','Lloyd','Logan','Long','Lopez','Lott','Love','Lowe','Lowery','Lucas','Luna','Lynch','Lynn','Lyons','Macdonald','Macias','Mack','Madden','Maddox','Maldonado','Malone','Mann','Manning','Marks','Marquez','Marsh','Marshall','Martin','Martinez','Mason','Massey','Mathews','Mathis','Matthews','Maxwell','May','Mayer','Maynard','Mayo','Mays','Mcbride','Mccall','Mccarthy','Mccarty','Mcclain','Mcclure','Mcconnell','Mccormick','Mccoy','Mccray','Wally','Mcdaniel','Mcdonald','Mcdowell','Mcfadden','Mcfarland','Mcgee','Mcgowan','Mcguire','Mcintosh','Mcintyre','Mckay','Mckee','Mckenzie','Mckinney','Mcknight','Mclaughlin','Mclean','Mcleod','Mcmahon','Mcmillan','Mcneil','Mcpherson','Meadows','Medina','Mejia','Melendez','Melton','Mendez','Mendoza','Mercado','Mercer','Merrill','Merritt','Meyer','Meyers','Michael','Middleton','Miles','Miller','Mills','Miranda','Mitchell','Molina','Monroe','Lucas','Jake','Scott','Amy','Molly','Hannah','Lucas']
#Your code here:
name = "Wally"
for i in range(len(people)):
    if people[i] == name:
        print(i)


--02.6------------------------------------------
par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"
#counts = {}
#your code go here:
x = par.count("a")
y = par.count("A")
print(x+y)
#print(counts)

#update professor solution form descktop prints

par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"
par = par.replace(" ","").lower() #replace espaces " " with no espaces "", and put everything in lowercase (lower) // replace and lower are methods of python.
counts = {}
#print(counts) #
#your code go here:
for i in par:
	if i not in counts.key():
		counts[i] = 1
		#print(counts)
	else:
		counts[i] += 1
		#the above line means:  
		#counts[i] = counts[i] + 1
		print(counts)

--03------------------------------------------

arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
new_list = []
for i in range(1, ((len(arr)))+1):
    new_list.append(arr[-i])
    
print(new_list)


--04------------------------------------------

mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below:
for i in range(len(mix)):
    x = mix[i]
    print(type(x))


    # other 
    # Your code below:
for x in mix:
#for i in range(len(mix)):
    #x = mix[i]
    print(type(x))

--04.1------------------------------------------


my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello = []
for i in my_list:
    if isinstance(i, dict) == True:
        hello.append(i)
        
        
print(hello)


my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:
hello = []
for i in my_list:
    if isinstance(i, (dict ,list)) == True:
        
        hello.append(i)
        
        
print(hello)

# other way

my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:
hello = []
for i in my_list:
    if type(i) == list or type(i) == dict:
        
        hello.append(i)
        
print(hello)

--05------------------------------------------

my_sample_list = [3423,5,4,47889,654,8,867543,23,48,5345,234,6,78,54,23,67,3,6,432,55,23,25,12]


def sum_all_values(items):
    total= 0  #this is an auxiliar variable
    #The magic happens here:
    for i in range(len(items)):
        total = items[i] + total 

    return total
print(sum_all_values(my_sample_list))

--06------------------------------------------
my_list = [3344,34334,454543,342534,4563456,3445,23455,234,262,2335,43323,4356,345,4545,452,345,434,36,345,4334,5454,345,4352,23,365,345,47,63,425,6578759,768,834,754,35,32,445,453456,56,7536867,3884526,4234,35353245,53244523,566785,7547,743,4324,523472634,26665,63432,54645,32,453625,7568,5669576,754,64356,542644,35,243,371,3251,351223,13231243,734,856,56,53,234342,56,545343]


for numb in my_list:
    #the magic go here:
    if numb%14==0:
        print(numb)

--06.1------------------------------------------

my_list = [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 1 ]

def my_function(numbers):
    new_list = []
    for numb in numbers:
        if numb == 1:
            new_list.append(numb)
        if numb == 0:
            new_list.append("Yahoo")
    return new_list

print(my_function(my_list))

--07------------------------------------------

x = 20
while x >= 0:
  if x==0:
    print("LIFTOFF")
  elif x%5==0:
        print(str(x) + "!")
  else:
        print(x)
  x -= 1
  
--08------------------------------------------

people = ['juan','ana','michelle','daniella','stefany','lucy','barak']
#Your code go here:
def deletePerson(person_name):
    new_list = []
    for x in people:
        new_list = new_list +[x]
    if person_name in new_list:
       new_list.remove(person_name)
    return new_list

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))
--08.1------------------------------------------
chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    new_list=[]
    new_list = list1 + list2
    
    return new_list
    
print(merge_list(chunk_one, chunk_two))

#NOTES: also works// create a loop to insert in list1 every element of second list one by one
#for x in list2:
    #new_list = list1 + [x]
    #list1 = new_list

--08.2------------------------------------------
list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]
#list_of_numbers = [1,2,33,10,20,4]
#Your code here:
def mergetwolist(insert_a_list):
    odd = []
    even = []
    merged_list =[]
    for numb in insert_a_list:
        if numb%2!=0:
           odd.append(numb)
        if numb%2==0:
           even.append(numb)
         
    merged_list = odd+even   
    return merged_list
print(mergetwolist(list_of_numbers))


--09------------------------------------------
my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]


#Your code go from here:
def biggest_number(list_of_numbers):
    biggest = 0
    for numb in list_of_numbers:
        if numb > biggest:
            biggest = numb
    return biggest

print(biggest_number(my_list))

--09.1------------------------------------------
my_list = [3344,34334,454543,342534,4563456,3445,23455,234,262,2335,
43323,4356,345,4545,452,345,434,36,345,4334,5454,345,4352,23,365,345,47,63,
425,6578759,768,834,754,35,32,445,453456,56,7536867,3884526,4234,35353245,53244523,
566785,7547,743,4324,523472634,26665,63432,54645,32,453625,7568,5669576,754,64356,542644,
35,243,371,3251,351223,13231243,734,856,56,53,234342,56,545343,]

#Your code here:
def smallest_number(list_of_numbers):
    biggest = 0
    smallest = 0
    for numb in list_of_numbers:
        if numb > biggest:
            biggest = numb
    smallest = biggest        
    for numb in list_of_numbers:
        if numb < smallest:
            smallest = numb
    #print("the smallest number is: " +str(smallest)+ ", and the biggest number is: " + str(biggest))            
    return smallest

print(smallest_number(my_list))

--10------------------------------------------

my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
avera = 0
items = len(my_list)

for x in my_list:
    avera = x + avera
    

avera = avera / items

print(avera)

--10.1------------------------------------------
contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:
for x, y in contact.items():
  print(x +" : "+ y)

--11------------------------------------------

coordinatesList = [[33.747252,-112.633853],[-33.867886, -63.987],[41.303921, -81.901693],[-33.350534, -71.653268]]

# Your code go here:
for i in range(len(coordinatesList)):
    print(coordinatesList[i][1])

--12------------------------------------------
Celsius_values = [-2,34,56,-10]

def fahrenheit_values(x):
    return (x * 9/5) + 32
#result = map(fahrenheit_values, Celsius_values)
#convert the map into a list, for readability: 
result = list(map(fahrenheit_values, Celsius_values))
print(result)

--12.1------------------------------------------

myNumbers = [23,234,345,4356234,243,43,56,2]

def increment_by_one(x):
    return x * 3
new_list = list(map(increment_by_one, myNumbers))
print(new_list)

--12.2------------------------------------------

names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

def prepender(name):
    return "My name is: " + name

new_list = list(map(prepender, names))
print(new_list)

--12.3------------------------------------------
list_Strings = ['1','5','45','34','343','34',6556,323]

def type_list(items):
        return type(items)

new_list = list(map(type_list, list_Strings))
print(new_list)

--12.4------------------------------------------

import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda person:  person["name"] , people))
date_list = list(map(lambda person:  person["birthDate"] , people))
age_list = list(map(calculateAge, (date_list)))
#print(age_list)
#print(name_list)
new_list =[]
for i in range(len(name_list)):
    new_list.append("Hello, my name is " +(name_list[i])+ " and I am "+str(age_list[i])+ " years old")

print(new_list)    
--12.5------------------------------------------

theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def wiki_woko(booleans):
        if booleans == 1:
            x = "wiki"
        elif booleans == 0:
            x = "woko"
        return x            

wikiwiko = list(map(wiki_woko, theBools))
print(wikiwiko)


--12.6------------------------------------------

incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:
def my_var(argument):
    transformedData = argument["name"] +" "+ argument["lastName"]
    return transformedData

full_name = list(map(my_var, incomingAJAXData))
print(full_name)

--13------------------------------------------

allNumbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]


def filter_function(items):
    #return items % 2 ==0
    return items > 10
greater_than_ten = list(filter(filter_function, allNumbers))
print(greater_than_ten)

--13.1------------------------------------------

all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filter_names(names_list):
   return names_list.startswith("R")

resulting_names = list(filter(filter_names, all_names))

print(resulting_names)

--13.2------------------------------------------



--13.3------------------------------------------



--13.4------------------------------------------



--14------------------------------------------



--------------------------------------------



--------------------------------------------

--------------------------------------------

--------------------------------------------

--------------------------------------------

--------------------------------------------

--------------------------------------------


