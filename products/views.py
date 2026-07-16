from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Avg

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Product, Category, ProductImage
from .forms import ProductForm, ProductImageForm

from wishlist.models import Wishlist

from orders.models import Order
from custom_orders.models import CustomOrder

from reviews.models import Review
from reviews.forms import ReviewForm


def shop(request):

    category_slug = request.GET.get("category")
    search_query = request.GET.get("search")


    products = Product.objects.all().order_by("-created")


    categories = Category.objects.all()



    # CATEGORY FILTER

    if category_slug:

        products = products.filter(
            category__slug=category_slug
        )



    # SEARCH

    if search_query:

        products = products.filter(
        Q(name__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(short_description__icontains=search_query) |
        Q(material__icontains=search_query)
    )



    wishlist_products = []



    if request.user.is_authenticated:

        wishlist_products = list(
            Wishlist.objects.filter(
                user=request.user
            ).values_list(
                "product_id",
                flat=True
            )
        )



    return render(
        request,
        "products/shop.html",
        {
            "products": products,
            "wishlist_products": wishlist_products,
            "categories": categories,
            "search_query": search_query,
        }
    )





def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug
    )


    reviews = Review.objects.filter(
        product=product
    ).order_by(
        "-created"
    )


    average_rating = reviews.aggregate(
        Avg("rating")
    )["rating__avg"]



    if request.method == "POST":


        if not request.user.is_authenticated:

            messages.error(
                request,
                "Please login to write a review."
            )

            return redirect(
                "product_detail",
                slug=product.slug
            )



        if Review.objects.filter(
            product=product,
            user=request.user
        ).exists():

            messages.error(
                request,
                "You have already reviewed this product."
            )

            return redirect(
                "product_detail",
                slug=product.slug
            )



        review_form = ReviewForm(
            request.POST
        )


        if review_form.is_valid():

            review = review_form.save(
                commit=False
            )

            review.product = product
            review.user = request.user

            review.save()


            messages.success(
                request,
                "Thank you for your review!"
            )


            return redirect(
                "product_detail",
                slug=product.slug
            )


    else:

        review_form = ReviewForm()



    related_products = Product.objects.filter(
        category=product.category
    ).exclude(
        id=product.id
    )[:3]


    gallery = product.images.all()



    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "gallery": gallery,
            "related_products": related_products,

            "reviews": reviews,
            "average_rating": average_rating,
            "review_form": review_form,
        }
    )
@staff_member_required
def admin_dashboard(request):

    context = {
        "products_count": Product.objects.count(),
        "orders_count": Order.objects.count(),
        "custom_orders_count": CustomOrder.objects.count(),
    }

    return render(
        request,
        "admin/dashboard.html",
        context,
    )
@staff_member_required
def admin_products(request):

    products = Product.objects.all().order_by("name")

    return render(
        request,
        "admin/products.html",
        {
            "products": products
        }
    )
@staff_member_required
def edit_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )


    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            product = form.save(
            commit=False
            )

            product.save()


            return redirect(
                "admin_products"
            )


    else:

        form = ProductForm(
            instance=product
        )


    return render(
        request,
        "admin/edit_product.html",
        {
            "form": form,
            "product": product
        }
    )

@staff_member_required
def add_product(request):

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            product = form.save(
            commit=False
            )

            from django.utils.text import slugify

            product.slug = slugify(
                product.name
            )

            product.save()


            return redirect(
                "admin_products"
            )


    else:

        form = ProductForm()


    return render(
        request,
        "admin/add_product.html",
        {
            "form": form
        }
    )

@staff_member_required
def delete_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )


    if request.method == "POST":

        product.delete()

        return redirect(
            "admin_products"
        )


    return render(
        request,
        "admin/delete_product.html",
        {
            "product": product
        }
    )

@staff_member_required
def product_gallery(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )


    images = product.images.all()


    if request.method == "POST":

        form = ProductImageForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            image = form.save(
                commit=False
            )

            image.product = product

            image.save()


            return redirect(
                "product_gallery",
                product_id=product.id
            )


    else:

        form = ProductImageForm()


    return render(
        request,
        "admin/product_gallery.html",
        {
            "product": product,
            "images": images,
            "form": form
        }
    )
