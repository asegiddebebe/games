from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
	person = {'name':'Asegid', 'age': 52}
	return Response(person)