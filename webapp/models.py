from django.db import models

# Create your models here.
class onlineuser(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	gender=models.CharField(max_length=100);
	age=models.CharField(max_length=100);




class queries(models.Model):
    q_n=models.CharField(max_length=1000);
    an_s=models.CharField(max_length=1000);



class Description(models.Model):
    Disease=models.CharField(max_length=1000);
    Description=models.CharField(max_length=1000);




class precautions(models.Model):
    Disease=models.CharField(max_length=1000);
    Precaution_1=models.CharField(max_length=1000);
    Precaution_2=models.CharField(max_length=1000);
    Precaution_3=models.CharField(max_length=1000);
    Precaution_4=models.CharField(max_length=1000);



class chat(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	message=models.CharField(max_length=5000);



class doctors(models.Model):
    Disease=models.CharField(max_length=1000);
    docid=models.CharField(max_length=100);
    name=models.CharField(max_length=100);
    designation=models.CharField(max_length=1000);
    address=models.CharField(max_length=1000);


class bookings(models.Model):
    docid=models.CharField(max_length=100);
    docname=models.CharField(max_length=100);
    pname=models.CharField(max_length=100);
    pemail=models.CharField(max_length=100);
    dat_e=models.CharField(max_length=1000);
    tim_e=models.CharField(max_length=1000);
    stz=models.CharField(max_length=100);


class performance(models.Model):
    alg_name = models.CharField(max_length=100)
    sc1 = models.FloatField()
    sc2 = models.FloatField()
    sc3 = models.FloatField()
    sc4 = models.FloatField()



    