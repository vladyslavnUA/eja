import os
from django.db import models

def get_project_cover_path(instance, filename):
    return os.path.join('projects', 'cover_images', filename)

def get_product_cover_path(instance, filename):
    return os.path.join('products', 'cover_images', filename)

def get_additional_image_path(instance, filename):
    return os.path.join('projects', 'additional_images', filename)

def get_additional_pimage_path(instance, filename):
    return os.path.join('products', 'additional_images', filename)

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to=get_project_cover_path, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to=get_product_cover_path, blank=True, null=True)

    def __str__(self):
        return self.title

class AdditionalProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_additional_image_path)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.project.title} - Additional Image"
    
class AdditionalProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='additional_pimages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_additional_pimage_path)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']
        
    def __str__(self):
        return f"{self.product.title} - Additional Image"
        
# def getProjectPath(instance, filename):
#     # File will be uploaded to MEDIA_ROOT/books/<project_name>/<book_title>/<filename>
#     return f'projects/{instance.title}/{filename}'

# def getProductPath(instance, filename):
#     return f'products/{instance.title}/{filename}'

# class Project(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(max_length=9999)
#     cover_image = models.ImageField(upload_to=getProjectPath, blank=True, null=True)
#     additional_images = models.ImageField(upload_to=getProjectPath, blank=True, null=True)

#     def __str__(self):
#         return self.title
    
# class Product(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(max_length=9999)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     cover_image = models.ImageField(upload_to=getProductPath, blank=True, null=True)
#     additional_images = models.ImageField(upload_to=getProductPath, blank=True, null=True)

#     def __str__(self):
#         return self.title
    


# def image_directory_path(instance, filename):
#     if instance.design_project:
#         return f'design_projects/{instance.design_project.title}/{filename}'
#     elif instance.product:
#         return f'products/{instance.product.title}/{filename}'