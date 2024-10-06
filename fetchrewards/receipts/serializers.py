from rest_framework import serializers
from fetchrewards.receipts.models import Receipt


class ReceiptSerializer(serializers.Serializer):
    def create(self, stream):
        stream = self.initial_data
        new_receipt = {"purchaseDate": stream['purchaseDate'], "purchaseTime": stream['purchaseTime'],
                       "retailer": stream['retailer'], "total": stream['total']}

        items = []
        for item in stream['items']:
            items.append({'price': item['price'], 'shortDescription': item['shortDescription']})
        new_receipt["items"] = items
        return Receipt.objects.create(**new_receipt)
