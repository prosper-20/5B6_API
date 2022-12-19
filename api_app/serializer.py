from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields= "__all__"

def update(self, instance, validated_data):
            instance.name=validated_data['name', instance.name],
            instance.description=validated_data['description', instance.description],
            instance.price=validated_data['price', instance.price],
            instance.stock=validated_data['stock', instance.stock],
            instance.discount_price=validated_data['discount_price', instance.discount_price], 
            instance.category=validated_data['category', instance.category]
            instance.save()
            return instance



# def create(self, attrs):
#     return super().validate(attrs)


# def create(self, validated_data):
#     return super().create(validated_data)


# def create(self, validated_data):
#     return super().update(instance, validated_data)

class Product2Serializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    description=serializers.CharField(max_length=100)
    price=serializers.DecimalField(max_digits=7, decimal_places=2)
    stock=serializers.CharField(max_length=100)
    discount_price=serializers.DecimalField(max_digits=7, decimal_places=2)
    category=serializers.CharField(max_length=100)
    
    def validate(self, attrs):
        name=attrs.get('name')
        description=attrs['description']
        if name is None:
            raise serializers.ValidationError("name must be provide")
        elif description is None:
            raise serializers.ValidationError("please provide a description")
    
        return attrs


    def create(self, validated_data):
        return Product.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            price=validated_data['price'],
            stock=validated_data['stock'],
            discount_price=validated_data['discount_price'], 
            category=validated_data['category']
    )

    def update(self, instance, validated_data):
            instance.name=validated_data['name', instance.name],
            instance.description=validated_data['description', instance.description],
            instance.price=validated_data['price', instance.price],
            instance.stock=validated_data['stock', instance.stock],
            instance.discount_price=validated_data['discount_price', instance.discount_price], 
            instance.category=validated_data['category', instance.category]
            instance.save()
            return instance