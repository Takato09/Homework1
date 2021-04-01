from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import datetime


def form(environ):

    method = environ["REQUEST_METHOD"]

    if method == "GET":
        response_content = """
    <form action="" method="post">
    Title: <input type="text" name="title"><br>
    Content: <input type="text" name="content"><br>
    <input type="submit">
    </form>
    """
    elif method == "POST":
        try:
            length = int(environ["CONTENT_LENGTH"])
        except ValueError:
            length = 0

        wsgi_input = environ["wsgi.input"].read(length).decode()
        form_data = parse_qs(wsgi_input)

        response_content = f"""
        <h1>{form_data["title"][0]}</h1>
        {datetime.datetime.now()} 
        <p>{form_data["content"][0]}</p>
        """

    return [response_content.encode()]


def application(environ, start_response):

    status = "200 OK"
    headers = [("Content-type", "text/html; charset=utf-8")]

    path = environ["PATH_INFO"]

    if path == "/":
        response_content = form(environ)
    else:
        response_content = "Not found"

    start_response(status, headers)

    return response_content


HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}")
    server.serve_forever()