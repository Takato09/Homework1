from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


def index():
    response_content = """
    <h1>Home page!</h1>
    <a href="/university">Go to university data input form </a>
    """
    return [response_content.encode()]

def university():
    response_content = """
        <html>
        <head>
        <script>
            function validateForm() {
                var full_name = document.forms["university"]["full_name"].value;
                var math_rating = document.forms["university"]["math_rating"].value;
                var latvian_rating = document.forms["university"]["latvian_rating"].value;
                var foreign_rating = document.forms["university"]["foreign_rating"].value;
                var full_name_object = document.forms["university"]["full_name"];
                var math_rating_object = document.forms["university"]["math_rating"];
                var latvian_rating_object = document.forms["university"]["latvian_rating"];
                var foreign_rating_object = document.forms["university"]["foreign_rating"];
                if (full_name == ""){
                    alert("Full name must be filled out");
                    full_name_object.style.backgroundColor = "red";
                    return false;
                }else if(math_rating < 1 || math_rating > 100){
                    alert("Math rating must be between 1 and 100");
                    math_rating_object.style.backgroundColor = "red";
                    return false;
                }else if (latvian_rating < 1 || latvian_rating > 100){
                    alert("Latvian rating must be between 1 and 100");
                    latvian_rating_object.style.backgroundColor = "red";
                    return false; 
                }else if (foreign_rating  < 1 || foreign_rating  > 100){
                    alert("Foreign rating must be between 1 and 100");
                    foreign_rating_object.style.backgroundColor = "red";
                    return false;
                }
            }
        </script>
        </head>
        <body>
        <form name="university" action="/univeristy_response" onsubmit="return validateForm()" method="post">
            Full name: <input type="text" name="full_name"><br>
            Math: <input type="text" name="math_rating"><br>
            Latvian language: <input type="text" name="latvian_rating"><br>
            Foreign language: <input type="text" name="foreign_rating"><br>
            <input type="submit">
        </form>
        </body>
        </html>
        """
    return [response_content.encode()]


def univeristy_response(environ):
    try:
        length = int(environ["CONTENT_LENGTH"])
    except ValueError:
        length = 0

    wsgi_input = environ["wsgi.input"].read(length).decode()
    form_data = parse_qs(wsgi_input)

    if int(form_data["math_rating"][0]) and int(form_data["latvian_rating"][0]) and int(
            form_data["foreign_rating"][0]) > 39:
        response_content = f"""
        <h1>{form_data["full_name"][0]} can apply to university</h1>
        """
    else:
        response_content = f"""
        <h1>{form_data["full_name"][0]} can't apply to university</h1>
        """

    return [response_content.encode()]


def application(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/html")]

    path = environ["PATH_INFO"]

    if path == "/university":
        response_content = university()
    elif path == "/univeristy_response":
        response_content = univeristy_response(environ)
    else:
        response_content = index()

    start_response(status, headers)

    return response_content


HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}/")
    server.serve_forever()