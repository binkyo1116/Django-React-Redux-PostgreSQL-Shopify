from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product, Order, OrderItem, ShippingAddress, Review

class UserSerializer(serializers.ModelSerializer):
    name= serializers.SerializerMethodField(read_only=True)
    _id= serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        #creating custom fields to send back more specific info, we can redo our modals but this is much simpler for smaller projects
        fields=['id','_id', 'username', 'email', 'name', 'isAdmin' ]
    
    def get_isAdmin(self,userObj):
        return userObj.is_staff
    
    def get__id(self,userObj):
        return userObj.id
        
    def get_name(self, userObj):
        name= userObj.first_name
        if name == '':
            name = userObj.email
        return name
    
    
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= User
        fields= ['id','_id', 'username', 'email', 'name', 'isAdmin', 'token' ]
    #requesting access token instead of refresh token, refresh token provide a request to get access tokens in order to access confidential info
    def get_token(self, userObj):
        token= RefreshToken.for_user(userObj)
        return str(token.access_token)
    
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
            
class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields='__all__'
        
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
        
class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
    
#nesting orderItems, shippingAddress, user serializers into one nested serializers to return as a complete order serializer 
class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderItems(self, obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data

    def get_shippingAddress(self, obj):
        try:
            address = ShippingAddressSerializer(
                obj.shippingaddress, many=False).data
        except:
            address = False
        return address

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data  
