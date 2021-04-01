from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/university')
def university():
    return render_template("university.html")


@app.route('/university_response')
def university_response():
    name = request.args.get('name')
    math = request.args.get('math')
    latvian = request.args.get('latvian')
    foreign = request.args.get('foreign')
    is_good_average = good_average(math,latvian,foreign)
    return render_template("university_response.html", is_good_average=is_good_average, name=name)


def good_average(math, latvian, foreign):
    if int(math) > 39 and int(latvian) > 39 and int(foreign) > 39:
        return True


if __name__ == "__main__":
    app.run(debug=True)