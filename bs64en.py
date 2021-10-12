
import base64

class bs:

    def bs64(self, a):
        try:
            self.file = a.replace('.','_en64.')
            with open(a, 'r') as r:
                self.__en64 = base64.b64encode(bytes(r.read(), encoding='utf8'))
                with open(self.file,'w') as w:
                    w.write(f'''
import base64
exec(base64.b64decode({self.__en64}))
                         ''')
                    w.close()
                    print (f'[√] saved {self.file}')

        except FileNotFoundError:
            print ('[!] Check your file')
            pass
    def bs32(self, b):
        try:
            self.file = b.replace('.','_en32.')
            with open(b,'r') as r:
                self.__en32 = base64.b32encode(bytes(r.read(), encoding='utf8'))
                with open(self.file,'w') as w:
                    w.write(f'''
import base64
exec(base64.b32decode({self.__en32}))
                         ''')
                    w.close()
                    print (f'[√] saved {self.file}')

        except FileNotFoundError:
            print('[!]Check your file')
            pass
    
    def b85(self, c):
        try:
            self.file = c.replace('.','_en85.')
            with open(c, 'r') as r:
                self.__en85 = base64.b85encode(bytes(r.read(), encoding='utf8'))
                with open(self.file,'w') as w:
                    w.write(f'''
import base64
exec(base64.b85decode({self.__en85}))
                        ''')
                    w.close()
                    print (f'[√] saved {self.file}')

        except FileNotFoundError:
            print ('[!]Check your file')
            pass

    def b16(self, d):
        try:
            self.file = d.replace('.','_en16.')
            with open(d,'r') as r:
                self.__en16 = base64.b16encode(bytes(r.read(), encoding='utf8'))
                with open(self.file,'w') as w:
                    w.write(f'''
import base64
exec(base64.b16decode({self.__en16}))
                        ''')
                    w.close
                    print (f'[√] saved {self.file}')

        except FileNotFoundError:
            print('[!]Check your file')
            pass




if __name__=='__main__':
    def call():
        inti = ['your file want encrypted: ']
        banner = [""""
B a s e - 6 4
 E n c o d e 
   F i l e  
   
1. encrypted in b64
2. encrypted in b32
3. encrypted in b85
4. encrypted in b16

'type exit for kill this tools'
                   """];print(banner[0])
        while True:
            masukan = input('choose your likes: ')
            if masukan == '1':
                inp = input(inti[0])
                bs().bs64(inp)
                exit()
            elif masukan == '2':
                xx = input(inti[0])
                bs().bs32(xx)
                exit()
            elif masukan == '3':
                yy = input(inti[0])
                bs().b85(yy)
                exit()
            elif masukan == '4':
                oo = input(inti[0])
                bs().b16(oo)
                exit()
            elif 'exit' in masukan:
                print ('[program finished]')
                exit()
            else:
                pass
    call()


