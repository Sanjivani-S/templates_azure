import pymssql
from django.shortcuts import render
from django.http import HttpResponse
from app_templates.models import User1
#from learning_templates import forms

# Create your views here.

def index(request):
    return render(request,'index.html')

def other(request):
    return render(request,'other.html')

def relative(request):
    return render (request, 'relative_url_templates.html')

def home(request):
    return render (request, 'home.html')

def details(request):
    return render(request, 'post_detail.html')

def users(request):
    #records = get_data()    

    #users_list = User1.objects.order_by('f_nm')
    #order_by('rec_date')

    users_list=get_data()
    users_dict = {'user_records':users_list}
    return render(request, 'users.html',context= users_dict)

def get_data():   
    conn = pymssql.connect(
        server='FirstServer-sgs.database.windows.net',
        user='FirstUser',
        password='idntknw12#',
        database='FirstDB',
        as_dict=True
    )

    cursor = conn.cursor()

    select_query = "select * from myTable"
    cursor.execute(select_query)
    records = cursor.fetchall()

    print ("\n inside views.py\nFirst name \t Last name \t email\n")
    for r in records:
        print(f"{r['FirstName']}\t\t{r['LastName']}\t\t {r['email']} ")

    if conn:        
        conn.close()
        print ("DB saved and connection closed")

    return records