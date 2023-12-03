# Exercise no. 
num = 'Thirty'
d_y = 'Days'
_of = 'Of'
course = 'python'
space = ' '
single_string =  num + space + d_y + space + _of + space + course
print(single_string)

# Exercise no.2
x1 = 'Coding'
x2 = 'For'
x3 = 'All'
space = ' '
single_string = x1 + space + x2 + space + x3
print(single_string)

company = 'Coding For All' #declaring variable
print(company) # No. 4
print(len(company)) # no. 5
print(company.upper()) # no. 6
print (company.lower()) # no.7
print(company.capitalize()) #no. 8
print(company.title()) #no. 8
print(company.swapcase()) # no. 8
print(company.strip('Coding')) # no. 9
print(company.startswith('Coding')) # no. 10
print((company.replace('Coding','python'))) # no. 11

string = 'Python for Everyone' # no. 12 (declaring string)
print((string.replace('Everyone','All'))) #changing string
# splitting words no. 13
print(company.split())
   
company_names = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company_names.split(',')) # no.14

# no. 15 first index
first_index = company[0]
print(first_index)

# no. 16 last index
last_index = company[-1]
print(last_index)

#no. 17
index_10 = company[10]
print(index_10)

# no. 18
String = 'Python For Everyone'
pfe = String[0:13:7]
print(pfe)
      
# no. 19
string2 = 'Coding For All'
acronym = string2[0:12:7]
print(acronym)

# no. 20 finding index of 'C'
string_index = 'C'
print(string2.index(string_index)) 
   
# no. 21 finding index of 'F'
string_index = 'F'
print(string2.index(string_index))

#no. 22 using rfind
print(string2.rfind('l'))

# no.23 finding the occurrence of 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(sentence.index(sub_string))

# no. 24 using rindex to find the position of the last occurrence of because
print(sentence.rindex(sub_string))

# no. 25 slicing because because because
sub_slice = sentence[31:54]
print(sub_slice)

# no. 26 finding 1st occurrence of because
print(sentence.find('because'))

# no. 27 slicing because because because
sub_slice = sentence[31:54]
print(sub_slice)

# no 28 the answer is NO

#NO. 29 The answer is NO

# NO. 30   

# NO 31 ANSWER: (thirty_days_of_python RETURN) VALID VARIABLE NAME

# NO. 32 USING .joint
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(python_libraries) 
print(result)

# NO. 33
print('I am enjoying this challenge. \n I just wonder what is next.')

# no. 34 using  Tab '\t'
print('Name\t\tAge\tCountry\tCity')   
print('Asabeneh\t250\tFinland\tHelsinki')

# no.35 using string formatting method
radius = 10
area = 3.14 * radius ** 2
formatting_string = 'The area of a circle with {} is {} meters square'.format(radius,area)
print(formatting_string)

#using string formatting method
x = 8
y = 6
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{x} * {y} = { x * y}')
print(f'{x} / {y} ={ x / y:.2f}')
print(f'{x} % {y} = { x % y}')
print(f'{x} // {y} = {x // y}')
print(f'{x} ** {y} ={x ** y}')
