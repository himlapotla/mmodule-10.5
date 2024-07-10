from django.shortcuts import render
import datetime

# Create your views here.
def home(request):


    d = {'listt': ['Python is best', 'And i love it', 'This is my future'], 
        'time': datetime.datetime.now(), 'number': 100, 'word': 'django', 'cut': 'this , is , our , country',
        'llst': [    {'name': 'Josh', 'age': 19}, {'name': 'h', 'age': 90},
                     {'name': 'Dave', 'age': 22},
                {'name': 'Joe', 'age': 31}], 'list':  ['Jane', 'Janet', 'Joe'],
                'lst':  ['Apple', 'Mango', 'Orange'], 'lstt':  ['Apple', 'Mango', 'Orange'],
                'line': 'this is a sunny day and we are loving it.', 'random': ['Apple', 'Mango', 'Orange'],
                 'num_messages': 5,    }
    

    return render(request, 'home.html', d)