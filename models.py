from django.db import models

# Create your models here.

class User(models.Model):  # 1
    id = models.IntegerField(primary_key=True)
    avatar = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250, null=False, unique=True)
    email = models.CharField(max_length=250, null=False, unique=True)
    password = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=250)
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)

class Address(models.Model):  # 2
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title =  models.CharField(max_length=250)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    postal_code =  models.CharField(max_length=250)
    landmark = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)
    
class Category(models.Model):  # 3
    id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=250)
    description =  models.CharField(max_length=250)
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)

class SubCategory(models.Model): # 4
    id = models.IntegerField(primary_key=True)
    parent_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name =  models.CharField(max_length=250)
    description =  models.CharField(max_length=250)
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)

class Product(models.Model): # 5
    id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=250)
    description =  models.CharField(max_length=250)
    cover =  models.CharField(max_length=250)
    category_id =  models.ForeignKey(SubCategory, max_length=250, on_delete=models.CASCADE)
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)

class ProductAttribute(models.Model): # 6
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)
    
class ProductSKU(models.Model): # 7
    id = models.ForeignKey(ProductAttribute, primary_key=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_attribute = models.ForeignKey(ProductAttribute, related_name='size_attribute', on_delete=models.CASCADE)
    color_attribute = models.ForeignKey(ProductAttribute, related_name='color_attribute', on_delete=models.CASCADE)
    sku = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    quantity = models.IntegerField()
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)

class Wishlist(models.Model): # 8
    id = models.ForeignKey(ProductSKU, primary_key=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)

class Cart(models.Model): # 9
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)

class CartItem(models.Model): # 10
    id = models.IntegerField(primary_key=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    products_sku_id = models.ForeignKey(ProductSKU, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)

class OrderDetails(models.Model): # 11
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.IntegerField()
    total = models.IntegerField()
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)

class OrderItem(models.Model): # 12
    id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    products_sku_id = models.ForeignKey(ProductSKU, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)
    
class PaymentDetails(models.Model): # 13
    id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    amount = models.IntegerField()
    provider = models.CharField(max_length=250)
    status = models.CharField(max_length=255)
    created_at =  models.DateTimeField(auto_now_add=True)
    deleted_at =  models.DateTimeField(auto_now=True)
