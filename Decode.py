import base64
import csv
import sys
import pandas as pd

class decript(object):
    def __init__(self):
        file = r'C:\Users\Kelvin\Desktop\Python\Encrypt_pass_user\passwords.csv'
        print('hello looking for ur username/passwrod enter the site')
        print('these are the current sites I currently have:')
        data = pd.read_csv(file)
        site_li = list(data['site'])
        print(site_li)
        self.sitename = str(input('site:'))

    def search_4_value(self,filename = 'passwords.csv'): # deafult file
        row = []
        key = self.sitename
        with open(filename,'r') as file:
            for line in file:
                if key in line:
                    #row=line.rstrip()
                   # li = row.split(',')
                   # print(line)
                    row.append(line.rstrip())
                else:
                    print('{} is not found'.format(key))
                    sys.exit()
        return row
    def display(self):
        print('I have the current information for the following site')


    def decode_v(self,value):
                coded_pass = value
                pas_64byte = coded_pass.encode('ascii')
                pass_byte =base64.b64decode(pas_64byte)
                password = pass_byte.decode('ascii')
                return password

    def wht_to_decode(self,row):
        if len(row) >1:
            pass
        print('what u want to decode')
        ans = int(input('1.username,2.passowrd:'))
        if ans == 1:
            value = row[1]
            return value
        if ans == 2:
            value = row[2]
            return value
        else:
            print('error resting program')
            exit()
            return False

def main():
    import pandas as pd
    filename = 'passwords.csv'
    k = decript()
    c=k.search_4_value(filename)
    if len(c) > 1:
        print('found {} results select which one to decode'.format(len(c)))
        ans = int(input('number:'))
        if ans <= len(c):
            row = c[ans-1]
            li=row.split(',')
            h=k.wht_to_decode(li)
            e=k.decode_v(h)
            print(e)
        else:
            print('error')

    else :
        row=c[0].split(',')
        h=k.wht_to_decode(row)
        print('do u want to decode the usename/password')
        ans = input('Yes/No:')
        if ans == 'Yes':
            e=k.decode_v(h)
            print(e)
        elif ans == 'No':
            print('system closing')
            sys.exit()
        else:
            print('unknown value entered system closing')
            sys.exit()

if __name__ == "__main__":
            main()
  
