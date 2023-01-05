import inquirer
import helper
import api

api = api.Api()

def resolve_save_password():
    name = input('Enter what this password is for: ')
    length = input('Enter what is the length of the generated password: ')
    api.create(name=name, password=helper.generate_random_password(int(length))) 
    return

def resolve_update_password():
    name = input('what password do you want to update: ')
    length = input('Enter what is the length of the new generated password: ')
    api.update(name=name, password=helper.generate_random_password(int(length))) 
    return

def resolve_view_saved_password():
    name = input("name for the password? (show all if input is empty): ")
    api.view(name)
    return

def resolve_remove_password():
    name = input("name for the password?: ")
    api.remove(name)
    return


api.check_and_create_db()

options = ['view saved passwords', 'save a password','update a password','remove a password']

questions = [
    inquirer.List('action', message = 'What do you want to do?', choices = options)
]

answers = inquirer.prompt(questions)

choice = answers['action']

if(choice == 'view saved passwords'):
    resolve_view_saved_password()
elif(choice == 'save a password'):
    resolve_save_password()
elif(choice == 'update a password'):
    resolve_update_password()
elif(choice == 'remove a password'):
    resolve_remove_password()
else:
    pass