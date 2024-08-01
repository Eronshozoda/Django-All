from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from .models import GeeksModel

class MyView(View):
	def get(self, request):
		# <view logic>
		return HttpResponse('result')
	

class GeeksCreate(CreateView):
	
    model=GeeksModel
	
    fields=['title','description']
	


