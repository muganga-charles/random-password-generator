#creating of a password
import random
lower_case="abdcefghijklmnopqstuvwxyz"#lowercase letters
upper_case="ABCDEFGHILKLMNOPQRSTUVWXYZ"#uppercase latters
numbers="0123456789"#numeric values
symbols="@#$%&*?\/"#sybols
user_for=lower_case+upper_case+numbers+symbols#combines from any of the listed categories
length=8#definining the length of the password
password="".join(random.sample(user_for,length))#this randomly gets the characters with a given length
print("The password is",password)#gives the out put(password)