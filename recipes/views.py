from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, Template
from django.conf import settings

from recipes.models import Recipe

def view_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=int(recipe_id))
    
    icon = None
    try:
        icon = recipe.images.all()[0].url
    except:
        pass
    
    return render(request, "view-recipe.html", {
        "recipe" : recipe,
        "icon" : icon
    })