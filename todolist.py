

print('Welcome to your to do list')

lst = []
close = False


while close == False:
 aud = input("do you want to (add) or (remove) or (change) or (print) list or (close) program: ")

 if aud == 'add':
    intask = input("Enter task ")
    lst.append(intask)
    print('task added successfully')
 elif aud == 'remove':
    retask = input("enter task that u want to remove ")
    if retask in lst:
        lst.remove(retask)
        print('task removed successfully')
    else:
        print('task not found')
 elif aud == 'change':
     chtask1 = input('Enter the task you want to change: ')
     chtask2 = input('What do you want to change it to: ')

     if chtask1 in lst:
    # Get the index of chtask1
      chtask1_index = lst.index(chtask1)
    
    # Replace the old task with the new task
      lst[chtask1_index] = chtask2
      print('Item changed successfully')
     else:
      print('Task not found')
 elif aud == 'print':
    print(lst)
 elif aud == 'close':
     close = True