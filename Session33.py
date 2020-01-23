# Explore HTML : w3schools
# Explore Flask: w3schools
# https://www.geeksforgeeks.org/flask-creating-first-simple-application/

from flask import Flask

app = Flask(__name__)

@app.route('/')
def fun():
    a = int(input("Enter a: "))
    b = 20
    c = a + b
    return 'sum is: {}'.format(c)


if __name__ == '__main__':
    app.run()

# Create a Program which takes inputs
# name, phone, email of Customer on web page

