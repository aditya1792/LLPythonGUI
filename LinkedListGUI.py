'''Linked List in Pyhton'''

def CREATE():
    global LL
    
    print("\n Entr a num : ")
    ele = int(input())
    
    LL.append(ele)

def DISP():
    global LL
    
    if(len(LL)==0):
        print('\n LL is empty')
    else:
        print('LINKED LIST')
        for i in range(len(LL)):
            print( LL[i], end = " ")
            
def Insert_Begin():
    global LL
    
    print("\n Enter a number: ")
    num = int(input())
    
    LL.insert(0, num)
    
def Insert_Nth_Position():
    global LL
    
    print('\n Enter a num')
    ele = int(input())
    
    print('\n Position: ')
    pos = int(input())
    
    if(pos<0):
        print('\n Invalid Position')
    else:
        LL.insert(pos-1,ele)
    
def Insert_End():
    global LL

    print("\n Enter a number : ")
    ele = int(input())
    
    LL.append(ele)
    
def Delete_Begin():
    global LL
    
    if(LL == []):
        print('\n List is Empty')
    else:
        LL.pop(0)
        
def Delete_Given():
    global LL
    
    print('\n Enter num to be deleted')
    num = int(input())
    
    if(num not in LL):
        print('\n Num not found')
    else:
        LL.remove(num)
        
def Delete_Last():
    global LL
    
    if(LL == []):
        print('\n List is empty. ')
    else:
        LL.pop()



    
    


LL = []

while(True):
    print('\n'*5)
    print('\n\n----Main Menu----')
    print('1] Add_an_Element')
    print('2] Display')
    print('3] Insert_Begin')
    print('4] Insert_Nth_Position')
    print('5] Insert_End')
    print('6] Delete_Begin')
    print('7] Delete_Given')
    print('8] Delete_Last')
    print('9] Exit')
    
    print('\n Enter your choice : ')
    choice = int(input())
    
    if(choice ==1):
        CREATE()
        DISP()
    elif(choice ==2):
        DISP()
    elif(choice ==3):
        Insert_Begin()
        DISP()
    elif(choice ==4):
        Insert_Nth_Position()
        DISP()
    elif(choice ==5):
        Insert_End()
        DISP()
    elif(choice ==6):
        Delete_Begin()
        DISP()
    elif(choice ==7):
        Delete_Given()
        DISP()
    elif(choice ==8):
        Delete_Last()
        DISP()
    elif(choice ==9):
        print("\n Exit")
        break
    else:
        print('\n Invalid_Input')
    input()
