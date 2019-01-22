from models import Category

def context_catalog(request):
    return {
        'categories': Category.objects.all()
    }