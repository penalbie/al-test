import random

class pwdcipher():
     def __init__(self):
        self.alphabet=['a','b','c','d',
                  'e','f','g','h',
                  'i','j','k','l',
                  'm','n','o','p',
                  'q','r','s','t',
                  'u','v','w','x',
                  'y','z']
     def pwd(self):         
          w=pwdcipher()         
          w.shuffle(self.alphabet)
          pwd=""
          num=""
          for i in range(0,5):
             x1=random.randint(0,9)
             pwd+=self.alphabet[i]
             num+=str(x1)            
          pwd=pwd+num
          print(pwd)

     def shuffle(self,alpha):
        shuffled_alphabet=[] 
        random.seed(random.seed(15))
        shuffled_alphabet=random.shuffle(alpha) 
        return shuffled_alphabet     
w=pwdcipher()
w.pwd()
