# Basic structure of a Flask server

# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "Hello, Flask!"

# Run the server
if __name__ == '__main__':
    app.run(debug=True)