## 4. Routing and URL Building

Routing refers to how an application responds to client requests for different URLs. In Flask, routes are defined using the `@app.route` decorator.

### Basic Routing

```python
@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/about')
def about():
    return 'This is the about page'
```

### Dynamic Routes
You can add variable sections to a URL by marking them with `<variable_name>`:

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'
```

### URL Building
Flask provides a `url_for()` function to build URLs for specific functions:

```python
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

This is particularly useful as it allows you to change your URLs in a single place without having to remember to update every URL in your templates.
