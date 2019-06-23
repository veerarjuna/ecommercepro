from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class CustomMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print("Process Custom Middleware")

    def process_response(self, request, response):
        print("Process Custom Response")
