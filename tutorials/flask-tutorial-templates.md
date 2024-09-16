## 5. Templates and Jinja2

Flask uses the Jinja2 templating engine to render HTML templates. This allows you to generate dynamic HTML pages that can display different content depending on the arguments passed to the template renderer.

### Creating a Template

Create a new directory called `templates` in your project folder. Inside this folder, create a new file called `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
    <p>This is a Flask template.</p>
</body>
</html>
```

### Rendering a Template

To render this template, update your `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', title='Home', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

### Template Inheritance

Jinja2 supports template inheritance, which allows you to build a base "skeleton" template that contains all the common elements of your site and defines blocks that child templates can override.

Base template (`base.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %} - My Website</title>
    {% endblock %}
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright 2024 by you.
        {% endblock %}
    </div>
</body>
</html>
```

Child template (`child.html`):

```html
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p class="important">Welcome to my awesome homepage.</p>
{% endblock %}
```
