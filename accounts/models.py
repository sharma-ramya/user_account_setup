from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.



class AdminUser(AbstractUser):
    """
    Defining different types of admins here, 
    for ease of use later on

    """

    L1_ADMIN = 'L1'
    L2_ADMIN = 'L2'
    L3_ADMIN = 'L3'

    ADMIN_CHOICES = (
    	( L1_ADMIN, "L1 ADMIN"),
    	( L2_ADMIN, "L2 ADMIN"),
    	( L3_ADMIN, "L3 ADMIN"),
    	
    )
    pass
    # add additional fields in here
    
    admin_level = models.CharField(
    	max_length = 2,
    	choices=ADMIN_CHOICES,
    	default = L1_ADMIN,
	)

    def __str__(self):
        return self.username

class Plan(models.Model):
	"""
	The subscription plan that a customer's wallet is subscribed to
	Might be changed later on
	"""
	PREPAID = 'PR'
	POSTPAID = 'PO'

	PLAN_CHOICES = [
		(PREPAID, "Prepaid"),
		(POSTPAID, "Postpaid"),

	]

	plan_style = models.CharField(
        max_length = 2,
        choices = PLAN_CHOICES,
        default = PREPAID , #default customer activity is inactive
    )


	description = models.CharField(max_length = 100)
	
	#check if something need to be changed here
	plan_amount = models.FloatField()





class Customer(models.Model):
	"""
	Defining the Customer details for the admin
	To be filled up/saved by the admin
	"""

	ACTIVE = 'A'
	INACTIVE = 'I'
	RESTRICTED = 'R'

	ACTIVE_CHOICES = [
		(ACTIVE, "Active"),
		(INACTIVE, "Inactive"),
		(RESTRICTED, "Restricted"),
		#('B', "Blocked")

	]


	name = models.CharField(max_length = 100)
	username = models.CharField(max_length = 100, unique = True)
	email = models.EmailField()
	phone = models.CharField(max_length = 10)
	admin_id = models.ForeignKey(
		AdminUser, 
		models.DO_NOTHING,
		db_column = 'username',
		)
	active_status = models.CharField(
        max_length = 1,
        choices = ACTIVE_CHOICES,
        default = INACTIVE , #default customer activity is inactive
    )

	#will be changed later on
	wallet_id = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)

	def __str__(self):
		return '' + self.username

	def is_active(self):
		return self.active_status in {self.ACTIVE}



