#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total= 0.0):
    self.total = total
    self.discount = discount
    self.items = []
    self.prices = []
  
  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    #append the title and price into the lists....use the extend method which will help iterate over an iterable
    self.items.extend([title] * quantity)
    self.prices.extend([price] * quantity)

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      #calculate discount = total * % discount
      discount_amount = self.total * (self.discount / 100)
      discounted_amount = self.total - discount_amount
      self.total = discounted_amount
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    #check if there are items and prices
    if self.items and self.prices:
      last_item = self.items.count(self.items[-1])
      last_price = self.prices[-1] * last_item
      self.total -= last_price

      #delete the last price and item
      del self.items[-last_item:]
      del self.prices[-last_item:]
    else:
      print("No items to void.")
