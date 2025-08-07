

# 03_duplicate_items.py
# This script identifies duplicate items from a list of user-input items.
    
def duplicate():
    #user input
    items = input("Enter the items separated by spaces: ")
    #numbers split malpara
    items=items.split()
     #items set d print apunda thuvara {} curly braces
    seen = set(items)
    print("Seen items are:", seen)#print malapara set n
    duplicates = []# duplicate item store malpara array create malthin
    
    for item in items:#for loop onji onji number n la iterate malpara  items d ethina 
        if item in seen:#item d duplicate ethnda 
            duplicates.append(item)#duplicate andh empty array d append malpara
        else:
            # ejanda item n seen set d add malpara
            seen.add(item)
    #print malapara duplicate items n
    print("Duplicate items are:", duplicates)

#function call malpara
duplicate()
# This code will prompt the user to enter items, identify duplicates, and print them.
