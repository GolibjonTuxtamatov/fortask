# qavs = "()()(()())(())((()))(((()()())))"
# part_qavs = ""
# all_qavs = []
# c = 0
# a,b = 0,0
# for i in range(len(qavs)):
#     if qavs[i] == '(':
#         a+=1
#     if qavs[i]==')':
#         b+=1

#     if a==b:
#         all_qavs.append(qavs[c:i+1])
#         c=i+1
#         a=0
#         b=0


# print(all_qavs)


"================================================================================================"

# sozi = "babarrakunnukui"
# max_soz = ""
# new_soz = []
# palindrom_words = []

# for i in range(len(sozi)):
#     for j in range(i):
#         new_soz.append(sozi[j:i+1])

# for i in new_soz:
#     if i == i[::-1] and i not in palindrom_words:
#         palindrom_words.append(i)
#         if(len(i)>len(max_soz)): max_soz=i
        

# print(max_soz)


"================================================================================================"

# qavs = "()()(()())(())))"
# part_qavs = ""
# all_qavs = []
# c = 0
# a,b = 0,0
# for i in range(len(qavs)):
#     if qavs[0]=='(' and qavs[len(qavs)-1]==')' and len(qavs)%2==0:
#         if qavs[i] == '(':
#             a+=1
#         if qavs[i]==')':
#             b+=1

#         if a==b:
#             all_qavs.append(qavs[c:i+1])
#             c=i+1
#             a=0
#             b=0
#             valu = True
#         else:valu = False
#     else:valu=False;print(qavs,valu)
# print(all_qavs,valu)

"================================================================================================"

# def sumNumLength(son):
#     son = str(son)
#     sum = 0
#     for i in son:
#         sum+=int(i)
    
#     if sum==7:
#         return 1




# lst = [234,4,3,5676,34,7,436,52,214,5]
# new_lst = []

# for i in lst:
#     if len(str(i))>1 and sumNumLength(i):
#         new_lst.append(i)

# print(new_lst)

"================================================================================================"

# son = int(input("nechta son kiritasiz: "))
# lst = []
# for i in range(son):
#     lst.append(int(input("son: ")))


# print(lst)
"================================================================================================"

# lst = [1,2,3,4,5,5,4,3,2,1]

# def  bolibBer(lst):
#     part_lst = []
#     all_lst = []
#     for i in lst:
#         part_lst.append(i)
#         if len(part_lst) == len(lst)//2 and len(all_lst)==0:
#             all_lst.append(part_lst)
#             part_lst = []
#     if len(all_lst[0])!=len(part_lst):
#         all_lst.append([part_lst[0]])
#         part_lst.pop(0)
#     if len(part_lst)>0:
#         all_lst.append(part_lst)

#     return all_lst

# all_lst = bolibBer(lst)

# if sum(all_lst[0]) < sum(all_lst[len(all_lst)-1]):
#     all_lst[0] = all_lst[len(all_lst)-1]
# elif sum(all_lst[0]) > sum(all_lst[len(all_lst)-1]):
#     all_lst[len(all_lst)-1] = all_lst[0]
# else:pass     
# print(all_lst)

"================================================================================================"

# def convert_morze(word):
#     word = word.upper()
#     char_to_dots = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#     '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#     '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#     ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#     '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
#     }


#     for i in word:
#         for j in char_to_dots:
#             if i == j:
#                 print(char_to_dots[j],end=" ")


# soz = input("Soz kiriting: ")

# convert_morze(soz)

"========================================================================================================="

# def shu(son):
#     if son>0:
#         for i in range(1,son+1):
#             print((son-i)*'_'+(i)*'#')
#     elif son<0:
#         son=-1*son
#         for i in range(son):
#             print((i)*'_'+(son-i)*'#')



# son = int(input("Son:"))

# shu(son)

"========================================================================================================="

# def input_kod():
#     kod = input("Kodni kiriting(16 atlik):")
#     lst = []
#     if len(kod)==16:
#         for i in kod:
#             lst.append(int(i))
#     else: input_kod()
#     return lst
    

# def check_valid(lst):
#     sum = 0
#     kum = 0
#     for i in range(16):
#         cum = 0
#         if i%2==1:
#             sum+=lst[i]
#         else:
#             a=lst[i]*2
#             a=str(a)
#             for j in range(len(a)):
#                 cum += int(a[j])
#             kum+=cum

#     if (sum+kum)%10==0:
#         return 'VALID'
#     else:return 'INVALID'
    

# print(check_valid(input_kod()))


"================================================================================================"

# word = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat, distinctio."

# word = word.split()
# lst = []

# for i in range(len(word)):
#     if i == len(word)-1:
#         lst.append(word[len(word)-1][0]+word[0][1:])
#     else:lst.append(word[i][0]+word[i+1][1:])

# lst.insert(0,lst[len(lst)-1])
# lst.pop(len(lst)-1)

# print(" ".join(lst))



"================================================================================================"




# def checkWordPower(word):
#     word = word.split()
#     cum = 0
#     son = 0
#     soz = ""
#     soz1 = ""
#     for i in word:
#             for j in i:
#                 if j.isalpha():
#                     cum += ord(j.upper())-64
#                     soz+=j
#                     if son<cum:
#                         soz1 = soz
#                         son = cum
                        
#             soz = ''
#             cum = 0
#     return soz1
# word = "Nancy is very pretty."
# print(checkWordPower(word))


"================================================================================================"
# from math import pow

# def checkHappy(son,lst):
#     cum = 0
#     son = str(son)
#     if int(son) not in lst and int(son)!=1:
#         for i in son:
#             cum +=pow(int(i),2)
#             son = cum
#     elif int(son)==1:
#         return True
#     elif int(son) in lst:
#         return False
#     son = int(son)       
#     lst.append(son)
#     return checkHappy(son,lst)
    

# son =3970
# lst = []
# print(checkHappy(son,lst))

"================================================================================================"

# lst = ['cow','pig','hen','cow','cow','pig','hen','cow','cow','pig','hen','cow']
# new_lst = []
# for i in lst:
#     if lst.count(i)>1 and (i+'s') not in new_lst:
#         new_lst.append(i+'s')
#     elif (i+'s') not in new_lst:new_lst.append(i)
# print(new_lst)
"================================================================================================"

# lst = ['salom bu dunyo salom',['salom','bu'],['_']]

# def changeWord(lst):

#     word = lst[0].split()
#     for i in range(len(word)):
#         if word[i] in lst[1]:
#             word[i]=len(word[i])*str(lst[2])[2:3]

#     return word

# print(' '.join(changeWord(lst)))


"================================================================================================"

# lst = [1,2,3]
# new_lst = []
# sort_lst = []
# for i in range(len(lst)):
#     for j in range(1,len(lst)+1):
#         for l in range(1,len(lst)):
#             new_lst.append(lst[i:j:l])

# for i in new_lst:
#     if i not in sort_lst:
#         sort_lst.append(i)

# for i in range(len(sort_lst)):
#     for j in range(len(sort_lst)):
#         if len(sort_lst[i])<len(sort_lst[j]):
#             sort_lst[i],sort_lst[j]=sort_lst[j],sort_lst[i]

# print(sort_lst)





    
"================================================================================================"


# lst = [1,2,4,5,6]

# for i in range(len(lst)-1):
#     if lst[i]+1==lst[i+1]:
#         bole = True
#     else:bole = False;break

# print(bole)


"================================================================================================"

# word = 'aabdsbbda'
# lst = []
# lst1 = []
# for i in word:
#     lst.append(i)
#     if i not in lst1:
#         lst1.append(i)

# for i in range(len(lst1)):
#     cnt = 1
#     a = 0
#     for j in range(len(lst)):
#         if lst1[i] == lst[j] and a>0:
#             lst[j]+=f'_{cnt}'
#             cnt+=1
#         if lst1[i] == lst[j]:
#             a+=1
    
# print(' '.join(lst))
"================================================================================================"



# def word_power(word):
#     ball_1 = ['a','e','i','o','u','l','n','s','t','r']
#     ball_2 = ['d','g']
#     ball_3 = ['b','c','m','p']
#     ball_4 = ['f','h','w','v','y']
#     ball_5 = ['k']
#     ball_8 = ['j','x']
#     ball_10 = ['q','z']
#     word = word.lower()
#     sum = 0
#     for i in word:
#         if i.isalpha():
#             if i in ball_1:
#                 sum+=1
#             elif i in ball_2:
#                 sum+=2
#             elif i in ball_3:
#                 sum+=3
#             elif i in ball_4:
#                 sum+=4
#             elif i in ball_5:
#                 sum+=5
#             elif i in ball_8:
#                 sum+=8
#             elif i in ball_10:
#                 sum+=10
#     return sum


# word = input("Soz kiriting: ")

# print(word_power(word))

"================================================================================================"

# num = int (input("Son: "))

# def is_disarium(num):
#     num = str(num)
#     sum = 0
#     for i in range(len(num)):
#         sum+=pow(int(num[i]),i+1)
    
#     if sum == int(num):
#         return True,sum
#     else: return False,sum

# print(is_disarium(num))


"================================================================================================"







# word = "Assalomu aleykum G`olibjon aka zaza"
# shifr_word = ""

# for i in word:
#     if i.isupper():
#         shifr_word+=chr(90-(ord(i)-65))
#     elif i.islower():
#         shifr_word+=chr(122-(ord(i)-97))
#     else:shifr_word+=i



# print(shifr_word)
"================================================================================================"

# son = int(input())
# lst = []
# i = 2
# while son!=1:
#     if son%i==0:
#         son//=i
#         lst.append(i)
#     else:i+=1
# print(lst)
"================================================================================================"







# lst = [2,1,2,1]

# lst.sort()
# lst.reverse()
# new_lst = []
# for i in lst:
#     part_lst = []
#     for j in lst:
#         if i == j:
#             part_lst.append(j)

#     if part_lst not in new_lst:
#         new_lst.append(part_lst)


# print(new_lst)


"================================================================================================"

#   KASR ni qisqartirish



# def kasr_num():
#     kasr = input()

#     try:

#         if kasr[0]!='-' and kasr[kasr.find('/')+1]!='-':
#             a = int(kasr[:kasr.find("/")])
#             b = int(kasr[kasr.find("/")+1:])
#         elif kasr[0]=='-' and kasr[kasr.find('/')+1]=='-':
#             a = int(kasr[1:kasr.find("/")])
#             b = int(kasr[kasr.find("/")+2:])
#             a,b = a*(-1),b*(-1)
#         elif kasr[0]=='-':
#             a = int(kasr[1:kasr.find("/")])
#             b = int(kasr[kasr.find("/")+1:])
#             a = a*(-1)
#         elif kasr[kasr.find('/')+1]=='-':
#             a = int(kasr[:kasr.find("/")])
#             b = int(kasr[kasr.find("/")+2:])
#             b = b*(-1)
        

        
#         if a<b and b%a==0 and b!=0 and a>0:
#             b//=a
#             a//=a
#             print(kasr,'-->',a,'/',b)
#         elif a>b and a%b==0 and b!=0 and b>0:
#             a//=b
#             b//=b
#             print(kasr,'-->',a)
#         elif a>b and a%b==0 and b!=0 and a>0 and b<0:
#             a//=b
#             print(kasr,'-->',a)
#         elif a<b and b%a==0 and b!=0 and b>0 and a<0:
#             b//=a
#             a//=a
#             print(kasr,'-->',a*(-1),'/',b*(-1))
#         elif a>b and b%a==0 and b!=0 and a<0 and b<0:
#             b//=a
#             a//=a
#             print(kasr,'-->',a,'/',b)
#         elif a<b and a%b==0 and b!=0 and a<0 and b<0:
#             a//=b
#             b//=b
#             print(kasr,'-->',a)
#         elif a%b!=0 and b!=0 or b%a!=0 and b!=0:
#             print(kasr,'--->',kasr)
#     except:
#         print("Iltimos (son/son) ko`rinishda kiriting")
#         kasr_num()
        

# kasr_num()



"================================================================================================"


# lst = [["1","2","3"],["4","5","6"],["7","8","9"]]

# def x_0(lst):
#     for i in lst:
#         print(i)

#     for i in range(9):
#         son1 = (input("Player1(X):"))
#         for i in range(len(lst)):
#             for j in range(len(lst)):
#                 if son1==(lst[i][j]):
#                     lst[i][j]='X'
#         for i in lst:
#             print(i)
#         for i in range(len(lst)):
#             for j in range(len(lst)):
#                 if  ((lst[0][0]== 'X' and lst[0][1]== 'X' and lst[0][2]) == 'X'
#                     or (lst[1][0]== 'X' and lst[1][1]== 'X' and lst[1][2])=='X'
#                     or (lst[2][0]== 'X' and lst[2][1]== 'X' and lst[2][2])=='X' 
#                     or (lst[0][0]== 'X' and lst[1][0]== 'X' and lst[2][0])=='X'
#                     or (lst[0][1]== 'X' and lst[1][1]== 'X' and lst[2][1])=='X' 
#                     or (lst[0][2]== 'X' and lst[1][2]== 'X' and lst[2][2])=='X' 
#                     or (lst[0][0]== 'X' and lst[1][1]== 'X' and lst[2][2])=='X'
#                     or (lst[0][2]== 'X' and lst[1][1]== 'X' and lst[2][0])=='X') :
#                     return " X wins"

#         son2 = (input("Player2(0):"))
#         for i in range(len(lst)):
#             for j in range(len(lst)):
#                 if son2==(lst[i][j]):
#                     lst[i][j]='0'
#         for i in lst:
#             print(i)
#         for i in range(len(lst)):
#             for j in range(len(lst)):
#                 if  ((lst[0][0]=='0' and lst[0][1]=='0' and lst[0][2])=='0'
#                     or (lst[1][0]=='0' and lst[1][1]=='0' and lst[1][2])=='0'
#                     or (lst[2][0]=='0' and lst[2][1]=='0' and lst[2][2])=='0' 
#                     or (lst[0][0]=='0' and lst[1][0]=='0' and lst[2][0])=='0'
#                     or (lst[0][1]=='0' and lst[1][1]=='0' and lst[2][1])=='0' 
#                     or (lst[0][2]=='0' and lst[1][2]=='0' and lst[2][2])=='0' 
#                     or (lst[0][0]=='0' and lst[1][1]=='0' and lst[2][2])=='0'
#                     or (lst[0][2] =='0'and lst[1][1]=='0' and lst[2][0])=='0') :
#                     return " 0 wins"
#     return 'Game Over'    

# print(x_0(lst))
"================================================================================================"
# son = int(input("Son: "))
# for i in range(son+1):
#     print(" "*(son-i)+" *"*i)

"================================================================================================"
# import os

# with open('users.txt','r') as fayl:
#     soz =fayl.read()

# lst = []
# son = ''
# for i in soz:
#     if i.isdigit():
#         son+=i
#     elif len(son)>0:
#         lst.append(int(son))
#         son =''

# os.system("cls")
# print(soz)
# print(lst)
"==============================================================================================="

# def num_split(num,key):
#     length = len(num)
#     lst = []
#     if key:
#         for i in range(length):
#             lst.append(int(num[i])*pow(10,length-(i+1)))
#     else:
#         for i in range(length):
#             lst.append(int(num[i])*pow(10,length-(i+1))*(-1))
#     return lst


# def num_send(num):
#     if num[0]=='-':
#         num=num[1:]
#         a = (num_split(num,0))
#     else:
#        a = num_split(num,1)
#     return a

# num = input()
# print(num_send(num))


"================================================================================================"

# plus = lambda *lst : sum(lst)

# print(plus(1,2,3,4,5,6,7,8,9))
"================================================================================================"

# dct1 = {1:2}
# dct2 = {2:3}
# dct3 = {3:4}

# all_dct = {}

# all_dct
"================================================================================================"

# arr = [(1,2),(2,3),(3,4)]
# for i in range(len(arr)):
#     arr[i]=list(arr[i])

# print(arr)
"================================================================================================"

# dct1 = {1:1}
# dct2 = {2:2}
# dct3 = {3:3}

# all_dct = {}

# lst = [dct1,dct2,dct3]
# for i in lst:
#     all_dct.update(i)

# print(all_dct)




"================================================================================================"

# dct = {
#     "men":1997,
#     "u":2003,
#     "biz":-929
# }
# summa=0
# for i in dct.values():
#     summa +=i

# print(summa)
# print(sum(dct.values()))
"================================================================================================"



# data = [
#     {
#         "model":"RDX",
#         "year":2009
#     },{
#         "model":"LS",
#         "year":2000
#     },{
#         "model":"LR2",
#         "year":2010    
#     }
# ]
# print(data)
# for i in range(len(data)):
#     for j in range(len(data)):
#         if data[i]["year"]>data[j]["year"]:
#             data[i],data[j] = data[j],data[i]


# print(data)

"================================================================================================"


# lst = [10,20,30,40,50,60]
# def check_num_sort(lst):
#     bole = bool
#     for i in range(len(lst)-1):
#         if lst[i]+10==lst[i+1]:
#             bole = True
#         else: bole = False ; return bole 
#     return bole


# print(check_num_sort(lst))
"================================================================================================"
# lst = [1,2]
# if sum(lst) == len(lst):
#     print(True)
# else:print(False)


"================================================================================================"

# lst = [1,2,3,4,1,2,3,5,1,2,3]
# def check_repate_num(lst):
#     bole = True
#     for i in range(len(lst)-1):
#         if lst[i]+1==lst[i+1] and bole:
#             continue
#         elif lst[i]%2==0 and lst[i+1]==lst[0]:
#             continue
#         else: return False
    
#     if i == len(lst):
#         return True
#     else: return False

# print(check_repate_num(lst))


"================================================================================================"


# lst = ['a','f','z']

# new_lst = [] 
# sort_lst = []
# for i in range(len(lst)):
#     for j in range(1,len(lst)+1):
#         for l in range(1,len(lst)):
#             new_lst.append(lst[i:j:l])

# for i in new_lst:
#     if i not in sort_lst:
#         sort_lst.append(i)

# for i in range(len(sort_lst)):
#     for j in range(len(sort_lst)):
#         if len(sort_lst[i])<len(sort_lst[j]):
#             sort_lst[i],sort_lst[j]=sort_lst[j],sort_lst[i]

# print(sort_lst)
"================================================================================================"


# with open("forbidden_words.txt","r") as file:
#     readed = file.read()
#     readed = readed.split()
# word = """Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
# Fugit architecto salad laudsaladantium dolorem exercitationem 
#  excepturi saepe molestiae repudiandae illum corrupti?"""
# word = word.split()

# for i in range(len(word)):
#     for j in readed:
#         if j in word[i]:
#             word[i] = word[i].replace(j,len(j)*'*')

# word = " ".join(word)
# print(word)
"==========================================================================================="
# lst = [1,2,3,4,[5,6,7,8],[9,10,11,[12,13,14,15,16,17,18],19,20]]


# def write_lst(lst,lst1=[]):
#     for i in lst:
#         if type(i)==list:
#             write_lst(i,lst1)
#         else:lst1.append(i)
        
#     return lst1

# print(write_lst(lst))
"================================================================================================"
# lst = ['Red','Blue','Red','Blue','Red']
# lst = ['Blue','Yellow','Red','Green']
# lst = ['Blue','Blue','Blue','Red','Red','Red']
# sum = 2
# for i in range(len(lst)-1):
#     if lst[i]==lst[i+1]:
#         sum+=2
#     else:
#         sum+=3
    
# print(sum)


"==========================================================================================="


# word_num = input("9,6,0 dan iborat son kirit: ")
# def check_180(word_num):
#     word_num2 = word_num[::-1]
#     word_num2=word_num2.replace("6","1")
#     word_num2=word_num2.replace("9","2")
#     word_num2=word_num2.replace("2","6")
#     word_num2=word_num2.replace("1","9")
#     print(word_num,word_num2)
    
#     if word_num2==word_num:
#         return True
#     else:return False


# print(check_180(word_num))
"==========================================================================================="
# name = input("Ism:")
# age = int(input("Yoshi: "))
# if age%2==0:
#     word = f'# {age} Happy Birthday! {name} {age} #'
#     ramka = len(word)*'#'
# else:
#     word = f'* {age} Happy Birthday! {name} {age} *'
#     ramka = len(word)*'*'

# with open("birthday.txt","w") as file:
#     file.write(f'{ramka}\n\n{word}\n\n{ramka}')
    

"================================================================================================"

# animals = ['dog','cat','bat','cock','cow','pig','fox','ant','bord','lion','wolf','derr','bear','frog','hen','mole','duck','goat']
# word  = input("Soz:")
# lst = []
# for i in word:
#     lst.append(i)



"==========================================================================================="

lst = [
    [0,0,0,1,1,1,1],
    [1,1,0,0,1,1,1],
    [1,1,1,0,1,1,1],
    [0,0,1,0,0,1,1],
    [1,1,1,1,0,0,1]
]

# lst = [
#     [0,0,0,1,1,1,1],
#     [1,1,0,0,1,1,1],
#     [1,1,1,0,1,1,1],
#     [0,0,1,0,0,1,1],
#     [1,1,1,1,0,0,0]
# ]


def labirint(lst,i=0,j=0):
    if i==4 and j==6 and lst[i][j]==0:
        lst[i][j]=9
        return lst,True
    
    if i<4 and lst[i+1][j]==0:
        lst[i][j]=9
        i+=1
        return labirint(lst,i,j)
    elif j<6 and lst[i][j+1]==0:
        lst[i][j]=9
        j+=1
        return labirint(lst,i,j)
    else:lst[i][j]=9;return lst,False

a,bole=labirint(lst)
print(bole)
for i in a:
    print(i)


"==========================================================================================="



"==========================================================================================="



"==========================================================================================="



"==========================================================================================="



"==========================================================================================="
