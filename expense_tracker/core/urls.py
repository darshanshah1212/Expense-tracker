from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
   path('',views.ExpenseList,name="expense_list"),
   path('AddExpenses/',views.AddExpense,name="add_expenses"),
   path('EditExpenses/<int:id>/',views.EditExpense,name="edit_expenses"),
   path('DeleteExpenses/<int:id>/',views.DeleteExpense,name="delete_expenses"),
   path('Catergories/',views.CategoriesList,name="categories_list"),
   path('Catergories/Add/',views.AddCategories,name="add_categories"),
   path('Catergories/edit/<int:id>/',views.EditCategories,name="edit_categories"),
   path('Catergories/delete/<int:id>/',views.DeleteCategories,name="delete_categories"),
   path('export/csv/', views.export_expenses_csv, name='export_expenses_csv')
]