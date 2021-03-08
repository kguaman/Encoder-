'''
basic encryption not relaible for realworld application
can be 'hacked easily'

look into algrothims for encryption like the
module cryptography and paalib
'''
class Password_encription(object):
    def __init__(self):
        self.site = None
        self.username = None
        self.password =  None
        print('enter password and username')
        self.site = str(input('site:'))
        self.username = input('username:')
        self.password = input('password:')


    def _display(self):
        print('site\n',self.site,'password\n',self.password,'\nusername\n',self.username)

    def _site(self):
        return self.site

    def username_encode(self):
        user = self.username
        user_byte = user.encode('ascii')
        pas_64byte = base64.b64encode(user_byte) # ex: input-> hello output ->b'aGVsbG8=
        user_enc = pas_64byte.decode('ascii') #output -> aGVsbG8=
        print('encode username:', user_enc)
        return user_enc

    def encode(self):
        password = self.password
        #change string to acii / byte like object
        pass_byte = password.encode('ascii')
        pas_64byte = base64.b64encode(pass_byte) # ex: input-> hello output ->b'aGVsbG8=
        pas_64mess = pas_64byte.decode('ascii') #output -> aGVsbG8=
        print('encode password:', pas_64mess)
        return pas_64mess




n = Password_encription()
name=n._site()
User = n.username_encode()
cryptied= n.encode()
encry_file = 'passwords.csv'

with open(encry_file,'a') as files:
    files.write(name+',')
    files.write(User+',')
    files.write(cryptied+'\n')

files.close()
#n.decode()
