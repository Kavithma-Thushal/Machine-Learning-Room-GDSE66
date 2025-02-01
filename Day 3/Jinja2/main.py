from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    # Render the form page
    return render_template('customer-form.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    # Pass the data to the submitted template
    return render_template('customer-details.html', name=name, email=email, phone=phone)


if __name__ == '__main__':
    app.run(debug=True)
