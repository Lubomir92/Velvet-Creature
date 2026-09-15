from django.contrib import admin
from django.utils.html import format_html
import cloudinary

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

    readonly_fields = ["video_upload_widget"]

    fieldsets = (
        ("Základné informácie", {
            "fields": ("name", "slug", "description", "short_description")
        }),
        ("Obrázok", {
            "fields": ("image",)
        }),
        ("Informácie o produkte", {
            "fields": ("sku", "material", "size", "weight")
        }),
        ("Cena a sklad", {
            "fields": ("price", "stock", "featured")
        }),
        ("Kategória", {
            "fields": ("category",)
        }),
        ("Video", {
            "fields": ("video_url", "video_upload_widget")
        }),
    )

    def video_upload_widget(self, obj):
        cloud_name = cloudinary.config().cloud_name or ""
        return format_html("""
            <script src="https://upload-widget.cloudinary.com/global/all.js" type="text/javascript"></script>
            <button type="button" id="upload_widget" style="
                padding: 10px 20px;
                background: #d4af37;
                color: #0a0a0a;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-weight: 700;
                font-size: 14px;
            ">📹 Nahrať video</button>
            <p id="video_status" style="color: #d4af37; margin-top: 10px;"></p>
            <script>
                var myWidget = cloudinary.createUploadWidget({{
                    cloudName: '{cloud_name}',
                    uploadPreset: 'velvet_video_preset',
                    resourceType: 'video',
                    sources: ['local', 'url', 'camera'],
                    multiple: false,
                    maxFileSize: 40000000
                }}, (error, result) => {{
                    if (!error && result && result.event === "success") {{
                        document.getElementById("video_status").innerHTML =
                            '✅ Video nahraté!';
                        var urlField = document.getElementById("id_video_url");
                        if (urlField) {{
                            urlField.value = result.info.secure_url;
                        }}
                    }}
                }});
                document.getElementById("upload_widget").addEventListener("click", function(){{
                    myWidget.open();
                }}, false);
            </script>
        """, cloud_name=cloud_name)

    video_upload_widget.short_description = "Nahrať video cez Cloudinary"