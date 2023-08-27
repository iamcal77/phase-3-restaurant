class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        self._reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self._name

    def reviews(self):
        return self._reviews

    def customers(self):
        return list(set([review.customer() for review in self._reviews]))

    def add_review(self, review):
        self._reviews.append(review)

    def average_star_rating(self):
        total_ratings = sum([review.rating() for review in self._reviews])
        num_reviews = len(self._reviews)
        if num_reviews > 0:
            return total_ratings / num_reviews
        return 0

    @classmethod
    def all(cls):
        return cls.all_restaurants
