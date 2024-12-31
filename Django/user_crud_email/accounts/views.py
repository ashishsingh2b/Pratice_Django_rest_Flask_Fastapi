import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProductForm
from .models import Product

logger = logging.getLogger('accounts')  # Use your app-specific logger

# User Registration
def register(request):
    logger.debug("Function called: register() - Method: %s", request.method)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("User registered successfully.")
            return redirect('login')
        else:
            logger.warning("Registration form invalid: %s", form.errors)
    else:
        logger.debug("Displaying registration form.")
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

# Product List
@login_required
def product_list(request):
    logger.debug("Function called: product_list() - User: %s", request.user.username)
    products = Product.objects.filter(user=request.user)
    logger.info("Fetched %d products for user: %s", products.count(), request.user.username)
    return render(request, 'product_list.html', {'products': products})

# Product Creation
@login_required
def product_create(request):
    logger.debug("Function called: product_create() - User: %s", request.user.username)
    if not hasattr(request.user, 'profile'):
        logger.warning("User %s has no profile. Redirecting.", request.user.username)
        return redirect('profile_create')

    if request.method == 'POST':
        logger.debug("POST request received for product creation.")
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            logger.info("Product created successfully for user: %s", request.user.username)
            return redirect('product_list')
        else:
            logger.warning("Product form invalid: %s", form.errors)
    else:
        logger.debug("Displaying product creation form.")
        form = ProductForm()

    return render(request, 'product_form.html', {'form': form})








# ## send email with attachment with using signals


# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# from .forms import RegisterForm, ProductForm
# from .models import Product
# from django.conf import settings

# # User Registration
# # your_app/views.py

# from django.shortcuts import render, redirect
# from .forms import RegisterForm  # Assuming you have a registration form

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()  # User is saved automatically, signal will send the email
#             return redirect('login')
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})


# # Product CRUD
# @login_required
# def product_list(request):
#     products = Product.objects.filter(user=request.user)
#     return render(request, 'product_list.html', {'products': products})
# @login_required
# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.user = request.user  # Associate the product with the current user
#             product.save()  # Save the product
#             return redirect('product_list')  # Redirect to the product list
#     else:
#         form = ProductForm()
#     return render(request, 'product_form.html', {'form': form})


# ## send email notifiaction without using signals    

# # from django.shortcuts import render, redirect
# # from django.contrib.auth import login, authenticate
# # from django.contrib.auth.decorators import login_required
# # from django.core.mail import send_mail
# # from .forms import RegisterForm, ProductForm
# # from .models import Product
# # from django.conf import settings

# # # User Registration
# # def register(request):
# #     if request.method == 'POST':
# #         form = RegisterForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
# #             send_mail(
# #                 'Registration Successful',
# #                 f'Hi {user.username}, your registration was successful!',
# #                 settings.EMAIL_HOST_USER,
# #                 [user.email],
# #             )
# #             return redirect('login')
# #     else:
# #         form = RegisterForm()
# #     return render(request, 'register.html', {'form': form})

# # # Product CRUD
# # @login_required
# # def product_list(request):
# #     products = Product.objects.filter(user=request.user)
# #     return render(request, 'product_list.html', {'products': products})

# # @login_required
# # def product_create(request):
# #     if request.method == 'POST':
# #         form = ProductForm(request.POST)
# #         if form.is_valid():
# #             product = form.save(commit=False)
# #             product.user = request.user
# #             product.save()
# #             # Send email
# #             send_mail(
# #                 'New Product Added',
# #                 f'Product "{product.name}" has been successfully added.',
# #                 settings.EMAIL_HOST_USER,
# #                 [request.user.email],
# #             )
# #             return redirect('product_list')
# #     else:
# #         form = ProductForm()
# #     return render(request, 'product_form.html', {'form': form})
    
