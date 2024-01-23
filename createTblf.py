from connectF import *

dbCursor.execute(
    """
Create Table "Film"(
     "filmID"  INTEGER NOT NULL  UNIQUE,
     "title" TEXT,
     "yearReleased" INTEGER,
     "rating" text,
     "duration" INTEGER,
     "GENRE" TEXT,
     PRIMARY KEY("filmID" AUTOINCREMENT)


 )"""
 )