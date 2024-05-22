import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from phonepe.sdk.pg.payments.v1.payment_client import PhonePePaymentClient
import uuid
from phonepe.sdk.pg.payments.v1.models.request.pg_pay_request import PgPayRequest


def home(request):
    return render(request, 'home.html')


def payment_gateway(request):
    ##################################################################################################
    # PHONEPE CODE
    ##################################################################################################
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            ##################################################################################################
            # PHONEPE CODE - You can place your PhonePe payment processing logic here
            ##################################################################################################
            phonepe_client = PhonePePaymentClient(merchant_id=settings.PHONEPE_MERCHANT_ID,
                                                  salt_key=settings.PHONEPE_SALT_KEY,
                                                  salt_index=int(settings.PHONEPE_SALT_INDEX), env=settings.PHONEPE_ENV)
            unique_transaction_id = str(uuid.uuid4())
            ui_redirect_url = settings.REDIRECT_BASE_URL + reverse("success")
            s2s_callback_url = settings.REDIRECT_BASE_URL + reverse("success")
            amount_in_paise = int(amount) * 100
            id_assigned_to_user_by_merchant = None  # Replace with User id for unique user tracking
            pay_request = PgPayRequest.pay_page_pay_request_builder(merchant_transaction_id=unique_transaction_id,
                                                                    amount=amount_in_paise,
                                                                    merchant_user_id=id_assigned_to_user_by_merchant,
                                                                    callback_url=s2s_callback_url,
                                                                    redirect_url=ui_redirect_url)
            pay_page_response = phonepe_client.pay(pay_request)
            pay_page_url = pay_page_response.data.instrument_response.redirect_info.url
            return render(request, 'payment.html', context={'payment_url': pay_page_url, 'amount': amount})
    return HttpResponseRedirect(reverse('home'))


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')
