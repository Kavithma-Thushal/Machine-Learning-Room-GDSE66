from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    # Render the form page
    return render_template('login-form.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    # Pass the login data to the submitted template
    return render_template('login-details.html', username=username, password=password)


if __name__ == '__main__':
    app.run(debug=True)
