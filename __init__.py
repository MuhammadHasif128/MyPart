from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from Forms import CreateUserFrom

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/user_registration', methods=['GET', 'POST'])
def register_user():
    user_register = CreateUserFrom(request.form)
    if request.method == 'POST' and user_register.validate():
        return redirect(url_for('output'))
    else:
        return render_template('user_registration.html', form=user_register)


if __name__ == '__main__':
    app.run()
