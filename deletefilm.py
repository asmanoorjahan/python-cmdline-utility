from connectF import *

def delete_film():
    idField= input("Enter the filmID of the record to be deleted:")
    dbCursor.execute(f"delete from film where filmID={idField}")
    dbCon.commit()
    print(f"Record{idField} deleted from the films table")
if __name__ == "__main__":
    delete_film()
