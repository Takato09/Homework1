import flask

import student

application = flask.Flask(__name__)


@application.route('/')
def index():
    response = flask.render_template(
        template_name_or_list='index.html',
        title='Calculate average',
    )

    return response


@application.route('/hello/', methods=['POST'])
def hello():
    name = flask.request.form['name']

    return f'Hello, {name}'


@application.route('/average/', methods=['POST'])
def average():
    name = flask.request.form['name']
    grades = list(map(int, flask.request.form['grades'].split(',')))

    named_student = student.Student(
        name=name,
        grades=grades,
    )

    student_average = named_student.average()
    content = named_student.generate_report(average=student_average)

    return content


application.run(debug=True)