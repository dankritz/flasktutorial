# Tutorial video: https://www.youtube.com/watch?v=Z1RJmh_OqeA
from flask import Flask, render_template, url_for

app = Flask(__name__) # Create a new instance of app. __name__ references this file

@app.route('/') # Set the route so we don't get a 404
def index(): # Define the index for this route)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)