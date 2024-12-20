from exercise_restaurant import User
    
class Admin(User):
    def __init__(self, first_name, last_name, phone, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.age = age
        self.gender = gender
        self.privileges = Privileges()
    
class Privileges():
    
    def __init__(self):
        self.list_privileges = [
            "can add post",
            "can delete post", 
            "can ban user",
        ]

    def show_privileges(self):
        print('Privilegios do admin:')
        for privilege in self.list_privileges:
            print(privilege)


admin = Admin('Henrique', 'Bisetto', 21321312389, 35, 'M')
admin.privileges.show_privileges()