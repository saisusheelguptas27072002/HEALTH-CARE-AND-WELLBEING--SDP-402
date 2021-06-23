# Create your views here.
from django.shortcuts import render, redirect
from .forms import *
from .decorators import *
from .filters import fooditemFilter


# Create your views here.

def home(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5]
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5]

    context = {'breakfast': breakfast,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               }
    return render(request, 'main.html', context)


def fooditem(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()
    bcnt = breakfast.count()
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
    lcnt = lunch.count()
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()
    dcnt = dinner.count()
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()
    scnt = snacks.count()
    context = {'breakfast': breakfast,
               'bcnt': bcnt,
               'lcnt': lcnt,
               'scnt': scnt,
               'dcnt': dcnt,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               }
    return render(request, 'fooditem.html', context)


def createfooditem(request):
    form = fooditemForm()
    if request.method == 'POST':
        form = fooditemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'createfooditem.html', context)


def userPage(request):
    fooditems = Fooditem.objects.filter()
    myfilter = fooditemFilter(request.GET, queryset=fooditems)
    fooditems = myfilter.qs
    total = UserFooditem.objects.all()
    myfooditems = total.filter()
    cnt = myfooditems.count()
    querysetFood = []
    for food in myfooditems:
        querysetFood.append(food.fooditem.all())
    finalFoodItems = []
    for items in querysetFood:
        for food_items in items:
            finalFoodItems.append(food_items)
    totalCalories = 0
    for foods in finalFoodItems:
        totalCalories += foods.calorie
    CalorieLeft = 2000 - totalCalories
    context = {'CalorieLeft': CalorieLeft, 'totalCalories': totalCalories, 'cnt': cnt, 'foodlist': finalFoodItems,
               'fooditem': fooditems, 'myfilter': myfilter}
    return render(request, 'user.html', context)


def addFooditem(request):
    user = request.user
    if request.method == "POST":
        form = addUserFooditem(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = addUserFooditem()
    context = {'form': form}
    return render(request, 'addUserFooditem.html', context)
