from connectF import *
def update_films():
    idField= input("Enter the filmID of the record to update:")
    fieldName=input("Enter the title or yearReleased,rating,duration,Genre as field name:")
    fieldValue=input(f"Enter the value for {fieldName} field")
    fieldValue= "'"+fieldValue+"'"
    dbCursor.execute(f"update film set {fieldName}={fieldValue} where filmID={idField}")
    dbCon.commit() 
    print(f"Record {idField} update in the film table")
if __name__ == "__main__":
 update_films()           
