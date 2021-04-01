from wsgiref.simple_server import make_server
from string import Template
from urllib.parse import parse_qsl, parse_qs


def load_template(name):
    with open(name, "r") as template:
        source = Template(template.read())

    return source


def load_request_body(environ):
    try:
        length = int(environ["CONTENT_LENGTH"])
    except ValueError:
        length = 0

    request_body = environ["wsgi.input"].read(length)
    return request_body.decode()


def parse_request_body(request_body):
    parsed = parse_qsl(request_body)

    return dict(parsed)


def load_request(environ):
    request_body = load_request_body(environ)
    parsed_body = parse_request_body(request_body)

    request = Request(path=environ["PATH_INFO"], data=parsed_body)

    return request


class Request:

    def __init__(self, path, data):
        self.path = path
        self.data = data


class Application:

    def __init__(self, routess):
        self.routess = routess

    def __call__(self, environ, start_response):
        status = "200 OK"
        headers = [("Content-type", "text/html")]

        path = environ["PATH_INFO"]
        request = load_request(environ)

        try:
            handler = self.routess[path]
        except KeyError:
            handler = self.routess["/"]

        start_response(status, headers)

        return handler(request)


def index(request):
    response_body = load_template("index.html")
    return [response_body.substitute().encode()]


def latin(request):
    response_body = load_template("latin.html")
    return [response_body.substitute().encode()]


def university(request):
    response_body = load_template("university.html")
    university_data = request.data

    return [response_body.substitute(university_data).encode()]


def university_response(request):
    form_data = load_request_body(request)
    response_content = f"""
            <h1>{form_data["full_name"][0]} can apply to university</h1>
            """

    return [response_content.encode()]


routes = {
    "/": index,
    "/latin": latin,
    "/university": university,
    "/university_response": university_response
}

application = Application(routes)

HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}/")
    server.serve_forever()

# aplikācijai pievienot
# /university -> universitya ar vārdu, uzvārdu un epastu
# kad sumbit ->
# /name -> parāda vārdu, uzvārdu un epastu
