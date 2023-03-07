from flask import Flask

# Create a Flask application instance
app = Flask(__name__)
    
# Define the route for the index page
@app.route("/")
def index():
    # Fetch a single document from the test_collection
    with open('data/data.txt') as f:
        lines = f.readlines()
    # Return the fetched data as a string
    return str(lines)

# Start the Flask application if this file is being executed as the main script
if __name__ == "__main__":
    # Start the Flask application, listening on all available interfaces
    app.run(host="0.0.0.0")

