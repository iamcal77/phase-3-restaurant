from customer import Customer
from restaurant import Restaurant
from review import Review

# Create customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Create restaurants
restaurant1 = Restaurant("Tasty Eats")
restaurant2 = Restaurant("Spice Kingdom")

# Create reviews
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)
review3 = Review(customer2, restaurant2, 3)

# Print information
print("Customers:", [customer.full_name() for customer in Customer.all()])
print("Restaurants:", [restaurant.name() for restaurant in Restaurant.all()])
print("Reviews:")
for review in Review.all():
    print(f"{review.customer().full_name()} reviewed {review.restaurant().name()} with a rating of {review.rating()}")

print("Average rating for Tasty Eats:", restaurant1.average_star_rating())
