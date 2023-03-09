from django.shortcuts import render

def test():
    
        mytest = (
            "Hello world"
        )
        return mytest

def index(request):
        mytest = test()
        return render(request, 'esd_home/index.html', {'test': mytest})
