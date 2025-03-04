from tinydb import TinyDB, Query
db = TinyDB('db.json')

User = Query() # type: tinydb.queries.Query

def insert_user():
    db.insert({'name': 'John', 'age': 22})
    db.insert({'name': 'Max', 'age': 25})
    db.insert({'name': 'Sarah', 'age': 21, 'city': 'New York'})

def search_user():
    results = db.search(User.city == 'New York') # returns a list
    for res in results:
        print(res) # type: tinydb.database.Document
        # print(res.city) # Not allowed!
        print(res['city'])

    results = db.search(User.age > 21)
    for res in results:
        print(res)

def update_user():
    db.update({'age': 26}, User.name == 'Max')
    for item in db:
        print(item)

    # or
    results = db.search(User.name == 'Max')
    for res in results:
        res['age'] = 27
    #db.write_back(results) # write back results we retrieved # write_back deprecated, trying replace
    print("error here:")
    print(results)
    db.update(replace(results), doc_ids=[doc_id])
    #db.update(replace(results), doc_ids=[doc_id])
    #db.replace(results)

    # or get and update/remove by document_id

def delete_user():
    db.remove(User.name == 'John')
    # db.purge() # remove all

def update_by_document_id():
    db.remove(doc_ids=[2])
    # this will not create doc_id=2, but the next highest number
    db.insert({'name': 'Jason', 'age': 40})

    item = db.get(doc_id=3)
    print(item)
    print(item.doc_id)

    db.update({'city': 'Boston'}, doc_ids=[1, 2])

    db.remove(doc_ids=[1, 2])

# def replace(new):
#     """
#     Used with update to replace the original doc with new. # needed to replace TinyDB.write_back()
#     """
#     def transform(doc):
#         # update doc to include key/values from new
#         doc.update(new)
#         # remove any key/values from doc that are not in new
#         for k in list(doc.keys()):
#             if k not in new:
#                 del doc[k]
#         return transform


#### TESTS ####

# db.purge() # empty db
db.truncate() # empty db

insert_user()
search_user()
# update_user()
delete_user()
#update_by_document_id()

print(db.all())
for item in db:
    print(item)
print(len(db)) # number of items


class Quiz:
    def __init__(self):
        pass

def add_question():
    db.insert({'question': 'John', 'answer': 22})




# class QueueError(IndexError):  # Choose base class for the new exception.
#     # def __init__(self):
#     #     self.IndexError
#     pass
#
# class Queue:
#     def __init__(self):
#         self.q=[]
#
#     def put(self, elem):
#         self.q.insert(0,elem)
#
#     def get(self):
#         if len(self.q) > 0:
#             elem = self.q[-1]
#             del self.q[-1]
#             return(elem)
#         else: raise QueueError
#
# que = Queue()
# que.put(1)
# que.put("dog")
# que.put(False)
# try:
#     for i in range(4):
#         print(que.get())
# except:
#     print("Queue error")