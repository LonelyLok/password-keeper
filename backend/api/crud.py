from pymongo import MongoClient
from bson.json_util import dumps, loads

class CRUD:
    db_name = 'local'
    collection_name = 'password'
    
    def __init__(self):
        self.client = MongoClient('mongodb://host.docker.internal:27017/')
        # self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[f'{self.db_name}']
        self.collection = self.db[f'{self.collection_name}']

    
    def check_keys_type(self,fig:dict[str,str],expected_keys:list[str]):
        for k in fig:
            if(k in expected_keys):
                v = fig[k]
                if(isinstance(v,str)):
                    expected_keys.remove(k)
        if(len(expected_keys) != 0):
            raise ValueError('Incorrect input')

    
    def create(self, fig:dict[str,str]):
        self.check_keys_type(fig,['name','username','password'])
        resp = self.collection.insert_one(fig)
        return resp

    def update(self, fig:dict[str,str]):
        self.check_keys_type(fig,['name','username','password'])
        resp = self.collection.update_one({'name': fig['name'], 'username': fig['username']}, { "$set": { 'password': fig['password'] } })
        return resp

    def get_all(self):
        cursor = self.collection.find({})
        return list(cursor)

    def remove(self, fig:dict[str,str]):
        self.check_keys_type(fig,['name','username'])
        resp = self.collection.delete_one(fig)
        return resp
