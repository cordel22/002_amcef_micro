##### this module connects to a restful api service ###

import requests
# db module creates and populates the database
import db  
from sqlalchemy.orm import sessionmaker
import os
import time
import pprint


# admin password
admin = { "passw" : "0000" }
# user password
user = {  "passw": "1111" }
# user_id, you might wann extract it from restapi
user_id = range(1,10)
id = range(1,100)

# endpoints for the restfulapi
endpoint1 = 'users'
endpoint2 = 'posts'
#url of the restful api
url = "https://jsonplaceholder.typicode.com/"
# response variable array
res = []


#   calling restful api service
def api_call(url, endpoint):
  return requests.get(url + endpoint).json()

#   add post to database
def add_post(user_id, id, title, body):
    post = db.Posts( user_id, id, title, body)
    # post = db.db_connect.Posts( user_id, id, title, body)
    session.add(post)
    session.commit()

#   query entire database
def show_all():
    for s in session.query(db.Posts).all():
      print("\nuser_id : ", s.user_id, "\nid : ", s.id, "\ntitle : ", s.title, "\nbody : ", s.body, "\ndate : ", s.date)

#   query database by user_id
def show_by_user(userId):
  for t in session.query(db.Posts).filter(db.Posts.user_id==userId):
      print("\nuser_id : ", t.user_id, "\nid : ", t.id, "\ntitle : ", t.title, "\nbody : ", t.body, "\ndate : ", t.date)

#   query database by post id
def show_by_id(id):
  for u in session.query(db.Posts).filter(db.Posts.id==id):
      print("\nuser_id : ", u.user_id, "\nid : ", u.id, "\ntitle : ", u.title, "\nbody : ", u.body, "\ndate : ", u.date)

#   update post title
def edit_title(idecko, newTitle):
  session.query(db.Posts).filter(db.Posts.id == idecko).update({db.Posts.title:newTitle})
  session.commit()
#   update post body
def edit_body(ident, newBody):
  session.query(db.Posts).filter(db.Posts.id == ident).update({db.Posts.body:newBody}, synchronize_session = False)
  session.commit()

#   delete by id
def delete_by_id(identif):
  # session.query(db.Posts).filter(db.Posts.id == identif)
  # session.delete()
  session.query(db.Posts).filter(db.Posts.id == identif).delete()
  session.commit()
#   delete all
def delete_all():
  
  session.query(db.Posts).delete()
  session.commit()


# connect to database, create it if there is none
# db.db_connect()
os.system('python db.py')

# connect to database session
Session = sessionmaker(bind=db.engine)
session = Session()


password = input("Enter password, admin 0000, user 1111 :")

### admin UI
if password == admin["passw"]:
  # connect to database session
  
  while True:
    print("\nWelcome Admin\n")
    print("\n1) If you want to see all the posts in the database, press 1 \n")
    print("\n2) If you want to see the posts by user_id, press 2 \n")
    print("\n3) If you want to see a particular post, press 3 \n")
    print("\n4) If you want to DOWNLOAD posts from RESTful api and put it INTO database, press 4 \n")
    print("\n5) If you want to EDIT a post Title, press 5 \n")
    print("\n6) If you want to EDIT a post Title, press 6 \n")
    print("\n7) If you want to DELETE  post, press 7 \n")
    print("\n8) If you want to DELETE ALL posts, press 8 \n")
    

    print("\nx) Exit, press x \n")

    choice = input("Type your choice, please : ")
    # if you want to read from the database

      #   read all

    if choice == "1":
      show_all()
      
      #   read by user_id
    if choice == "2":
      userId = input("\nEnter the user_id, please : ")
      show_by_user(userId)
      #   read by post id
    if choice == "3":
      idcko = input("\nEnter the post id, please : ")
      show_by_id(idcko)

    # if you want to write to your database

      #   if you want to download from rest api serve into your database

    # reload the database from api server
    if choice == "4":
      res = api_call(url, endpoint2)

      # saves the posts into the database
      for x in range(100):
        add_post(
          res[x]["userId"],
          res[x]["id"],
          res[x]["title"],
          res[x]["body"]
          )

        # if you want to edit existing post by user_id by id
    if choice == "5":
      idecko = input("\nEnter the post id you want to edit the Title, please : ")
      newTitle = input("\nType in the new Title, please : ")
      edit_title(idecko, newTitle)


        # if you want to edit existing post by id
    if choice == "6":
      ident = input("\nEnter the post id you want to edit the Body, please : ")
      newBody = input("\nType in the new Body, please : ")
      edit_body(ident, newBody)
      # if you want to delete a post
    
        # delete a post by id
    if choice == "7":
      identif = input("\nEnter the post id you want to delete, please : ")
      delete_by_id(identif)
        # delete all
    if choice == "8":
      confirm = input("\nAre you sure you want to DELETE EVERYTHING from the database? y/n : ")
      if confirm == "y":
        delete_all()
        

    # Exit
    if choice == "x":
      break
print("Cheers, byeO!")
  # option = input("\nType in 1 to see all the posts, 2 to see posts from a selected user, 3 to edit a post, 4 to delete a post")

### user UI


### failed password







