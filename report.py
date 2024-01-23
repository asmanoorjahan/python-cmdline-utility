from connectF import *
def film_report():
    dbCursor.execute("select * from film order by yearReleased desc")
    records = dbCursor.fetchall()
    for aRecord in records:
        print(aRecord)
if __name__ =="__main__":
  film_report()        
 