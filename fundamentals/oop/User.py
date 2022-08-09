class user():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"User: {self.first_name} {self.last_name}\n Email: {self.email}\n Age: {self.age}\n Is rewards member: {self.is_rewards_member}\n Gold Card Points:{self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("Member is already a rewards member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points - amount >= 0:
            self.gold_card_points -= amount
        else:
            print("Not enough points to spend")
        return self

user1,user2, user3  = user('Bruce', 'Wayne', 'iamnotbatman@gmail.com', 62),user('Jason', 'Todd', 'jokersbiggestfan@aol.com', 36), user('Damion', 'Wayne', 'bookytheclown@hotmasil.com', 17)
user1.display_info().enroll().spend_points(50).display_info().enroll()
user2.enroll().spend_points(80).display_info()
user3.display_info().spend_points(40)



