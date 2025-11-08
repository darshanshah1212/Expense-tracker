import csv
from django.shortcuts import render , redirect ,get_object_or_404
from .models import Category , Expense
from .forms import CategoryForm , ExpenseForm
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def export_expenses_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expenses.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Category', 'Amount', 'Date', 'Description'])

    for expense in Expense.objects.all():
        writer.writerow([
            expense.title,
            expense.category.name if expense.category else '',
            expense.amount,
            expense.date,
            expense.description
        ])

    return response


def ExpenseList(request):
    query = request.GET.get('q')
    if query:
        expenses = Expense.objects.filter(title__icontains=query) | Expense.objects.filter(description__icontains=query)
    else:
        expenses = Expense.objects.all()
    return render(request,'expense_list.html',{'expenses':expenses})

def AddExpense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm()
    return render(request,'add_expenses.html',{'form':form})

def EditExpense(request,id):
    expenses = get_object_or_404(Expense,id=id)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST,request.FILES,instance=expenses)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form= ExpenseForm(instance=expenses)
    return render(request,'edit_expenses.html',{'form':form})

def DeleteExpense(request,id):
    expense = get_object_or_404(Expense,id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect("expense_list")
    return render(request,'delete_expenses.html',{'expense':expense})

def CategoriesList(request):
    categories = Category.objects.all()
    return render(request,'categories/categories_list.html',{'categories':categories})

def AddCategories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories_list")
    else:
        form = CategoryForm()
    return render(request,'categories/add_categories.html',{'form':form})

def EditCategories(request,id):
    categories = get_object_or_404(Category,id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=categories)
        if form.is_valid():
            form.save()
            return redirect("categories_list")
    else:
        form = CategoryForm(instance=categories)
    return render(request,'categories/edit_categories.html',{'form':form})    

def DeleteCategories(request,id):
    categories = get_object_or_404(Category,id=id)
    categories.delete()
    return redirect("categories_list")
    