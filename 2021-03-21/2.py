import flask

application = flask.Flask(__name__)

save = "Go to the <a href = '/add_user'>/add_user</a><ul>"


class User:

    def __init__(self, username, e_mail):
        self.username = username
        self.e_mail = e_mail

    def print(self):
        formatted = f"""
        <h1>Successfully added {self.username}</h1>
        <p>Email: {self.e_mail}</p>
        <a href = '/add_user'>Add new user</a> or <a href = '/'>See all added users</a>
        """

        return formatted

    def report(self):
        formatted = f"""
        <li>
        <h1>{self.username}</h1>
        <p>Email: {self.e_mail}</p>
        </li>
        """

        return formatted


@application.route('/')
def index():
    global save
    return save


@application.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if flask.request.method == 'GET':
        response_content = """
    <form action="/add_user" method="post">
    Username: <input type="text" name="username"><br>
    E-mail: <input type="text" name="e_mail"><br>
    <input type="submit">
    </form>
    """
    elif flask.request.method == 'POST':
        username = flask.request.form['username']
        e_mail = flask.request.form['e_mail']
        response_content = User(username, e_mail).print()
        saved_response_content = User(username, e_mail).report()
        global save
        save += saved_response_content

    return response_content


application.run(debug=True)