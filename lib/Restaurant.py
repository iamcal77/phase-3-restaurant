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

    def average_star_rating(self):
        if len(self._reviews) == 0:
            return 0
        total_rating = sum([review.rating() for review in self._reviews])
        return total_rating / len(self._reviews)

    @classmethod
    def all(cls):
        return cls.all_restaurants
