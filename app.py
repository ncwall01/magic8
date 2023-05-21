from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = 'John Doe'
    age = 30
    hobbies = ['Programming', 'Reading', 'Gaming']
    return render_template('index.html', name=name, age=age, hobbies=hobbies)

if __name__ == '__main__':
    app.run()
