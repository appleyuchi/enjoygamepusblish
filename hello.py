from flask import  Flask,render_template
app = Flask(__name__)


@app.route('/home')
def index_home():
    return render_template('home.html')
    # return '<h1>Hello World!</h1>'


@app.route('/about')
def index_about():
    return render_template('about.html')
    # return '<h1>Hello World!</h1>'

@app.route('/guest_book')
def guest_book():
    return render_template('guest_book.html')
    # return '<h1>Hello World!</h1>'


@app.route('/map')
def index_map():
    return render_template('map.html')
    # return '<h1>Hello World!</h1>'



@app.route('/estore')
def index_estore():
    return render_template('estore.html')
    # return '<h1>Hello World!</h1>'


@app.route('/crowdfunding')
def index_crowdfunding():
    return render_template('crowdfunding.html')
    # return '<h1>Hello World!</h1>'


# 这个的目的是只剩下导航栏
@app.route('/flight')
def index_test():
    return render_template('flight_nav.html')#这个取名的意思是整合现有的导航栏
    # return '<h1>Hello World!</h1>'


@app.route('/flight')
def index_flight():
    return render_template('flight.html')
    # return '<h1>Hello World!</h1>'




if __name__ == '__main__':
    app.run(debug=True,port=10071)