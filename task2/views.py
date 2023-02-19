from django.shortcuts import render
from django.http import HttpResponse
from task2.utilidad import main_process,save_json
from task2.models import Project
from django.core.paginator import Paginator#pagination
from django.http import Http404

# Create your views here.
def ambiental(request):
    '''START FUNCTION  TO SCRAP WEBSITE'''
    page_number=request.GET.get('page',1) #pagination
    words_keys=[
        'noid', 'nombre', 'tipo', 'region', 'tipologia', 'titular', 'inversion', 'fechapresentacion', 'estado', 'mapa',]#declare values
    typelist=[
        'number', 'string', 'string', 'string', 'string', 'string', 'string', 'number', 'string', 'string']#datatype    
    
    if request.method == 'POST':
        main_process()#scrap website
        # print("running!!!")
        
    info = Project.objects.all()
    paginator=Paginator(info, 10) # Show 10 projects per page.
    if int(page_number) > paginator.num_pages:
        print(f"my val {page_number} and the limit {paginator.num_pages} set to {paginator.num_pages}")
        page_obj = paginator.get_page(paginator.num_pages)
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(paginator.num_pages)
    elif int(page_number) == 0:
        raise Http404("Page does not exist")
    else:
        page_obj = paginator.get_page(page_number)
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    #return HttpResponse(request,"Hello")
    return render(request, 'task2/scraper.html', {'info':page_obj, "val":words_keys, "typeList":typelist,})

def ambientalData(request):
    
    page_number=request.GET.get('page',1) #pagination
    words_keys=[
        'noid', 'nombre', 'tipo', 'region', 'tipologia', 'titular', 'inversion', 'fechapresentacion', 'estado', 'mapa',]#declare values
    typelist=[
        'number', 'string', 'string', 'string', 'string', 'string', 'string', 'number', 'string', 'string'
        ]#datatype
    
    
    #scrap website
    #main_process()
    info = Project.objects.all()
    paginator=Paginator(info, 10) # Show 10 projects per page.
    if int(page_number) > paginator.num_pages:
        print(f"my val {page_number} and the limit {paginator.num_pages} set to {paginator.num_pages}")
        page_obj = paginator.get_page(paginator.num_pages)
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(paginator.num_pages)
    elif int(page_number) == 0:
        raise Http404("Page does not exist")
    else:
        page_obj = paginator.get_page(page_number)
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    #return HttpResponse(request,"Hello")
    return render(request, 'task2/scraper.html', {'info':page_obj, "val":words_keys, "typeList":typelist,})