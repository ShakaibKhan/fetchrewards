from curses.ascii import isalnum
from math import ceil

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from fetchrewards.receipts.models import Receipt
from rest_framework.parsers import JSONParser

from fetchrewards.receipts.serializers import ReceiptSerializer


@csrf_exempt
def process_receipt(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReceiptSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        new_id = serializer.instance.id if serializer.instance.id else {}
        return JsonResponse({"id": new_id}, status=200)
    else:
        return JsonResponse({"error": "Must be a POST request"}, status=400)


@csrf_exempt
def get_points(request, id):
    if request.method == 'GET':
        receipt = Receipt.objects.get(pk=id)
        if receipt is None:
            return JsonResponse({"error-message": "It seems like we do not have a record of that id"}, status=404)

        retailer_name_points = sum([isalnum(x) for x in receipt.retailer])

        round_dollar_points = 50 if receipt.total.split(".")[1] == "00" else 0

        divisible_by_tf_points = 25 if float(receipt.total) % 0.25 == 0 else 0

        item_points = 5 * (len(receipt.items) // 2)

        trim_length_points = 0
        for item in receipt.items:
            if len(item["shortDescription"].strip()) % 3 == 0:
                trim_length_points += ceil(float(item["price"]) * 0.2)
        day_of_purchase_odd_points = 6 if receipt.purchaseDate.day % 2 == 1 else 0

        time_of_purchase_points = 10 if int(receipt.purchaseTime.split(":")[0]) >= 14 and int(
            receipt.purchaseTime.split(":")[0]) <= 16 else 0
        total_points = retailer_name_points + round_dollar_points + divisible_by_tf_points + item_points + trim_length_points + day_of_purchase_odd_points + time_of_purchase_points
        return JsonResponse({
            "points": total_points},
            status=200)
    else:
        return JsonResponse({"error": "request must be a GET request"}, status=200)

# Create your views here.
