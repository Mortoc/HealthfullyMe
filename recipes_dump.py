#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# which this script has hooks to.
#
# On that file, don't forget to add the necessary Django imports
# and take a look at how locate_object() and save_or_locate()
# are implemented here and expected to behave.
#
# This file was generated with the following command:
# ./manage.py dumpscript recipes
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script


IMPORT_HELPER_AVAILABLE = False
try:
    import import_helper
    IMPORT_HELPER_AVAILABLE = True
except ImportError:
    pass

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    #initial imports
    from core.models import Tag
    from core.models import HMUser

    def locate_object(original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        #You may change this function to do specific lookup for specific objects
        #
        #original_class class of the django orm's object that needs to be located
        #original_pk_name the primary key of original_class
        #the_class      parent class of original_class which contains obj_content
        #pk_name        the primary key of original_class
        #pk_value       value of the primary_key
        #obj_content    content of the object which was not exported.
        #
        #you should use obj_content to locate the object on the target db
        #
        #and example where original_class and the_class are different is
        #when original_class is Farmer and
        #the_class is Person. The table may refer to a Farmer but you will actually
        #need to locate Person in order to instantiate that Farmer
        #
        #example:
        #if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #    pk_name="name"
        #    pk_value=obj_content[pk_name]
        #if the_class == StaffGroup:
        #    pk_value=8


        if IMPORT_HELPER_AVAILABLE and hasattr(import_helper, "locate_object"):
            return import_helper.locate_object(original_class, original_pk_name, the_class, pk_name, pk_value, obj_content)

        search_data = { pk_name: pk_value }
        the_obj =the_class.objects.get(**search_data)
        return the_obj

    def save_or_locate(the_obj):
        if IMPORT_HELPER_AVAILABLE and hasattr(import_helper, "save_or_locate"):
            the_obj = import_helper.save_or_locate(the_obj)
        else:
            the_obj.save()
        return the_obj



    #Processing model: UnitOfMeasure

    from recipes.models import UnitOfMeasure

    recipes_unitofmeasure_1 = UnitOfMeasure()
    recipes_unitofmeasure_1.name = u'Cup'
    recipes_unitofmeasure_1 = save_or_locate(recipes_unitofmeasure_1)

    recipes_unitofmeasure_2 = UnitOfMeasure()
    recipes_unitofmeasure_2.name = u'Tbsp.'
    recipes_unitofmeasure_2 = save_or_locate(recipes_unitofmeasure_2)

    recipes_unitofmeasure_3 = UnitOfMeasure()
    recipes_unitofmeasure_3.name = u'Tsp.'
    recipes_unitofmeasure_3 = save_or_locate(recipes_unitofmeasure_3)

    recipes_unitofmeasure_4 = UnitOfMeasure()
    recipes_unitofmeasure_4.name = u'Gallon'
    recipes_unitofmeasure_4 = save_or_locate(recipes_unitofmeasure_4)

    #Processing model: Ingredient

    from recipes.models import Ingredient

    recipes_ingredient_1 = Ingredient()
    recipes_ingredient_1.name = u'Diced Tomato'
    recipes_ingredient_1 = save_or_locate(recipes_ingredient_1)

    recipes_ingredient_2 = Ingredient()
    recipes_ingredient_2.name = u'Jalape\xf1o'
    recipes_ingredient_2 = save_or_locate(recipes_ingredient_2)

    recipes_ingredient_3 = Ingredient()
    recipes_ingredient_3.name = u'Onion'
    recipes_ingredient_3 = save_or_locate(recipes_ingredient_3)

    recipes_ingredient_4 = Ingredient()
    recipes_ingredient_4.name = u'Zucchini'
    recipes_ingredient_4 = save_or_locate(recipes_ingredient_4)

    recipes_ingredient_5 = Ingredient()
    recipes_ingredient_5.name = u'Cilantro'
    recipes_ingredient_5 = save_or_locate(recipes_ingredient_5)

    recipes_ingredient_6 = Ingredient()
    recipes_ingredient_6.name = u'Lime'
    recipes_ingredient_6 = save_or_locate(recipes_ingredient_6)

    recipes_ingredient_7 = Ingredient()
    recipes_ingredient_7.name = u'Salt & Pepper'
    recipes_ingredient_7 = save_or_locate(recipes_ingredient_7)

    recipes_ingredient_8 = Ingredient()
    recipes_ingredient_8.name = u'Black Beans'
    recipes_ingredient_8 = save_or_locate(recipes_ingredient_8)

    recipes_ingredient_9 = Ingredient()
    recipes_ingredient_9.name = u'Mexican Blend Shredded Cheese'
    recipes_ingredient_9 = save_or_locate(recipes_ingredient_9)

    recipes_ingredient_10 = Ingredient()
    recipes_ingredient_10.name = u'Large Whole Wheat Tortilla'
    recipes_ingredient_10 = save_or_locate(recipes_ingredient_10)

    recipes_ingredient_11 = Ingredient()
    recipes_ingredient_11.name = u'Egg'
    recipes_ingredient_11 = save_or_locate(recipes_ingredient_11)

    recipes_ingredient_12 = Ingredient()
    recipes_ingredient_12.name = u'Hot Sauce'
    recipes_ingredient_12 = save_or_locate(recipes_ingredient_12)

    recipes_ingredient_13 = Ingredient()
    recipes_ingredient_13.name = u'Skinless Chicken Thigh'
    recipes_ingredient_13 = save_or_locate(recipes_ingredient_13)

    recipes_ingredient_14 = Ingredient()
    recipes_ingredient_14.name = u'Paprika'
    recipes_ingredient_14 = save_or_locate(recipes_ingredient_14)

    recipes_ingredient_15 = Ingredient()
    recipes_ingredient_15.name = u'Cayenne Pepper'
    recipes_ingredient_15 = save_or_locate(recipes_ingredient_15)

    recipes_ingredient_16 = Ingredient()
    recipes_ingredient_16.name = u'Garlic Salt'
    recipes_ingredient_16 = save_or_locate(recipes_ingredient_16)

    recipes_ingredient_17 = Ingredient()
    recipes_ingredient_17.name = u'Black Pepper'
    recipes_ingredient_17 = save_or_locate(recipes_ingredient_17)

    recipes_ingredient_18 = Ingredient()
    recipes_ingredient_18.name = u'Lemon'
    recipes_ingredient_18 = save_or_locate(recipes_ingredient_18)

    recipes_ingredient_19 = Ingredient()
    recipes_ingredient_19.name = u'Olive Oil'
    recipes_ingredient_19 = save_or_locate(recipes_ingredient_19)

    #Processing model: IngredientListing

    from recipes.models import IngredientListing

    recipes_ingredientlisting_1 = IngredientListing()
    recipes_ingredientlisting_1.amount_numerator = 2
    recipes_ingredientlisting_1.amount_denominator = 3
    recipes_ingredientlisting_1.unit = recipes_unitofmeasure_1
    recipes_ingredientlisting_1.ingredient = recipes_ingredient_1
    recipes_ingredientlisting_1.notes = u''
    recipes_ingredientlisting_1.optional = False
    recipes_ingredientlisting_1 = save_or_locate(recipes_ingredientlisting_1)

    recipes_ingredientlisting_2 = IngredientListing()
    recipes_ingredientlisting_2.amount_numerator = 1
    recipes_ingredientlisting_2.amount_denominator = 1
    recipes_ingredientlisting_2.unit = None
    recipes_ingredientlisting_2.ingredient = recipes_ingredient_2
    recipes_ingredientlisting_2.notes = u''
    recipes_ingredientlisting_2.optional = False
    recipes_ingredientlisting_2 = save_or_locate(recipes_ingredientlisting_2)

    recipes_ingredientlisting_3 = IngredientListing()
    recipes_ingredientlisting_3.amount_numerator = 1
    recipes_ingredientlisting_3.amount_denominator = 1
    recipes_ingredientlisting_3.unit = None
    recipes_ingredientlisting_3.ingredient = recipes_ingredient_2
    recipes_ingredientlisting_3.notes = u'(minced)'
    recipes_ingredientlisting_3.optional = False
    recipes_ingredientlisting_3 = save_or_locate(recipes_ingredientlisting_3)

    recipes_ingredientlisting_4 = IngredientListing()
    recipes_ingredientlisting_4.amount_numerator = 1
    recipes_ingredientlisting_4.amount_denominator = 4
    recipes_ingredientlisting_4.unit = recipes_unitofmeasure_1
    recipes_ingredientlisting_4.ingredient = recipes_ingredient_3
    recipes_ingredientlisting_4.notes = u'(diced, for zucchini mixture)'
    recipes_ingredientlisting_4.optional = False
    recipes_ingredientlisting_4 = save_or_locate(recipes_ingredientlisting_4)

    recipes_ingredientlisting_5 = IngredientListing()
    recipes_ingredientlisting_5.amount_numerator = 2
    recipes_ingredientlisting_5.amount_denominator = 1
    recipes_ingredientlisting_5.unit = recipes_unitofmeasure_2
    recipes_ingredientlisting_5.ingredient = recipes_ingredient_3
    recipes_ingredientlisting_5.notes = u'(diced)'
    recipes_ingredientlisting_5.optional = False
    recipes_ingredientlisting_5 = save_or_locate(recipes_ingredientlisting_5)

    recipes_ingredientlisting_6 = IngredientListing()
    recipes_ingredientlisting_6.amount_numerator = 1
    recipes_ingredientlisting_6.amount_denominator = 1
    recipes_ingredientlisting_6.unit = None
    recipes_ingredientlisting_6.ingredient = recipes_ingredient_4
    recipes_ingredientlisting_6.notes = u'(diced)'
    recipes_ingredientlisting_6.optional = False
    recipes_ingredientlisting_6 = save_or_locate(recipes_ingredientlisting_6)

    recipes_ingredientlisting_7 = IngredientListing()
    recipes_ingredientlisting_7.amount_numerator = 1
    recipes_ingredientlisting_7.amount_denominator = 4
    recipes_ingredientlisting_7.unit = recipes_unitofmeasure_1
    recipes_ingredientlisting_7.ingredient = recipes_ingredient_5
    recipes_ingredientlisting_7.notes = u'(chopped and packed)'
    recipes_ingredientlisting_7.optional = False
    recipes_ingredientlisting_7 = save_or_locate(recipes_ingredientlisting_7)

    recipes_ingredientlisting_8 = IngredientListing()
    recipes_ingredientlisting_8.amount_numerator = 1
    recipes_ingredientlisting_8.amount_denominator = 1
    recipes_ingredientlisting_8.unit = None
    recipes_ingredientlisting_8.ingredient = recipes_ingredient_6
    recipes_ingredientlisting_8.notes = u'(juiced)'
    recipes_ingredientlisting_8.optional = False
    recipes_ingredientlisting_8 = save_or_locate(recipes_ingredientlisting_8)

    recipes_ingredientlisting_9 = IngredientListing()
    recipes_ingredientlisting_9.amount_numerator = 0
    recipes_ingredientlisting_9.amount_denominator = 1
    recipes_ingredientlisting_9.unit = None
    recipes_ingredientlisting_9.ingredient = recipes_ingredient_7
    recipes_ingredientlisting_9.notes = u'to taste'
    recipes_ingredientlisting_9.optional = False
    recipes_ingredientlisting_9 = save_or_locate(recipes_ingredientlisting_9)

    recipes_ingredientlisting_10 = IngredientListing()
    recipes_ingredientlisting_10.amount_numerator = 1
    recipes_ingredientlisting_10.amount_denominator = 2
    recipes_ingredientlisting_10.unit = recipes_unitofmeasure_1
    recipes_ingredientlisting_10.ingredient = recipes_ingredient_8
    recipes_ingredientlisting_10.notes = u'(drained)'
    recipes_ingredientlisting_10.optional = False
    recipes_ingredientlisting_10 = save_or_locate(recipes_ingredientlisting_10)

    recipes_ingredientlisting_11 = IngredientListing()
    recipes_ingredientlisting_11.amount_numerator = 1
    recipes_ingredientlisting_11.amount_denominator = 2
    recipes_ingredientlisting_11.unit = recipes_unitofmeasure_1
    recipes_ingredientlisting_11.ingredient = recipes_ingredient_9
    recipes_ingredientlisting_11.notes = u''
    recipes_ingredientlisting_11.optional = False
    recipes_ingredientlisting_11 = save_or_locate(recipes_ingredientlisting_11)

    recipes_ingredientlisting_12 = IngredientListing()
    recipes_ingredientlisting_12.amount_numerator = 2
    recipes_ingredientlisting_12.amount_denominator = 1
    recipes_ingredientlisting_12.unit = None
    recipes_ingredientlisting_12.ingredient = recipes_ingredient_10
    recipes_ingredientlisting_12.notes = u''
    recipes_ingredientlisting_12.optional = False
    recipes_ingredientlisting_12 = save_or_locate(recipes_ingredientlisting_12)

    recipes_ingredientlisting_13 = IngredientListing()
    recipes_ingredientlisting_13.amount_numerator = 2
    recipes_ingredientlisting_13.amount_denominator = 1
    recipes_ingredientlisting_13.unit = None
    recipes_ingredientlisting_13.ingredient = recipes_ingredient_11
    recipes_ingredientlisting_13.notes = u''
    recipes_ingredientlisting_13.optional = False
    recipes_ingredientlisting_13 = save_or_locate(recipes_ingredientlisting_13)

    recipes_ingredientlisting_14 = IngredientListing()
    recipes_ingredientlisting_14.amount_numerator = 0
    recipes_ingredientlisting_14.amount_denominator = 1
    recipes_ingredientlisting_14.unit = None
    recipes_ingredientlisting_14.ingredient = recipes_ingredient_12
    recipes_ingredientlisting_14.notes = u''
    recipes_ingredientlisting_14.optional = True
    recipes_ingredientlisting_14 = save_or_locate(recipes_ingredientlisting_14)

    recipes_ingredientlisting_15 = IngredientListing()
    recipes_ingredientlisting_15.amount_numerator = 2
    recipes_ingredientlisting_15.amount_denominator = 1
    recipes_ingredientlisting_15.unit = None
    recipes_ingredientlisting_15.ingredient = recipes_ingredient_13
    recipes_ingredientlisting_15.notes = u''
    recipes_ingredientlisting_15.optional = False
    recipes_ingredientlisting_15 = save_or_locate(recipes_ingredientlisting_15)

    recipes_ingredientlisting_16 = IngredientListing()
    recipes_ingredientlisting_16.amount_numerator = 2
    recipes_ingredientlisting_16.amount_denominator = 1
    recipes_ingredientlisting_16.unit = recipes_unitofmeasure_2
    recipes_ingredientlisting_16.ingredient = recipes_ingredient_14
    recipes_ingredientlisting_16.notes = u''
    recipes_ingredientlisting_16.optional = False
    recipes_ingredientlisting_16 = save_or_locate(recipes_ingredientlisting_16)

    recipes_ingredientlisting_17 = IngredientListing()
    recipes_ingredientlisting_17.amount_numerator = 2
    recipes_ingredientlisting_17.amount_denominator = 1
    recipes_ingredientlisting_17.unit = recipes_unitofmeasure_3
    recipes_ingredientlisting_17.ingredient = recipes_ingredient_15
    recipes_ingredientlisting_17.notes = u''
    recipes_ingredientlisting_17.optional = False
    recipes_ingredientlisting_17 = save_or_locate(recipes_ingredientlisting_17)

    recipes_ingredientlisting_18 = IngredientListing()
    recipes_ingredientlisting_18.amount_numerator = 2
    recipes_ingredientlisting_18.amount_denominator = 1
    recipes_ingredientlisting_18.unit = recipes_unitofmeasure_3
    recipes_ingredientlisting_18.ingredient = recipes_ingredient_16
    recipes_ingredientlisting_18.notes = u''
    recipes_ingredientlisting_18.optional = False
    recipes_ingredientlisting_18 = save_or_locate(recipes_ingredientlisting_18)

    recipes_ingredientlisting_19 = IngredientListing()
    recipes_ingredientlisting_19.amount_numerator = 1
    recipes_ingredientlisting_19.amount_denominator = 1
    recipes_ingredientlisting_19.unit = recipes_unitofmeasure_3
    recipes_ingredientlisting_19.ingredient = recipes_ingredient_17
    recipes_ingredientlisting_19.notes = u''
    recipes_ingredientlisting_19.optional = False
    recipes_ingredientlisting_19 = save_or_locate(recipes_ingredientlisting_19)

    recipes_ingredientlisting_20 = IngredientListing()
    recipes_ingredientlisting_20.amount_numerator = 1
    recipes_ingredientlisting_20.amount_denominator = 1
    recipes_ingredientlisting_20.unit = None
    recipes_ingredientlisting_20.ingredient = recipes_ingredient_18
    recipes_ingredientlisting_20.notes = u'(juiced)'
    recipes_ingredientlisting_20.optional = False
    recipes_ingredientlisting_20 = save_or_locate(recipes_ingredientlisting_20)

    recipes_ingredientlisting_21 = IngredientListing()
    recipes_ingredientlisting_21.amount_numerator = 1
    recipes_ingredientlisting_21.amount_denominator = 4
    recipes_ingredientlisting_21.unit = recipes_unitofmeasure_1
    recipes_ingredientlisting_21.ingredient = recipes_ingredient_19
    recipes_ingredientlisting_21.notes = u''
    recipes_ingredientlisting_21.optional = False
    recipes_ingredientlisting_21 = save_or_locate(recipes_ingredientlisting_21)

    recipes_ingredientlisting_22 = IngredientListing()
    recipes_ingredientlisting_22.amount_numerator = 1
    recipes_ingredientlisting_22.amount_denominator = 2
    recipes_ingredientlisting_22.unit = recipes_unitofmeasure_4
    recipes_ingredientlisting_22.ingredient = recipes_ingredient_11
    recipes_ingredientlisting_22.notes = u''
    recipes_ingredientlisting_22.optional = True
    recipes_ingredientlisting_22 = save_or_locate(recipes_ingredientlisting_22)

    recipes_ingredientlisting_23 = IngredientListing()
    recipes_ingredientlisting_23.amount_numerator = 20
    recipes_ingredientlisting_23.amount_denominator = 1
    recipes_ingredientlisting_23.unit = None
    recipes_ingredientlisting_23.ingredient = recipes_ingredient_6
    recipes_ingredientlisting_23.notes = u''
    recipes_ingredientlisting_23.optional = False
    recipes_ingredientlisting_23 = save_or_locate(recipes_ingredientlisting_23)

    #Processing model: RecipeImg

    from recipes.models import RecipeImg

    recipes_recipeimg_1 = RecipeImg()
    recipes_recipeimg_1.url = u'http://2.bp.blogspot.com/-5GjI_Pbhu00/UW4C7zh74hI/AAAAAAAABVM/GlnZsmq61gk/s640/IMG_0736.JPG'
    recipes_recipeimg_1 = save_or_locate(recipes_recipeimg_1)

    recipes_recipeimg_2 = RecipeImg()
    recipes_recipeimg_2.url = u'http://4.bp.blogspot.com/-nn5GeQueqMA/UW4DDlOjgOI/AAAAAAAABVc/rLb62vK6AXw/s640/IMG_0746.JPG'
    recipes_recipeimg_2 = save_or_locate(recipes_recipeimg_2)

    recipes_recipeimg_3 = RecipeImg()
    recipes_recipeimg_3.url = u'http://1.bp.blogspot.com/-vrrTH2NZbyU/UW4CrmNV22I/AAAAAAAABUs/3NBgvYqA9II/s640/IMG_0730.JPG'
    recipes_recipeimg_3 = save_or_locate(recipes_recipeimg_3)

    recipes_recipeimg_4 = RecipeImg()
    recipes_recipeimg_4.url = u'http://2.bp.blogspot.com/-qjkluUBlNhw/UW4CxBn4UvI/AAAAAAAABU8/3DH7sYDg0-s/s640/IMG_0731.JPG'
    recipes_recipeimg_4 = save_or_locate(recipes_recipeimg_4)

    recipes_recipeimg_5 = RecipeImg()
    recipes_recipeimg_5.url = u'http://3.bp.blogspot.com/-YQM5g1h9tps/UW4DGUR7L7I/AAAAAAAABVo/-ryC0r0rjXM/s640/IMG_0752.JPG'
    recipes_recipeimg_5 = save_or_locate(recipes_recipeimg_5)

    recipes_recipeimg_6 = RecipeImg()
    recipes_recipeimg_6.url = u'http://media.tumblr.com/1ce4207d7913c8545af8cda6cab3b729/tumblr_inline_mlopynX2LX1qz4rgp.jpg'
    recipes_recipeimg_6 = save_or_locate(recipes_recipeimg_6)

    recipes_recipeimg_7 = RecipeImg()
    recipes_recipeimg_7.url = u'http://media.tumblr.com/cc66b9fb738b92b5154cbf02e62f12be/tumblr_inline_mloq6kQECF1qz4rgp.jpg'
    recipes_recipeimg_7 = save_or_locate(recipes_recipeimg_7)

    recipes_recipeimg_8 = RecipeImg()
    recipes_recipeimg_8.url = u'http://2.bp.blogspot.com/-5GjI_Pbhu00/UW4C7zh74hI/AAAAAAAABVM/GlnZsmq61gk/s640/IMG_0736.JPG'
    recipes_recipeimg_8 = save_or_locate(recipes_recipeimg_8)

    #Processing model: Recipe

    from recipes.models import Recipe

    recipes_recipe_1 = Recipe()
    recipes_recipe_1.title = u'Spicy Lemon Paprika Chicken Thighs'
    recipes_recipe_1.instructions = u'1. Preheat the oven to 425 degrees<br/>\r\n<br/>\r\n2. Mix the paprika, cayenne, garlic salt, pepper, lemon juice and olive oil together in a big bowl<br/>\r\n<br/>\r\n3. Add the chicken thighs into the mixture and it marinate for a few hours. HOWEVER, this marinade actually tastes pretty good \r\neven without the wait :) I left it in the mixture for 5 minutes before throwing it into the oven<br/>\r\n<br/>\r\n4. Place the chicken on a baking sheet/pan and bake the pieces for 15 minutes, or until thoroughly cooked. This will depend on the size/thickness of your chicken<br/>\r\n<br/>\r\n5. Optional: Turn the oven into broiling mode if you want to make the chicken crispy<br/>'
    recipes_recipe_1.attribution = u'happychomp'
    recipes_recipe_1.attribution_link = u'http://www.happychomp.com/post/48660128323/how-to-make-spicy-lemon-paprika-chicken-thighs'
    recipes_recipe_1.created_by =  locate_object(HMUser, "id", HMUser, "id", 1, {'first_name': u'', 'last_name': u'', 'is_staff': True, 'receives_newsletter': False, 'is_active': True, 'id': 1, 'is_superuser': False, 'is_legacy': False, 'last_login': datetime.datetime(2013, 4, 23, 22, 58, 1, 428163, tzinfo=<UTC>), 'created_date': datetime.datetime(2013, 4, 23, 16, 16, 49, 573016, tzinfo=<UTC>), 'is_admin': True, 'password': u'pbkdf2_sha256$10000$IeC53v8xHpsk$6m9FC2+VQgkxiKd9jjnuDt5/dBKv+MvwJuElaZKZvBM=', 'email': u'mortoc@healthfully.me'} ) 
    recipes_recipe_1.created_date = datetime.datetime(2013, 4, 23, 18, 47, 53, tzinfo=<UTC>)
    recipes_recipe_1.serves = 2
    recipes_recipe_1.prep_time_hours = 0
    recipes_recipe_1.prep_time_minutes = 30
    recipes_recipe_1.refrigeration_life_days = 4
    recipes_recipe_1 = save_or_locate(recipes_recipe_1)

    recipes_recipe_1.ingredient_list.add(recipes_ingredientlisting_15)
    recipes_recipe_1.ingredient_list.add(recipes_ingredientlisting_16)
    recipes_recipe_1.ingredient_list.add(recipes_ingredientlisting_17)
    recipes_recipe_1.ingredient_list.add(recipes_ingredientlisting_18)
    recipes_recipe_1.ingredient_list.add(recipes_ingredientlisting_19)
    recipes_recipe_1.ingredient_list.add(recipes_ingredientlisting_20)
    recipes_recipe_1.ingredient_list.add(recipes_ingredientlisting_21)
    recipes_recipe_1.images.add(recipes_recipeimg_6)
    recipes_recipe_1.images.add(recipes_recipeimg_7)

    recipes_recipe_2 = Recipe()
    recipes_recipe_2.title = u'Veggie Loaded Huevos Rancheros'
    recipes_recipe_2.instructions = u"1. Prepare pico de gallo. Mix diced tomato, jalape\xf1o, 2 tbsp onion, cilantro, lime juice, and generous sprinkle of salt & pepper in a small bowl. Set aside.<br/>\r\n<br/>\r\n2. Prepare zucchini mixture. Heat 1 tbsp extra virgin olive oil in a large skillet over medium heat. Add zucchini and 1/4 cup onion and saute (stirring frequently), uncovered, until onions soften and zucchini begins to brown, about 5 minutes. Sprinkle with salt & pepper and set aside in a small bowl.<br/>\r\n<br/>\r\n3. Prepare tortilla. In a toaster oven, bake tortilla at 425\xb0f until it browns and crisps, almost to the point of burning. (If you don't have a toaster oven you can do this in a regular oven or crisp via stovetop in the large skillet over high heat, covered, turning over once.) Place tortilla on serving plate.<br/>\r\n<br/>\r\n4. Cook eggs. Spray large skillet with cooking spray or coat with an olive oil mister over high heat. Crack eggs over pan. When edges start to brown and crackle (about 1-2 minutes) gently flip eggs over, being careful not to break the yolk. Cook for another 2 minutes, and then set atop respective tortillas.<br/>\r\n<br/>\r\n5. Sprinkle 1 tbsp of cheese over the egg. Divide zucchini mixture evenly over two tortillas, and add another tbsp of cheese. Add beans to each tortilla along with a third tbsp of cheese. Top off tortillas with evenly divided pico de gallo, and garnish with last tablespoon of cheese. Serve with hot sauce, if desired. Buen Provecho!<br/>"
    recipes_recipe_2.attribution = u'kitchenkvell'
    recipes_recipe_2.attribution_link = u'http://www.kitchenkvell.com/2013/04/veggie-loaded-huevos-rancheros.html'
    recipes_recipe_2.created_by =  locate_object(HMUser, "id", HMUser, "id", 1, {'first_name': u'', 'last_name': u'', 'is_staff': True, 'receives_newsletter': False, 'is_active': True, 'id': 1, 'is_superuser': False, 'is_legacy': False, 'last_login': datetime.datetime(2013, 4, 23, 22, 58, 1, 428163, tzinfo=<UTC>), 'created_date': datetime.datetime(2013, 4, 23, 16, 16, 49, 573016, tzinfo=<UTC>), 'is_admin': True, 'password': u'pbkdf2_sha256$10000$IeC53v8xHpsk$6m9FC2+VQgkxiKd9jjnuDt5/dBKv+MvwJuElaZKZvBM=', 'email': u'mortoc@healthfully.me'} ) 
    recipes_recipe_2.created_date = datetime.datetime(2013, 4, 23, 18, 22, 11, tzinfo=<UTC>)
    recipes_recipe_2.serves = 2
    recipes_recipe_2.prep_time_hours = 0
    recipes_recipe_2.prep_time_minutes = 30
    recipes_recipe_2.refrigeration_life_days = 0
    recipes_recipe_2 = save_or_locate(recipes_recipe_2)

    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_1)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_3)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_4)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_5)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_6)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_7)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_8)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_9)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_10)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_11)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_12)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_13)
    recipes_recipe_2.ingredient_list.add(recipes_ingredientlisting_14)
    recipes_recipe_2.images.add(recipes_recipeimg_1)
    recipes_recipe_2.images.add(recipes_recipeimg_2)
    recipes_recipe_2.images.add(recipes_recipeimg_3)
    recipes_recipe_2.images.add(recipes_recipeimg_4)
    recipes_recipe_2.images.add(recipes_recipeimg_5)

    #Re-processing model: Recipe

    recipes_recipe_1.tags.add(  locate_object(Tag, "id", Tag, "id", 2, {'text': u'Paleo', 'id': 2} )  )

    recipes_recipe_2.tags.add(  locate_object(Tag, "id", Tag, "id", 1, {'text': u'Mexican', 'id': 1} )  )

