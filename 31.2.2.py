lemonade = .50
pink_lemonade = .75
raspberry_lemonade = 1
tropical_lemonade = 1
lemonade_sold = 10
pink_sold = 6
raspberry_sold = 3
tropical_sold = 8
tips = 5
total_revenue = lemonade * lemonade_sold + pink_lemonade * pink_sold + raspberry_lemonade * raspberry_sold + tropical_lemonade * tropical_sold + tips
donations_to_charity = .2 #percent
total_donated = total_revenue * donations_to_charity
total_money = total_revenue - total_donated

print("Get your lemonade here!")
print("Regular lemonade costs $" +str(lemonade))
print("Pink lemonade costs $" +str(pink_lemonade))
print("Raspberry lemonade costs $" +str(raspberry_lemonade))
print("Tropical lemonade costs $" +str(tropical_lemonade))
print("Today we sold "+str(lemonade_sold)+" lemonades, "+str(pink_sold)+" pink lemonades, " +str(raspberry_sold)+" raspberry lemonades, and "+str(tropical_sold)+" tropical lemonades")
print("We made $"+str(tips)+" in tips.")
print("In total we made $" +str(total_revenue))
print("We donated $"+str(total_donated)+" to charity")
print("At the end of the day, we made $"+str(total_money))
