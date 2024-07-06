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
    
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the list")
            pass
        elif choice == '2':
            item = input("enter item to remove: ")
            if item in shopping_list:
             shopping_list.remove(item)
             print(f"{item} removed from the list: ")
            else:
                print(f"{item} not find in the list: ")
            pass
            print
        elif choice == '3':
            if shopping_list:
                print("your shopping list. ")
                for item in shopping_list:
                 print(item)
            else:
                print(f"{item} no item in shopping list: ")     
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()