from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.shortcuts import render
from .other_api import get_random_fact, get_weather
from django.http import JsonResponse
from django.views import View
import requests

class CallCropAPI(View):
    def post(self, request):
        # Assuming the API endpoint and payload
        api_url = "https://1vk8d5k11e.execute-api.eu-west-1.amazonaws.com/crop_api_stage/x23109831_cropproj"
        payload = {"crop": "rice"}

        try:
            # Making the POST request
            response = requests.post(api_url, json=payload)
            
            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Returning the response from the API
                return JsonResponse(response.json())
            else:
                # If the request was not successful, return an error message
                return JsonResponse({"error": "Failed to call the API"}, status=500)
        except Exception as e:
            # If an exception occurs during the request, return an error message
            return JsonResponse({"error": str(e)}, status=500)
 
def random_fact_view(request):
    fact = get_random_fact()
    city = "Dublin"  # Default city
    weather_data = get_weather(city)
    return render(request, 'random_fact.html', {'fact': fact, 'weather_data': weather_data})
# def home(request):
#     isActive=True
#     if request.method=='POST':
#          check=request.POST.get("check")
#          print(check)
#          if check is  None: isActive=False
#          else: isActive=True


    # date=datetime.datetime.now()
    # name="LearnCodeWithDurgesh"
    # list_of_programs=[
    #     'WAP to check even or odd',
    #     'WAP to check prime number',
    #     'WAP to print all prime numbers from 1 to 100',
    #     'WAP to print pascals triangle'
    # ]
    # student={
    #     'student_name':"Rahul",
    #     'student_college':"ZYZ",
    #     'student_city':'LUCKNOW'
    # }
    # return HttpResponse("<h1>Hello this is index page  </h1> "+str(date))
    # data={
    #     'date':date,
    #     'isActive':isActive,
    #     'name':name,
    #     'list_of_programs':list_of_programs,
    #     'student_data':student
    # }
#     return render(request,"home.html",{})
#
# def about(request):
#     return render(request,"about.html",{})
#
# def services(request):
#     return render(request,"services.html",{})
