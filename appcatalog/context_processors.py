from models import Category
from .helpers import *


def context_catalog(request):
    print(tree_catalog())
    return {
        'categories': tree_catalog()
    }
