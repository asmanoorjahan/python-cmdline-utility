from addfilm import insert_Film
from report import film_report
from deletefilm import delete_film
from updatefilm import update_films



# Show the menu
def showoptions():
    print(""" 
Available Options:
    1. Add
    2. Delete
    3. Update
    4. Print all records
    5. Exit
    """)
    option = input("Enter one of the 5 options shown : ")
    return option

option = showoptions()    
# ask for selection

while option != "5":
    match option:
        case "1": 
            print("Enter values to add a film record --- ")
            insert_Film()
        case "2":
             print("Enter the option to delete a film:")
             delete_film()
        case "3":
            print("Enter the filmID to update :")
            update_films()
        case "4": 
            print("List of all films")
            film_report()
        case _ : print("Please select valid option")
    option = showoptions()

print("Thank you for using this program. Bye!!")


# depending upon selection invoke corresponding method

