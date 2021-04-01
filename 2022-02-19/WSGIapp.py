from wsgiref.simple_server import make_server
from string import Template
from urllib.parse import parse_qsl


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

    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        status = "200 OK"
        headers = [("Content-type", "text/html")]

        path = environ["PATH_INFO"]
        request = load_request(environ)

        try:
            handler = self.routes[path]
        except KeyError:
            handler = self.routes["/"]



        start_response(status, headers)

        return handler(request)


def index(request):
    response_body = load_template("index.html")
    return [response_body.substitute().encode()]


def latin(request):
    response_body = load_template("latin.html")
    return [response_body.substitute().encode()]


def form(request):
    response_body = load_template("form.html")
    return [response_body.substitute().encode()]


def name(request):
    response_body = load_template("name.html")
    form_data = request.data

    return [response_body.substitute(form_data).encode()]


routes = {
    "/": index,
    "/latin": latin,
    "/form": form,
    "/name": name
}


application = Application(routes)

HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}/")
    server.serve_forever()

# aplikācijai pievienot
# /form -> forma ar vārdu, uzvārdu un epastu
# kad sumbit ->
# /name -> parāda vārdu, uzvārdu un epastu