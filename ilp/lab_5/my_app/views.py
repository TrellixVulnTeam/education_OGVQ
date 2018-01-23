from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def hello_view(request):
    return HttpResponse('hello world')

class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')

class StaticView(View):
    def get(self, request):
        return render(request, 'static_page.html', {'years': [1, 2, 1, 3, 5, 8]})

class OrdersView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id':1},
                {'title': 'Второй заказ', 'id':2},
                {'title': 'Третий заказ', 'id':3},
            ]
        }
        return render(request, 'orders.html', data)

class OrderView(View):
    def get(self, request, id):
        data = {
            'order': {
                'id':id
            }
        }
        return render(request, 'order.html', data)