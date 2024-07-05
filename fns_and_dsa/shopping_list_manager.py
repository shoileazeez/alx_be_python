#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#thislist[1:3] = ["blackcurrant", "watermelon"]
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist[1:2] = ["blackcurrant", "watermelon"]
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist[1:3] = ["watermelon"]
#print(thislist)


#thislist = ["apple", "banana", "cherry"]
#thislist.insert(2, "watermelon")
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist.insert(1, input(f"enter the name of your fruit: "))
#thislist.append(input(f"enter the name of your friut: "))
#print(thislist)
  
#thislist = ["apple", "banana", "cherry"]
#tropical = ["mango", "pineapple", "papaya"]
#thislist.extend(tropical)
#print(thislist) 

#thislist = ["apple", "banana", "cherry"]
#thistuple = ("kiwi", "orange")
#thislist.extend(thistuple)
#print(thislist)


#thislist = ["apple", "banana", "cherry"]
#thislist.remove("banana")
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist.remove("banana")
#print(thislist)

#thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
#thislist.remove("banana")
#print(thislist)  

#thislist = ["apple", "banana", "cherry"]
#thislist.pop(1)
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist.pop(0)
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#del thislist[0]
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#del thislist

#thislist = ["apple", "banana", "cherry"]
#thislist.clear()
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#for x in thislist:
  #print(x)
  
#thislist = ["apple", "banana", "cherry"]
#for i in range(len(thislist)):
#  print(thislist[i])

#thislist = ["apple", "banana", "cherry"]
#i = 0
#while i < len(thislist):
 # print(thislist[i])
 # i = i + 1
    
while True:
    user_choice = input("do you want to convert F or C?: ")
    match user_choice:
        case "F":
            x = int(input("Please enter farihneit tempature: "))
            farinheit = (x-32) * 5/9
            print(farinheit)
            break
        case "C":
            c = int(input("Please enter celcius tempature: "))
            celcius = (c*1.8) + 32
            print(celcius)
            break
        case _:
            print("wrong input")
            continue