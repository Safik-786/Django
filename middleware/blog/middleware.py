
from django.shortcuts import HttpResponse
from typing import Any


def my_middleware(get_response):
    print("One time Initialization1.")
    def my_function(request):
        print("This is executed before view. (Mother)")
        response= get_response(request)
        print("this is executed after view. (Mother)")
        return response
    return my_function

# def my_middleware2(get_response):
#     print("One time Initialization2.")
#     def my_function(request):
#         print("This is executed before view2.")
#         response= get_response(request)
#         print("this is executed after view2.")
#         return response
#     return my_function

class MyMiddlewareFather:
    def __init__(self, get_response) :
        self.get_response= get_response
        print("One time Initialization2.")
    def __call__(self, request) -> Any:
        print("This is executed before view  (Father).")
        response= self.get_response(request)
        print("This is executed After view  (Father)")
        return response
class MyMiddlewareSon:
    def __init__(self, get_response) :
        self.get_response= get_response
        print("One time Initialization3.")
    def __call__(self, request) -> Any:
        print("This is executed before view  (Son)")
        response= HttpResponse("Site Under Construction.")
        print("This is executed After view2  (Son)")
        return response