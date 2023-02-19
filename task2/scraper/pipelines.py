from task2.models import Project

def save_item(*args, **kwars):
    '''create new obj with project model and save it!!'''
    print(args)
    
    obj = Project.objects.filter(noid=args[0])
    if not obj:
    
        item_create= Project.objects.create(
        noid=args[0],
        nombre=args[1],
        tipo=args[2],
        region=args[3],
        tipologia=args[4],
        titular=args[5],
        inversion=args[6],
        fechapresentacion=args[7],
        estado=args[8],
        mapa=args[9],
        )
        
        item_create.save()
    
    else:
        print(f"Key (noid)=({args[0]}) already exists.")

def count_table(cantidadperpage):    
    '''HOW MANY RECORDS are saved IN OUR DB'''
    cant = Project.objects.count()
    return int(cant/cantidadperpage)
        
def get_data():
    return Project.objects.all().order_by('noid').values()

