from django.shortcuts import render
from django.http import HttpResponse
import requests
from . mpesa import AccessToken, Password

def home(request):
    return render(request, 'home.html')

def pay(request):
    return render(request, 'pay.html')

def stk(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        access_token = AccessToken.access_token
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {"Authorization": "Bearer %s" % access_token}

        request = {
           "BusinessShortCode": Password.shortcode,
           "Password": Password.decoded_password,
           "Timestamp": Password.timestamp,
           "TransactionType": "CustomerPayBillOnline",
           "Amount": amount,
           "PartyA": phone,
           "PartyB": Password.shortcode,
           "PhoneNumber": phone,
           "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa",
           "AccountReference":"Stephen",
           "TransactionDesc":"Drawing Fee"
           }

        response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')






# def stk_push(request):
#     if request.method == "POST":
#         phone = request.POST.get('phone')
#         amount = request.POST.get('amount')
#
#         access_token = MpesaAccessToken.validated_token
#
#         api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#
#         headers = {"Authorization": "Bearer %s" % access_token}
#
#
# #
#     request = {
#     "BusinessShortCode": MpesaPassword.shortcode,
#     "Password": MpesaPassword.decoded_password,
#
#     }
#
# redirect('thank_you.html')

# Create your views here.
