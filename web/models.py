from django.db import models

# Create your models here.

class Usuario(models.Model):
    identificador = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=45,null=False,default='NN')
    apellido_pat = models.CharField(max_length=45,null=False,default='NN')
    apellido_mat = models.CharField(max_length=45,null=False,default='NN')
    user_name = models.CharField(max_length=45,null=False,default='NN')
    password = models.CharField(max_length=45,null=False,default='NN')
    correo = models.CharField(max_length=145,null=False,default='NN')
    fecha_naci = models.DateField()
    direccion = models.CharField(max_length=150,null=False,default='NN')

    def __str__(self):
        return str(self.nombre)+' '+str(self.user_name)+' '+str(self.password)
