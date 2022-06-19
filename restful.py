import requests
import db
from sqlalchemy.orm import sessionmaker
import time
import pprint

check = { "kokot": "mas to tu kokot" }

Session = sessionmaker(bind=db.engine)
session = Session()


def add_post(user_id, id, title, body):
    post = db.Posts( user_id, id, title, body)
    session.add(post)
    session.commit()


res = requests.get("https://jsonplaceholder.typicode.com/posts").json()

'''
for x in range(100):
  print(
    str(res[x]["userId"])
    + "\n" + str(res[x]["id"])
    + "\n" + res[x]["title"] 
    + "\n" + res[x]["body"]
    )
    '''

for x in range(100):
  add_post(
    res[x]["userId"],
    res[x]["id"],
    res[x]["title"],
    res[x]["body"]
    )
'''
add_post(
    res[0]["userId"],
    res[0]["id"],
    res[0]["title"],
    res[0]["body"]
    )
    '''


session.close()
