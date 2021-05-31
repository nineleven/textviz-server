from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SampleText
from .logic import encode_text
from .serializers import SampleTextsSerializer, SpecificTextSerializer


class SampleTextsView(APIView):
    def get(self, request):
        texts = SampleText.objects.all()
        serializer = SampleTextsSerializer(texts, many=True)
        return Response(serializer.data)

    
class SpecificTextView(APIView):
    def get(self, request):
        text_name = request.GET['name'].replace('+', ' ')
        text = SampleText.objects.filter(name__startswith=text_name)[0]
        serializer = SpecificTextSerializer(text, many=False)
        return Response(serializer.data)


class EncodeTextsView(APIView):
    # @csrf_exempt
    def post(self, request):
        text = request.body.decode('utf-8')
        words, codes = encode_text(text)

        return Response({'words': words,
                         'codes': codes})
