from django.shortcuts import render

def homepage(request): 
    context = {}
    
    return render(request, 'app/index.html', context)

def about(request): 
    context = {}
    
    return render(request, 'app/about.html', context)

def shop(request): 
    context = {}
    
    return render(request, 'app/shop.html', context)

def shopDetail(request): 
    context = {}
    
    return render(request, 'app/shop-details.html', context)

def contact(request): 
    context = {}
    
    return render(request, 'app/contact.html', context)