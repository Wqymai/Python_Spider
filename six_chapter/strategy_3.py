# -*- coding: utf-8 -*-
from abc import ABCMeta,abstractmethod
from collections import namedtuple
import promotions
import inspect

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<order total:{:.2f} due:{:.2f}>'
        return fmt.format(self.total(),self.due())


promos = [func for name, func in
          inspect.getmembers(promotions, inspect.isfunction)]
print promos


def best_promo(order):
    return max(promo(order) for promo in promos)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart =[LineItem('banana', 4, .5),
       LineItem('apple', 10, 1.5),
       LineItem('watermellon', 5, 5.0)]

print Order(joe,cart,best_promo)




