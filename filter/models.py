from django.db import models
from django.core import validators

# Create your models here.


class INDUSTRIAL_PRODUCTS(models.Model):
    
    PRODUCT_ID = models.IntegerField(primary_key=True)
    PRODUCT_TITLE = models.CharField(max_length=1000, null = True,blank=True,verbose_name="اسم المنتج")
    
    def __str__(self):
        return str(self.PRODUCT_TITLE) 
    class Meta:
        app_label = 'filter'
        ordering=['PRODUCT_TITLE']#could be wrong needs checking
        db_table = r'"IDA"."INDUSTRIAL_PRODUCTS"' 
        managed = False 
class FACILITY_DATA(models.Model):
    FACILITY_DATA_ID=models.CharField(max_length=50,unique=True)
    FACILITY_ID = models.CharField(max_length=1000,primary_key=True)
    NAME = models.CharField(max_length=100, null = True,blank=True,verbose_name="اسم المنشأه")
    CEO_NAME= models.CharField(max_length=200, null = True,blank=True,verbose_name="المدير")
    DETAILED_ADDRESS=models.CharField(max_length=200, null = True,blank=True,verbose_name="العنوان")
    PRIMARY_MOBILE=models.CharField(max_length=100, null = True,blank=True,verbose_name="الموبايل")
    Prouducts = models.ManyToManyField(INDUSTRIAL_PRODUCTS, through='FACILITY_PRODUCTS',verbose_name="المنتجات",related_name='ty')
    def __str__(self):
        return str(self.NAME) 
    def Productquantities(self):
   
        return FACILITY_PRODUCTS.objects.filter(FACILITY_ID=self.pk).order_by("PRODUCT_ID")
        
        # return FACILITY_PRODUCTS.objects.filter(Factory_ID=self.pk, PRODUCT_ID__in= self.Prouducts.pk)
    class Meta:
        ordering=['FACILITY_ID']
        app_label = 'filter'
        managed = False
        db_table = r'"IDA"."FACILITY_DATA"'

class INDUSTRIAL_REGISTRY(models.Model):
        
    REGISTRY_ID = models.CharField(max_length=50,unique=True,primary_key=True)
    FACILITY_DATA=models.ForeignKey(FACILITY_DATA, to_field='FACILITY_DATA_ID',db_column='FACILITY_DATA_ID' ,related_name='my', on_delete=models.CASCADE)
    REGISTRY_NUMBER=models.CharField(max_length=100)
    def __str__(self):
        return str(self.REGISTRY_NUMBER) 
    class Meta:
        app_label = 'filter'
        db_table = r'"IDA"."INDUSTRIAL_REGISTRY"'  
        managed = False
class MEASURING_UNITS (models.Model):
    UNIT_ID = models.DecimalField( max_digits=38, decimal_places=0,primary_key=True)
    UNIT_TITLE_AR=   models.CharField(max_length=50)
    def __str__(self):
        return str(self.UNIT_TITLE_AR)
    class Meta:
           db_table = r'"IDA"."MEASURING_UNITS"'
           managed = False
           app_label = 'filter' 

class FACILITY_PRODUCTS(models.Model):
    FAC_PROD_ID=models.CharField(max_length=50,primary_key=True)
    FACILITY_ID= models.ForeignKey(FACILITY_DATA,to_field='FACILITY_ID',db_column='FACILITY_ID',on_delete=models.CASCADE)
    PRODUCT_ID= models.ForeignKey(INDUSTRIAL_PRODUCTS,to_field='PRODUCT_ID',db_column='PRODUCT_ID',on_delete=models.CASCADE)
    UNIT_ID =models.ForeignKey(MEASURING_UNITS  ,related_name='ty' ,to_field='UNIT_ID',db_column='UNIT_ID',on_delete=models.CASCADE)
    PRODUCT_QUANTITY = models.DecimalField( max_digits=38, decimal_places=3)
       
    def __str__(self):
        return str(self.PRODUCT_QUANTITY) 
       
    class Meta:
        app_label = 'filter'
        #ordering = ["PRODUCT_ID"]
        managed = False
        db_table = r'"IDA"."FACILITY_PRODUCTS"'

