from django.db import models

# Create your models here.




class GeneralDepartment(models.Model):
	dept_id=models.AutoField(primary_key=True)
	dept_name=models.CharField(max_length=100)
	dept_headname=models.CharField(max_length=50)

	class Meta:
		db_table='generaldepartment'
		verbose_name='Generaldepartment'

class Books(models.Model):
	dept_id = models.ForeignKey(GeneralDepartment, default=1, verbose_name="Generaldepartment", on_delete=models.SET_DEFAULT)
	book_id=models.AutoField(primary_key=True)
	book_name=models.CharField(max_length=100)
	book_auther=models.CharField(max_length=100)
	book_price=models.IntegerField()
	published_year=models.IntegerField()
	available_copies=models.IntegerField()
	'''MEDIA_URL = '/images/' '''
	book_images=models.ImageField(blank=True,null=True)


	class Meta:
		db_table='books'
		verbose_name='bookdata'

user_category=(
	('student','STUDENT'),
	('staff','STAFF'),

	)
class UserData(models.Model):
	usercategory=models.CharField(max_length=10,choices=user_category,default='staff')
	user_id=models.AutoField(primary_key=True)
	user_name=models.CharField(max_length=100)
	user_mailid=models.CharField(max_length=100)
	user_address=models.CharField(max_length=200)
	user_phoneno=models.IntegerField()
	user_city=models.CharField(max_length=100)
 
	class Meta:
		db_table='userdata'
		verbose_name='Userdetails'

class IssuedBooks(models.Model):

	book_id = models.ForeignKey(Books, default=1, verbose_name="bookdata", on_delete=models.SET_DEFAULT)
	user_id = models.ForeignKey(UserData, default=1, verbose_name="Userdetails", on_delete=models.SET_DEFAULT)
	
	issue_date=models.DateField(default=None,null=True)
	return_date=models.DateField(default=None,null=True)
	fine_amount=models.IntegerField(default=0,null=True)
	remarks=models.CharField(max_length=100,default=None,null=True)

	class Meta:
		db_table='issuedbooks'
		verbose_name='issuebook'
	
