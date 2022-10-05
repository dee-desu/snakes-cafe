def user_order():
    counter = 0
    while True:
        customer_order = input("> ").title()
        if customer_order == "Quit":
            if counter != 0:
                print("\nYou ordered: \n")
                for i in final_order:
                    if final_order[i] != 0:
                        print(f' - {final_order[i]} {i}')
                print("\n")
            else:
                print("\n")
                print("Goodbye...")
                print("\n")
            break
        if customer_order in final_order:
            final_order[f"{customer_order}"] += 1
             
            if  final_order[f"{customer_order}"] == 1:
                print(f"** {final_order[f'{customer_order}']} order of {customer_order} have been added to your meal **")
            else:
                print(f"** {final_order[f'{customer_order}']} orders of {customer_order} have been added to your meal **")
        else:
            print(f"Sorry {customer_order} is not available in our menu")
        counter += 1
                


if __name__ == "__main__":

    MENU = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Beverages
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************'''

    final_order = {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0,
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A literal Garden": 0,
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0,
        "Coffee": 0,
        "Tea": 0,
        "Unicorn Tears": 0
    }

    print(MENU)
    user_order()
