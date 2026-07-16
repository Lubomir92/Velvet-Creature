from django.contrib import admin

from .models import Product, Category, ProductImage



class ProductImageInline(admin.TabularInline):

    model = ProductImage

    extra = 1



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "stock",
        "featured",
    )

    list_filter = (
        "category",
        "featured",
    )

    search_fields = (
        "name",
        "description",
        "material",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    inlines = [
        ProductImageInline,
    ]



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }



@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "created",
    )