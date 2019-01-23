from models import Category

def context_catalog(request):
    return {
        'categories': Category.objects.filter(parent__isnull=True)
    }