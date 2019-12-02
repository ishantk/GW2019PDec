"""
    Software Development Architecture

    MODEL
        data
    VIEW
        gui
    CONTROLLER
        logic
        1. Computation
        2 Conditional Flows
        3. Iteration

    example:
        we wish to order food online and
        hence it must be delivered to our home

        restaurant
        customer
        deliveryAgent

"""

# MODEL : Single Value Container

restaurantName = "Rishi Veg Dhaba"
restaurantPhone = "+91 99999 88888"
restaurantPricePerPerson = 300


# MODEL : Multi Value Container

# List
restaurant = ["Rishi Veg Dhaba",
              "+91 99999 88888",
              300,
              "Landmark",
              "08:00 - 22:00"]

# Dictionary | JSON (Java Script Object Notation)
restaurant = {"name": "Rishi Veg Dhaba",
              "phone": "+91 99999 88888",
              "pricePerPerson": 300,
              "landmark": "Country Homes",
              "time": "08:00 - 22:00"}