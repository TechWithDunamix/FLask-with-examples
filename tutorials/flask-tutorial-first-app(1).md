## 3. Creating Your First Flask Application

Now that we have our environment set up, let's create a simple Flask application. We'll start with a basic "Hello, World!" example.

1. Create a new file called `app.py` in your project directory.
2. Open `app.py` in your favorite text editor and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

3. Save the file and return to your terminal.
4. Run the application:

```
python app.py
```

5. Open a web browser and navigate to `http://127.0.0.1:5000/`. You should see "Hello, World!" displayed.

Congratulations! You've just created your first Flask application. Let's break down what's happening in this code:

- We import the Flask class from the flask module.
- We create an instance of the Flask class, which we name `app`.
- We use the `@app.route()` decorator to tell Flask what URL should trigger our function.
- The function returns the message we want to display in the user's browser.
- The `if __name__ == '__main__':` block ensures that the development server is only run if the script is executed directly (not imported as a module).
