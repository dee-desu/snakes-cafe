def print_menu():
    print("***************************************\n**     welcome to the Snakes Cafe!   **\n**     Please see our menu below.    ** \n**                                   **\n** To quit at any time, type  'quit' **\n***************************************\nAppetizers\n----------\nwings\ncookies\nspring Rolls\n\nEntrees\n-------\nSalmon\nSteak\nMeat Torando\nA Literal Garden\n\nDesserts\n--------\nIce Cream\nCake\npie\n\nDrinks\n------\nCoffee\nTea\nUnicorn Tears")
    print("***********************************\n** What would you like to order? **\n***********************************")

print_menu()

menu=["wings","cookies","spring rolls","salmon","steak","meat torando","a literal garden","ice cream","cake","pie","coffee","tea","unicorn tears"]

def take_order():
    added_item_arr=[]
    final_order={}
    items = ["wings","cookies","spring rolls","salmon","steak","meat torando","a literal garden","ice cream","cake","pie","coffee","tea","unicorn tears"]
    values = []
    
    while True:
        order=input("> ")
        count = 0
       
        if order.lower() == "quit" :
            break
      
        if order.lower() in menu:
            added_item_arr.append(order.lower())
           
            if order.lower() in added_item_arr:
                for j in range(len(added_item_arr)) :
                    if order.lower() == added_item_arr[j]:
                        count+=1
                        for i in range(len(items)):
                            if added_item_arr[j] == items[i]:
                                final_order[items[i]] = count
                items_arr=[]
                keys_arr=[]
                
                for k in final_order.items():
                    keys_arr.append(k)
               
                for values in final_order.values():
                    items_arr.append(values)
               
                for l in range(len(final_order)):
                    order_details=keys_arr[l]
                    order_total=items_arr[l]
                    print(f"** {order_total} order of {order_details} have been added to your meal **")
            else:
                count+=1
                print(f"** {count} order of {order} have been added to your meal **")
        elif order.lower() not in menu:
            print(f"sorry,{order} is not available menu")
    print(f"you order is: {final_order}")
take_order()