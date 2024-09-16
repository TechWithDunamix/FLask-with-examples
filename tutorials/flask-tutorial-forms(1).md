## 6. Working with Forms

Forms are an essential part of web applications. Flask-WTF is an extension that integrates WTForms into your Flask application, providing an easy way to create and handle web forms.

### Installation

First, install Flask-WTF:

```
pip install Flask-WTF
```

### Creating a Form

Create a new file called `forms.py`:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Log In')
```

### Using the Form in a Route

Update your `app.py`:

```python
from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.email.data}', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

### Creating a Template for the Form

Create a new file `login.html` in your `templates` folder:

```html
{% extends "base.html" %}

{% block content %}
    <h1>Sign In</h1>
    <form method="POST" action="">
        {{ form.hidden_tag() }}
        <div>
            {{ form.email.label }}
            {{ form.email(size=32) }}
        </div>
        <div>
            {{ form.password.label }}
            {{ form.password(size=32) }}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
{% endblock %}
```

This setup allows you to create, validate, and process forms in your Flask application.
