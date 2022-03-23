class User:
    
    total_count = 0

    def __init__(self, user_id, user_name, user_email):
        self.id = user_id
        self.name = user_name
        self.email = user_email

class Member(User):

    def __init__(self, user_id, user_name, user_email):
        pass

