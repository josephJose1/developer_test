from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator#pagination
from django.http import Http404
from task1.models import Network
import requests

# Create your views here.
def home(request):
    #return HttpResponse(request,"Hello")
    return render(request, 'task1/home/home.html')

def bikes(request, id="bikesantiago"):
    # obj=get_object_or_404(Network, pk=id)
    datos = company = location = gbfs_href = href = name = stations =None
    page_number=request.GET.get('page',1) #page
    
    try:
        obj = Network.objects.get(pk=id)
        p_ginator_station = Paginator(obj.stations, 50)#paginator
        p_ge_obj = p_ginator_station.get_page(page_number)
        
    except (KeyError, Network.DoesNotExist):       
        auth_endpoint = f"http://api.citybik.es/v2/networks/{id}"
        get_response = requests.get(auth_endpoint)
        if get_response.status_code == 200:
            datos = get_response.json()
            company=datos["network"]["company"]
            name=datos["network"]["name"]
            gbfs_href = datos["network"]["gbfs_href"] 
            href = datos["network"]["href"] 
            location=datos["network"]["location"]
            stations=datos["network"]["stations"]
            
            p_ginator_station=Paginator(stations, 50)#paginator
            p_ge_obj = p_ginator_station.get_page(page_number)
            #save new instance
            mydatos = Network.objects.create(pk=id,company=company,name=name, gbfs_href=gbfs_href, href = href, location=location, stations=stations)
            mydatos.save()
            return render(request, 'task1/index.html', {'list_info':p_ge_obj, 'company':company, 'location':location, 'name':name, 'gbfs_href':gbfs_href, 'href':href})
        else:
            raise Http404
    return render(request, 'task1/index.html', {'list_info':p_ge_obj, 'company':obj.company, 'location':obj.location})

    # p_ginator=Paginator(datos, 6)#paginator
    # p_ge_obj = p_ginator.get_page(page_number)
    # if datos:
    #     return render(request, 'appuserinfo/org_dataset_group/same_copy_custom.html', {'info':main_name,'list_info':p_ge_obj})
    # return render(request, 'appuserinfo/org_dataset_group/same_copy_custom.html', {'info':main_name})