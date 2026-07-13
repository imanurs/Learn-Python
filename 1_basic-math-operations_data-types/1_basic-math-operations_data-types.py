# %%
# Excercise 1
# Check the python version you are using (Python 3.14.4)

# Open the python interactive shell and do the following operations. The operands are 3 and 4
print(3 + 4)             # addition(+)
print(3 - 4)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(3 / 4)             # division(/)
print(3 ** 4)            # exponential(**) --> ini pangkat, alias 3 pangkat 4. jadi 3x3x3x3 = 81
print(3 % 4)             # modulus(%)  --> ini nyari modulo, alias sisa pembagian
print(3 // 4)            # floor division operator(//) ---> ini nyari pembagian trus dibuletin ke bilangan bulat terdekat

# Write strings on the python interactive shell. The strings are the following
print('Ima')             #name
print('Indonesia')       #country
print('I am really enjoying learning Python')

# Exercise 2
print('\n Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.\n')
# Check the data types of the following data:
print(type(10))                                 #int - integer. bilangan
print(type(9.8))                                #float - decimal ato pecahan
print(type(3.14))                               #float - decimal ato pecahan
print(type(4 - 4j))                             #complex - campuran bilangan bulat & imajiner
print(type(['Ima', 'Python', 'Indonesia']))     #list - isinya multiple items
print(type('Ima'))                              #str - string. huruf
print(type(True))                               #bool - boolean. true atau false aja
print(type({'name':'Ima', 'hobby':'Drawing'}))  #dict - dictionary
print(type(('Earth', 'Jupiter', 'Neptune')))    #tuple - kaya list tapi ngga bisa diubah. cocok buat data yg udah pakem/fixed
print(type({1.32, 4, 2.54, 3.14}))              #set - collection of data kaya dict sama list, tapi ini ngga berurutan
print(type(zip([1,2],[3,4])))                   #zip - built in buat ngegabungin bbrp list jadi pasangan. pasangannya berdasarkan urutan index

# Exercise 2
print('\n Find an Euclidean distance between (2, 3) and (10, 8)')
