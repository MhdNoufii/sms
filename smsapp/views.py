from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from twilio.rest import Client

# Create your views here.
def index(request):
    return render(request,"smsform.html")

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        print("Its Post")

        to = request.POST.get('to')
        msg = request.POST.get('msg')
        print( to, msg)

        SID = "AC612ff4249ad617e10e172b7642a565ba"
        token = "f7bd859814ca1bf3ea500f745233befb"
        fromm_num = "+19789060759"

        try:
            clt = Client(SID, token)
            mssg = clt.messages.create(
                body= msg,
                from_= fromm_num,
                to= to
            )
            return HttpResponse("SMS Sent Successfully")
        
        except Exception as e :
            return HttpResponse(f"Failed to send SMS : {e}")
        
    return render(request, "smsform.html")

