from django.shortcuts import render
def home_page(request):
    return render(request,'index.html',{})

def thank_you(request):
    return render(request,'thankyou.html',{})
