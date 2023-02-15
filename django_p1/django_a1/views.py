from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome Welcome!")

def wah(request):
    text = """<h1>Wah, Wah, Wah, Wah</h1>"""
    return HttpResponse(text)

def HTTPinfo(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['hi'] = 'your name'

    msg = f"""
            <br>Request info
            <br>Path: {path}
            <br>Address: {address}
            <br>Scheme: {scheme}
            <br>Method : {method}
            <br>User agent: {user_agent}
            <br>Path info: {path_info}
            <br>
            <br>Response header: {response.headers}

    """

    return HttpResponse(msg)

def wah_with_params(request, params1):
    query = params1
    wah_dic = {
        "1": "We are here!",
        "2": "We are happy!",
        "3": "We are hungry!",
        "4": "We are !@#$%^",
        "10": "wah"
    }

    wah_str = wah_dic[params1]

    return HttpResponse("<h2> {} WAH is </h2>".format(query) + wah_str)
