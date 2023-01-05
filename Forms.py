from wtforms import Form, StringField, RadioField, TextAreaField, validators, EmailField, DateField, IntegerField


class CreateUserFrom(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=100), validators.DataRequired()], render_kw={"placeholder": "Enter First Name"})
    last_name = StringField('Last Name', [validators.Length(min=1, max=100), validators.DataRequired()], render_kw={"placeholder": "Enter Last Name"})
    today_date = DateField('Today Date', render_kw={"placeholder": "Enter Today's Date"})
    age = IntegerField('Input Age', render_kw={"placeholder": "Enter Your Age"})
    phone_no = StringField('Input Phone Number', [validators.Length(max=8), validators.DataRequired()], render_kw={"placeholder": "+65"})
    gender = RadioField('Gender', choices=[("M", "Male"), ("F", "Female")], render_kw={"placeholder": "Enter Your Gender"})
    email_address = EmailField("Input Email", [validators.InputRequired()], render_kw={"placeholder": "Enter your email, eg:. example@gmail.com"})
    postal_code = TextAreaField("Postal Code", render_kw={"placeholder": "Enter your 6 digit postal code"})


