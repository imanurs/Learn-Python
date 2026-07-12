#%%
print('Python Documentation: https://docs.python.org/3/library/functions.html')

#ini buat import image. pake library Pillow
from PIL import Image
img = Image.open(r'D:\TECH\VS Code Projects\(Learn) Python\Learning Python\2_variables_built-in-functions\built-in-functions.jpg')
img.show()

#Variables in Python
#ini udah masuk ke variable. jadi nama variablenya tuh 'first_name', 'country', etc.. 
#datanya 'Ima', 'Indonesia' etc.. kalo datanya ganti, ntar pas dishow/manggil variablenya, yg muncul juga ganti

first_name = 'Ima'
last_name = 'S'
country = 'Indonesia'
city = 'Bandung'
age = 250                                                        #kalo int ga perlu pake petik
is_married = True                                                #boolean. valuenya True atau False. 
                                                                 #ini buat ngeevaluasi value. misal value 10 < 5, ntar hasilnya False
                                                                 #buat ngevalidasi gt sih. iya atau tidak. benar atau salah. gitu
skills = ['Management', 'Data', 'Design', 'Cloud', 'Python']     #list
person_info = {                                                  #dict - dictionary. valuenya bisa diganti2 kok
    'firstname': 'Ima',
    'lastname': 'S',
    'country': 'Indonesia',
    'city': 'Bandung'
}


#ini buat ngeprint variables di atas tadi dan ngeprint data variablenya
#biar tau isinya apa tanpa repot2 ngecheck kode dulu lol

print('\n')
print('Printing the values stored in the variables \n')

print('First name:', first_name)
print('First name length:', len(first_name))    

#len ini build in fuction. buat ngitung panjang data
#kalo datanya string kaya data first_name, brt ngitung jumlah hurufnya

print('Last Name: ', last_name)
print('Last Name Length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Number of Skills:', len(skills))                     #list kalo diprint selalu muncul kurung kok []
print('Person Information: ', person_info)
print('Number of Person Information:', len(person_info))    #list kalo diprint selalu muncul kurung kok []
print(type(person_info))                                    #mau liat type datanya apaan

print('\n')
print('Declaring multiple variables in one line \n')

first_name, last_name, country, age, is_married = 'Ima', 'S', 'Norway', 45, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

print('\n')
print('python tuh sequential. di awal gw declare value country indo, trus diakhir gw declare lagi norway')
print('yg di awal tetep keprint (sebelum declare value baru), dan yg value baru juga keprint abis declaration baru')
 # %%
