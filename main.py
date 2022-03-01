from User import User

miriam = User("Miriam")
rosa = User("Rosa")
carolina = User("Carolina")

#User 1
miriam.make_a_deposit(120)
miriam.make_a_deposit(180)
miriam.make_a_deposit(150)
miriam.withdraw_money(50)
miriam.show_balance()

#User2
rosa.make_a_deposit(100)
rosa.make_a_deposit(200)
rosa.withdraw_money(100)
rosa.show_balance()

#User3
carolina.make_a_deposit(600)
carolina.withdraw_money(150)
carolina.withdraw_money(250)
carolina.withdraw_money(50)
carolina.show_balance()

#Bonus
miriam.transfer_money(carolina,50)
miriam.show_balance()
carolina.show_balance()

# print(miriam.dollars)