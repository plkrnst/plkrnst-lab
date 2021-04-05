y=1
while True:
    x=input("Введите число: ")
    if x=='q' or x=='quit':
       print('Завершение работы.')
       break
    else: 
        x = int(x)
        print(y)
        y+=1
        if y<x:
            break
        
