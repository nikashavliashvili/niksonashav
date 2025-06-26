
from flask import Flask, render_template, request
import random


app = Flask(__name__)

@app.route('/tkt')
def tkt():
    return render_template("tkt.html")

@app.route('/receipt1', methods=['POST'])

def receipt1():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt2.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)

@app.route('/receipt3', methods=['POST'])

def receipt3():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt3.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)

@app.route('/receipt4', methods=['POST'])

def receipt4():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt4.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)

@app.route('/receipt5', methods=['POST'])

def receipt5():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt5.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)
@app.route('/receipt6', methods=['POST'])

def receipt6():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt7.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)
@app.route('/receipt7', methods=['POST'])

def receipt7():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt7.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)
@app.route('/receipt8', methods=['POST'])

def receipt8():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt8.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)
@app.route('/receipt9', methods=['POST'])

def receipt9():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt9.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)
@app.route('/receipt10', methods=['POST'])

def receipt10():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt10.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)
@app.route('/receipt11', methods=['POST'])

def receipt11():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt11.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)
@app.route('/receipt12', methods=['POST'])

def receipt12():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt12.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)
@app.route('/receipt13', methods=['POST'])

def receipt13():
    cinema = request.form['cinema']
    time = request.form['time']
    lang = request.form['lang']
    price = request.form['price']

    # Random seat like "E15"
    row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(1, 20)
    seat = f"{row}{number}"

    return render_template("receipt13.html", cinema=cinema, time=time, lang=lang, price=price, seat=seat)







@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shop')
def shop():
    return render_template('nika.html')



@app.route('/tkt2')
def tkt2():
    return render_template('tkt2.html')

@app.route('/tkt3')
def tkt3():
    return render_template('tkt3.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/tkt4')
def tkt4():
    return render_template('tkt4.html')

@app.route('/newhome')
def newhome():
    return render_template('home2.html')

@app.route('/frshop')
def frshop():
    return render_template('realshop.html')

@app.route('/tkt5')
def tkt5():
    return render_template('tkt5.html')


@app.route('/tkt6')
def tkt6():
    return render_template('tkt6.html')


@app.route('/tkt7')
def tkt7():
    return render_template('tkt7.html')


@app.route('/tkt8')
def tkt8():
    return render_template('tkt8.html')

@app.route("/realshop")
def realshop():
    return render_template("realshop.html")


@app.route('/receipt')
def receipt():
    return render_template("receipt.html")



if __name__ == '__main__':
    app.run(debug=True)

