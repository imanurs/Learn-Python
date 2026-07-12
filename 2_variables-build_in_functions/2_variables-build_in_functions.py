#%%
print('Python Documentation: https://docs.python.org/3/library/functions.html')

from PIL import Image
img = Image.open(r'D:\TECH\VS Code Projects\(Learn) Python\30DaysOfPython\day2_variables-build_in_functions\build_in_functions.jpg')
img.show()

# Variables in Python

first_name = 'Ima'
last_name = 'S'
country = 'Indonesia'
city = 'Bandung'
age = 250
is_married = True
skills = ['Management', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Ima',
    'lastname': 'S',
    'country': 'Indonesia',
    'city': 'Bandung'
}

print('\n')
print('Printing the values stored in the variables \n')

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

print('\n')
print('Declaring multiple variables in one line \n')

first_name, last_name, country, age, is_married = 'Ima', 'S', 'Indonesia', 45, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
# %%
