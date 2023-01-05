from pymongo import MongoClient

class Api:
    db_name = 'local'
    collection_name = 'password'
    
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[f'{self.db_name}']
        self.collection = self.db[f'{self.collection_name}']

    def __check_is_collection_exist(self):
        return self.collection_name in self.db.list_collection_names()

    def check_and_create_db(self):
        if(not self.__check_is_collection_exist()):
            self.collection.create_index('name',unique=True)
            self.collection.insert_one({'name': 'test', 'password': 'test'})
        if(not self.__check_is_collection_exist()):
            raise ValueError('Database error')
        return

    def show_index(self):
        cur = self.collection.list_indexes()
        for c in cur:
            print(c)
        return

    
    def create(self, name:str, password:str) -> None:
        if((name.strip() == '') or (len(password) == 0)):
            raise ValueError('Incorrect input')
        self.collection.insert_one({'name': name, 'password': password})
        print(f'password for {name} set')
        return

    def update(self, name:str, password:str) -> None:
        if((name.strip() == '') or (len(password) == 0)):
            raise ValueError('Incorrect input')
        result = self.collection.update_one({'name': name}, { "$set": { 'password': password } })
        isUpdated = result.matched_count > 0
        print(f'password for {name} {"" if isUpdated == True else "not"} updated')
        return

    def view(self,name:str) -> None:
        search_para = {}
        if(name != ''):
            search_para['name'] = name
        cursor = self.collection.find(search_para)
        for c in cursor:
            print(f"{c['name']}={c['password']}")
        return

    def remove(self, name:str) -> None:
        if(name.strip() == ''):
            raise ValueError('Incorrect input')
        self.collection.delete_one({'name': name})
        print(f'password for {name} removed')
        return



