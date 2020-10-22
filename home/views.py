from django.shortcuts import render, redirect, HttpResponse
import random
# Create your views here.

def index(request):
    x = random.randrange(0, 10)
    y = random.randrange(0,10)

    z = request.POST['problem1']
    problem_string = ''
    problem_string += str(x)
    problem_string += '+'
    problem_string += str(y)
    problem_string += '='

    if z == x*y:
        print("Yayyyyy you are correct")
    else:
        print("You are a dumbass!")
        print("The correct answer is:", x+y)

    context = {
        'problem' : problem_string
    }
    return render(request, 'index.html', context)

#def addition(request):
    #return render(request, 'index.html', context)