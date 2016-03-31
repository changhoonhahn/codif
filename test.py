from codif import notif
from codif import _MakeCred 


username = raw_input("Type in e-mail address: ")
confirm = raw_input("Is your email address "+username+"? [y/n]") 
if confirm == 'y': 
    pass
else: 
    username = raw_input("Type in e-mail address: ")
    confirm = raw_input("Is your email address "+username+"? [y/n]") 

password = raw_input("Type in password: ")

#_MakeCred('changs.code@gmail.com', 'Changh37')
_MakeCred(username, password)
notif(subject='testing')
