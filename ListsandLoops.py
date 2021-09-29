hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#loop through prices, add to total_price
total_price = 0
for price in prices:
  total_price += price

#total price divided by the number of prices to give average
average_price = total_price / len(prices)
print("Average haircut price: $", average_price)

#owner wants to cut all prices by 5 dollars. Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.

new_prices = [price - 5 for price in prices]
print("original prices were: $",prices)
print("The new prices are: $", new_prices)

#Find how much revenue was brought in last week.
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("total revenue $", total_price)

#Find the average daily revenue 

average_daily_revenue = total_revenue / 7
print("average daily revenue: $",average_daily_revenue)

#find cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(cuts_under_30)
