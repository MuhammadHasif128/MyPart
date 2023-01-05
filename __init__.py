from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from Forms import CreateUserFrom
import shelve
import User

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/user_registration', methods=['GET', 'POST'])
def register_user():
    user_register = CreateUserFrom(request.form)
    if request.method == 'POST' and user_register.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except IOError:
            print("Error in retrieving Users from user.db.")

        user = User.User(user_register.first_name.data, user_register.last_name.data, user_register.today_date.data, user_register.age.data, user_register.phone_no.data, user_register.gender.data, user_register.email_address.data, user_register.postal_code.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        # test message
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print(user.get_first_name(), user.get_last_name(), "was stored in user.db successfully with user_id ==", user.get_user_id())
        db.close()
        return redirect(url_for('home'))
    return render_template('user_registration.html', form=user_register)


if __name__ == '__main__':
    app.run()
