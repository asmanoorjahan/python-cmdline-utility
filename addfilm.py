from connectF import *
def insert_Film():
    filmTitle =    input("Enter film title:    ")
    yearReleased = input("Enter the year:      ")
    filmRating=    input("Enter the rating:    ")
    filmDuration=  input("Enter the duration:  ")
    filmGenre=     input("Enter the film genre:")
    dbCursor.execute("Insert into film(Title,yearReleased,Rating,Duration,Genre) VALUES(?,?,?,?,?)",(filmTitle,yearReleased,filmRating,filmDuration,filmGenre))
    dbCon.commit()
    print(f"{filmTitle} inserted in the film table")

if __name__ == "__main__":
    insert_Film()    
