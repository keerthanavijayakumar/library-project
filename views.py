from django.shortcuts import render
from django.http import HttpResponse
from libapp.models import Books,UserData,GeneralDepartment,IssuedBooks
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from libapp.models import UserData,IssuedBooks,Books 
import csv
from reportlab.pdfgen import canvas 


def index(request):
	return render(request,'login.html')

def booksimg(request):
	return render(request,'image.html')



def register(request):
	return render(request,'create_user.html')

def loginpage(request):
	return render(request,'login.html')

def allbooks(request):
	return render(request,'all_book.html')

def adduser(request):
	return render(request,'create_user.html')

def registeruser(request):
	
	user_name = request.POST.get('t2')
	user_mailid=request.POST.get('t3')
	user_address=request.POST.get('t4')
	user_phoneno=request.POST.get('t5')
	user_city=request.POST.get('t6')
	print(user_name ,' : ', user_mailid ,' : ',user_address,' : ',user_phoneno,' : ',user_city)
	u1 = UserData()
	
	u1.user_name = user_name
	u1.user_mailid =user_mailid
	u1.user_address =user_address
	u1.user_phoneno =user_phoneno
	u1.user_city =user_city
	u1.save()
	id=UserData.objects.latest('user_id')
	print(id)  
	return render(request,'registeruser.html',{'user_id':id})


def addbooks(request):
	return render(request,'create_books.html')

def registerbooks(request):
	
	book_name = request.POST.get('t2')
	book_auther=request.POST.get('t3')
	book_price=request.POST.get('t4')
	published_year=request.POST.get('t5')
	available_copies=request.POST.get('t6')
	book_images=request.POST.get('t7')
	print(book_name ,' : ', book_auther ,' : ',book_price,' : ',published_year,' : ',available_copies ,' : ',book_images)
	u1 = Books()
	
	u1.book_name = book_name
	u1.book_auther =book_auther
	u1.book_price =book_price
	u1.published_year =published_year
	u1.available_copies =available_copies
	u1.book_images=book_images
	u1.save()
	id=Books.objects.latest('book_id')
	print(id)  
	return render(request,'registerbooks.html',{'book_id':id})


def adddept(request):
	return render(request,'create_department.html')

def registerdept(request):
	
	dept_name = request.POST.get('t2')
	dept_headname=request.POST.get('t3')
	print(dept_name ,' : ', dept_headname)
	u1 = GeneralDepartment()
	
	u1.dept_name = dept_name
	u1.dept_headname =dept_headname
	
	u1.save()
	id=GeneralDepartment.objects.latest('dept_id')
	print(id)  
	return render(request,'registerdept.html',{'dept_id':id})


# def AddissuedBooks(request):
# 	return render(request,'create_issued_books.html')

def issuedbooks(request):
	bobj=Books.objects.all()
	uobj=UserData.objects.all()
	return render(request,'issued_books_details.html',{'book_obj':bobj,'user_obj':uobj})

def registerissuedBooks(request):
	print('Entered')
	bookid = request.POST.get('bookid')
	userid = request.POST.get('userid')
	issue_date = request.POST.get('t2')
	remarks=request.POST.get('t3')
	print('Book Id  : ', bookid)
	print('User Id  : ', userid)
	print('issue date : ', issue_date)
	print('Remarks : ', remarks)

	# bobj=Books.objects.all()
	# uobj=UserData.objects.all()
	 
	u1 = IssuedBooks()
	u1.bookid=bookid
	u1.userid=userid
	u1.issue_date = issue_date
	u1.remarks =remarks
	
	u1.save()
	#id=IssuedBooks.objects.latest('book_id') 
	# print(id) 
	return render(request,'issuedbooks.html')
 

def uid_issuedbooks(request):
	
	return render(request,'uid_view_issuedbook.html')

def viewissuedbooks(request):
	print('Entered')
	uid = request.POST.get('t2')
	print('User Id  : ', uid)                                                   
	uobj=IssuedBooks.objects.filter(user_id=uid)
	udata=UserData.objects.get(user_id=uid)
	return render(request,'uid_issued.html',{'uobj':uobj,'udata':udata})


def taken_booksname(request):
	
	return render(request,'bname_view_userdetails.html')

def viewtakenbooks(request):
	print('Entered')
	bookname = request.POST.get('t2')
	print('BOOK NAME : ', bookname)                                                   
	bobj=Books.objects.filter(book_name=bookname)
	
	return render(request,'bname_issuedbooks.html',{'bobj':bobj})      


def lend(request,bookid):
	print('lend')
	print('Passed Book Id',bookid)

	
	return render(request,'lend_issued_books_details.html',{'bookid':bookid})

def lendbooks(request):
	print('lendbooks')

	bookid=request.POST.get('t5')
	userid = request.POST.get('t4')
	issue_date = request.POST.get('t2')
	remarks=request.POST.get('t3')

	print('bookid:',bookid)
	print('User Id  : ', userid)
	print('issue date : ', issue_date)
	print('Remarks : ', remarks)

	user=UserData.objects.get(user_id=userid)
	book=Books.objects.get(book_id=bookid)
	print(book) 
	u1 = IssuedBooks()

	
	u1.book_id=book
	u1.user_id=user

	u1.issue_date = issue_date
	u1.remarks =remarks
	u1.save()
	return render(request,'issuedbooks.html',{'book':book,'user':user})







 
def loginpage2(request):

	print('this is loginpage')
	
	return render(request,'login.html')

def login02(request):

	print('Entered')
	userid = request.POST.get('t2')
	password = request.POST.get('t3')
	print('USER ID : ', userid)   
	print('PASSWORD :',password) 
	
	uobj=UserData.objects.filter(user_id=userid,user_mailid=password).exists()
	if 	uobj:
		print('user login success')
		return render(request,'loginuser.html',{'userid':userid})
	else:
		print('Invalid user')
		return render(request,'invaild.html')


def userissueddetail(request,userid):
	print('Passed user Id',userid)
	uobj=IssuedBooks.objects.filter(user_id=userid)
	udata=UserData.objects.get(user_id=userid)
	return render(request,'uid_issued.html',{'uobj':uobj,'udata':udata})
	# return render(request,'userissueddetail.html',{'uobj':uobj})
	

def userpersonal(request,userid):
	print('Passed user Id',userid)
	uobj=UserData.objects.filter(user_id=userid)
	return render(request,'one_user_detail.html',{'uobj':uobj})
	

def logout(request):
	print('User Logout')
	return render(request,'logout.html')


def admin(request):

	return render(request,'admin.html')

def admin2(request):
	print('Admin')
	userid = request.POST.get('t2')
	password = request.POST.get('t3')
	print('USER ID : ', userid)   
	print('PASSWORD :',password) 
	#return render(request,'admin2.html')

	if userid=='1234' and password=='admin':
		print('Admin login success')
		return render(request,'admin2.html')
	else:
		print('Invalid Admin')
		return render(request,'invaildadmin.html')


def getfile(request): 
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="userdetails.csv"'
	uobj = UserData.objects.all()
	writer = csv.writer(response)
	for u in uobj:
		writer.writerow([u.usercategory,u.user_id,u.user_name,u.user_mailid,u.user_address,u.user_phoneno,u.user_city])  
	return response 


def getuser(request): 
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="userdetails.csv"'
	uobj = UserData.objects.filter(user_id=1)
	writer = csv.writer(response)
	for u in uobj:
		writer.writerow([u.usercategory,u.user_id,u.user_name,u.user_mailid,u.user_address,u.user_phoneno,u.user_city])  
	return response 

def GetIssuedData(request): 
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="IssuedDetails.csv"'
	Iobj = IssuedBooks.objects.all()
	writer = csv.writer(response)
	for u in Iobj:
		writer.writerow([u.book_id,u.user_id,u.issue_date,u.return_date,u.remarks])  
	return response 

def GetBookData(request): 
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="BookDetails.csv"'
	bobj = Books.objects.all()
	writer = csv.writer(response)
	for u in bobj:
		writer.writerow([u.book_id,u.dept_id,u.book_name,u.book_auther,u.book_price,u.published_year,u.available_copies,u.book_images])  
	return response 


def getpdf(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="hello.pdf"'
	p = canvas.Canvas(response)
	bobj = Books.objects.all()
	p.drawString(100,700, "welcome to our library")  
	p.showPage()
	p.save()  
	return response     




class ViewAllBooks(ListView):
	model=Books
	template_name="image.html"

class ViewAlluser(ListView):
	model=UserData 
	template_name="view_all_user.html"

class Createnewuser(CreateView):
	model=UserData
	fields = "__all__"
	template_name='create_user.html'
	def newusers(request):
		return render(request,'newreg.html',{'user_id':id})

class ViewAllDepart(ListView):
	model=GeneralDepartment
	template_name="alldept.html"

class Createnewdept(CreateView):
	model=GeneralDepartment
	fields = "__all__"
	template_name='create_dept.html'   

class Addnewbooks(CreateView):
	model=Books
	fields = "__all__"
	template_name='Add_new_Books.html'

class Issuedbooks(CreateView):
	model=IssuedBooks
	fields = "__all__"
	template_name='issued_books.html'


class ViewOneUserData(DetailView):
	model=UserData
	template_name='view_one_user.html'


class ViewOneIssuedBook(DetailView):
	model=IssuedBooks
	template_name='view_one_issuedbooks.html'







def welcomeuser(request):
	return render(request,'welcome.html')

         



