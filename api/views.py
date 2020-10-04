from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from api.models import Mem
from api.serializers import MemberSerializer


def index(request):
    return HttpResponse('Hello')


class MemberDetailView(ModelViewSet):
    queryset = Mem.objects.all()
    serializer_class = MemberSerializer
