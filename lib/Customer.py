class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer.all_customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        restaurant.add_review(new_review)

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        self._reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self._name

    def add_review(self, review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews

    def customers(self):
        return list(set([review.customer() for review in self._reviews]))

    @classmethod
    def all(cls):
        return cls.all_restaurants
