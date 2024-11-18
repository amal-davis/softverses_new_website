from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.conf import settings




def home(request):
    content = CenterSection.objects.first()
    logos = ClientLogo.objects.all()  
    section = MissionVision.objects.all() 
    designs = WebDesign.objects.all() 
    blogs = BlogPost.objects.all().order_by('-created_at')[:4]
    bloge = BlogPost.objects.all().order_by('-created_at')[:2]

    faqs = FAQ.objects.all()
    return render (request,'home.html', {'content': content , 'logos': logos , 'section': section , 
'designs': designs , 'blogs': blogs , 'faqs': faqs,'bloge':bloge})


def add_center(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        subheading = request.POST.get('subheading')
        paragraph = request.POST.get('paragraph')
        button_text = request.POST['button_text']
        button_url = request.POST['button_url']
        
    
        # Save the data to the database
        content = CenterSection.objects.create(
            heading=heading,
            paragraph=paragraph,
            subheading=subheading,
            button_text=button_text,
            button_url=button_url
        )
        # Redirect or do other actions after saving
        return redirect('add_center')  # Replace 'success_page' with your actual success page URL

    add_center = CenterSection.objects.all()
    return render(request, 'add_home_center.html', {'add_center': add_center})


def edit_center(request, content_id):
    content = get_object_or_404(CenterSection, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        heading = request.POST.get('heading',content.heading)
        subheading = request.POST.get('subheading',content.subheading)
        paragraph = request.POST.get('paragraph',content.paragraph)
        button_text = request.POST.get('button_text',content.button_text)
        button_url = request.POST.get('button_url',content.button_url)
        
       

        # Update the SwiperContent instance with the new data
        content.heading = heading
        content.subheading = subheading
        content.paragraph = paragraph
        content.button_text = button_text
        content.button_url = button_url
       
        
        content.save()

        return redirect('add_center')  # Redirect to the Swiper view after editing

    return render(request, 'edit_home_center.html', {'content': content})



def delete_center(request, opening_id):
    content = get_object_or_404(CenterSection, id=opening_id)
    content.delete()
    return redirect('add_center')


def add_logo(request):
    if request.method == 'POST':

        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = ClientLogo.objects.create(

            image=image
        )
        # Redirect or do other actions after saving
        return redirect('add_logo')  # Replace 'success_page' with your actual success page URL

    logo = ClientLogo.objects.all()
    return render(request, 'add_home_logo.html', {'logo': logo})




def delete_logo(request, opening_id):
    content = get_object_or_404(ClientLogo, id=opening_id)
    content.delete()
    return redirect('add_logo')




def edit_logo(request, service_id):
    
    service = get_object_or_404(ClientLogo, pk=service_id)

    if request.method == 'POST':
        

        image = request.FILES.get('image')  

       

        if image:
            service.image = image

        
        service.save()

        return redirect('add_logo')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_home_logo.html', {'service': service})
    

def add_mission(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        link_url = request.POST['link_url']
        
    
        # Save the data to the database
        section =  MissionVision.objects.create(
            title=title,
            description=description,
            link_url=link_url
        )
        # Redirect or do other actions after saving
        return redirect('add_mission')  # Replace 'success_page' with your actual success page URL

    add_mission =  MissionVision.objects.all()
    return render(request, 'add_home_mission.html', {'add_mission': add_mission})


def edit_mission(request, content_id):
    content = get_object_or_404( MissionVision, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        title = request.POST.get('title',content.title)
        description = request.POST.get('description',content.description)
        link_url = request.POST.get('link_url',content.link_url)
        
       

        # Update the SwiperContent instance with the new data
        content.title = title
        content.description = description
        content.link_url = link_url
       
        
        content.save()

        return redirect('add_mission')  # Redirect to the Swiper view after editing

    return render(request, 'edit_home_mission.html', {'content': content})



def delete_mission(request, opening_id):
    content = get_object_or_404(MissionVision, id=opening_id)
    content.delete()
    return redirect('add_mission')


def add_design(request):
    if request.method == 'POST':

        
        # Check if image is provided
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
        # Save the data to the database
        service_content = WebDesign.objects.create(

            image=image
        )
        # Redirect or do other actions after saving
        return redirect('add_design')  # Replace 'success_page' with your actual success page URL

    design = WebDesign.objects.all()
    return render(request, 'add_home_design.html', {'design': design})




def delete_design(request, opening_id):
    content = get_object_or_404(WebDesign, id=opening_id)
    content.delete()
    return redirect('add_design')




def edit_design(request, service_id):
    
    service = get_object_or_404(WebDesign, pk=service_id)

    if request.method == 'POST':
        

        image = request.FILES.get('image')  

       

        if image:
            service.image = image

        
        service.save()

        return redirect('add_design')  # Replace 'mamamia_services' with your actual view name
    else:
        return render(request, 'edit_home_design.html', {'service': service})


def add_faq(request):
    if request.method == 'POST':
        # Get form data
      
        question = request.POST.get('question')
        answer = request.POST.get('answer')
       
    
        # Save the data to the database
        content = FAQ.objects.create(
            question=question,
            answer=answer,
           
        )
        # Redirect or do other actions after saving
        return redirect('add_faq')  # Replace 'success_page' with your actual success page URL

    add_faq = FAQ.objects.all()
    return render(request, 'add_home_faq.html', {'add_faq': add_faq})


def edit_faq(request, content_id):
    content = get_object_or_404(FAQ, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        question = request.POST.get('question',content.question)
        answer = request.POST.get('answer',content.answer)
       

        # Update the SwiperContent instance with the new data
        content.question =  question
        content.answer = answer
       
        
        content.save()

        return redirect('add_faq')  # Redirect to the Swiper view after editing

    return render(request, 'edit_home_faq.html', {'content': content})



def delete_faq(request, opening_id):
    content = get_object_or_404(FAQ, id=opening_id)
    content.delete()
    return redirect('add_faq')






def contact_us(request):
    logos = ClientLogo.objects.all()
    bloge = BlogPost.objects.all().order_by('-created_at')[:2]
    return render (request,'contact_us.html',{'logos':logos,'bloge':bloge})


def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if first_name and email and message:
            # Save the contact form data to the database
            ContactMessage.objects.create(first_name=first_name, email=email, message=message)
            
            # Compose the email content
            subject = f"New Contact Form Submission from {first_name}"
            admin_message = f"New contact form submission:\n\nName: {first_name}\nEmail: {email}\nMessage:\n{message}"
            recipient_email = 'akhilakd5299@gmail.com'  # Update to the desired recipient email

            try:
                # Send email to the specified recipient
                send_mail(subject, admin_message, settings.EMAIL_HOST_USER, [recipient_email], fail_silently=False)
                messages.success(request, 'Thank you for your message. We will get back to you shortly.')
            except Exception as e:
                messages.error(request, f"Error sending email: {str(e)}")
            
            return redirect('thank_you')
        else:
            messages.error(request, 'Please fill in all fields.')

    return redirect('/#contact-form')


def thank_you(request):
    return render(request, 'thank_you.html')




def contact_messages(request):
    messages = ContactMessage.objects.all()
    return render(request, 'contact_messages.html', {'messages': messages})


def delete_contact_message(request,delet_type):
    product_type = get_object_or_404(ContactMessage, id=delet_type)
    
    product_type.delete()  # Delete the product type
    
    return redirect('contact_messages')  # Redirect to the list page

def about(request):
    section = Aboutus_intro.objects.first()  # Fetch the first instance
    testimonials = About_Testimonial.objects.all() 
    why = WhyChooseUs.objects.first()  # Fetch the first instance
    logos = ClientLogo.objects.all()
    bloge = BlogPost.objects.all().order_by('-created_at')[:2]
    return render (request,'about_us.html', {'section': section , 'testimonials': testimonials,'logos':logos,'bloge':bloge})


def add_about(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        highlight_text = request.POST.get('highlight_text')
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None  # Set image to None if not provided
        
    
        # Save the data to the database
        content = Aboutus_intro.objects.create(
            heading=heading,
            paragraph=paragraph,
            highlight_text=highlight_text,
            image=image,
           
        )
        # Redirect or do other actions after saving
        return redirect('add_about')  # Replace 'success_page' with your actual success page URL

    add_about = Aboutus_intro.objects.all()
    return render(request, 'add_aboutus.html', {'add_about': add_about})


def edit_about(request, content_id):
    content = get_object_or_404(Aboutus_intro, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        heading = request.POST.get('heading',content.heading)
        highlight_text = request.POST.get('highlight_text',content.highlight_text)
        paragraph = request.POST.get('paragraph',content.paragraph)
        image = request.FILES.get('image', content.image)  
       

        # Update the SwiperContent instance with the new data
        content.heading = heading
        content.highlight_text = highlight_text
        content.paragraph = paragraph
        content.image = image
       
        
        content.save()

        return redirect('add_about')  # Redirect to the Swiper view after editing

    return render(request, 'edit_aboutus.html', {'content': content})



def delete_about(request, opening_id):
    content = get_object_or_404(Aboutus_intro, id=opening_id)
    content.delete()
    return redirect('add_about')

def add_slider(request):
    if request.method == 'POST':
        # Get form data
      
        question = request.POST.get('question')
        content = request.POST.get('content')
       
    
        # Save the data to the database
        service = About_Testimonial.objects.create(
            question=question,
            content=content,
           
        )
        # Redirect or do other actions after saving
        return redirect('add_slider')  # Replace 'success_page' with your actual success page URL

    add_slider = About_Testimonial.objects.all()
    return render(request, 'add_about_slider.html', {'add_slider': add_slider})


def edit_slider(request, service_id):
    service = get_object_or_404(About_Testimonial, id=service_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        question = request.POST.get('question',service.question)
        content = request.POST.get('content',service.content)
       

        # Update the SwiperContent instance with the new data
        service.question =  question
        service.content = content
       
        
        service.save()

        return redirect('add_slider')  # Redirect to the Swiper view after editing

    return render(request, 'edit_about_slider.html', {'service': service})



def delete_slider(request, opening_id):
    content = get_object_or_404(About_Testimonial, id=opening_id)
    content.delete()
    return redirect('add_slider')



def services(request):
    why = WhyChooseUs.objects.first() 
    logos = ClientLogo.objects.all()
    bloge = BlogPost.objects.all().order_by('-created_at')[:2]  
    return render (request,'services.html', {'why': why , 'logos':logos,'bloge':bloge})

def add_why(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        left_heading = request.POST.get('left_heading')
        left_description = request.POST.get('left_description')
        right_heading = request.POST.get('right_heading')
        right_description = request.POST.get('right_description')
        
    
        # Save the data to the database
        content = WhyChooseUs.objects.create(
            title=title,
            sub_title=sub_title,
            left_heading=left_heading,
            left_description=left_description,
            right_heading=right_heading,
            right_description=right_description,
        )
        # Redirect or do other actions after saving
        return redirect('add_why')  # Replace 'success_page' with your actual success page URL

    add_why = WhyChooseUs.objects.all()
    return render(request, 'add_service_why.html', {'add_why': add_why})


def edit_why(request, content_id):
    content = get_object_or_404(WhyChooseUs, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        title = request.POST.get('title',content.title)
        sub_title = request.POST.get('sub_title',content.sub_title)
        left_heading = request.POST.get('left_heading',content.left_heading)
        left_description = request.POST.get('left_description',content.left_description)
        right_heading = request.POST.get('right_heading',content.right_heading)
        right_description = request.POST.get('right_description',content.right_description)
        


        # Update the SwiperContent instance with the new data
        content.title = title
        content.sub_title = sub_title
        content.left_heading = left_heading
        content.left_description = left_description
        content.right_heading = right_heading
        content.right_description = right_description
       
        
        content.save()

        return redirect('add_why')  # Redirect to the Swiper view after editing

    return render(request, 'edit_service_why.html', {'content': content})



def delete_why(request, opening_id):
    content = get_object_or_404(WhyChooseUs, id=opening_id)
    content.delete()
    return redirect('add_why')


def portfolio(request):
    portfolio_items = Portfolio.objects.all()
    logos = ClientLogo.objects.all()
    bloge = BlogPost.objects.all().order_by('-created_at')[:2]
    return render (request,'portfolio.html', {'portfolio_items': portfolio_items,'logos':logos,'bloge':bloge})


def add_portfolio(request):
    if request.method == 'POST':
        # Get form data
        heading = request.POST.get('heading')
        paragraph = request.POST.get('paragraph')
        link = request.POST.get('link')  # New link field
        image = request.FILES.get('image') if 'image' in request.FILES else None

        # Save the data to the database
        Portfolio.objects.create(
            heading=heading,
            paragraph=paragraph,
            link=link,
            image=image,
        )

        return redirect('add_portfolio')  # Redirect after saving

    add_portfolio = Portfolio.objects.all()
    return render(request, 'add_portfolio.html', {'add_portfolio': add_portfolio})



def edit_portfolio(request, content_id):
    content = get_object_or_404(Portfolio, id=content_id)

    if request.method == 'POST':
        # Update the fields with new data
        content.heading = request.POST.get('heading', content.heading)
        content.paragraph = request.POST.get('paragraph', content.paragraph)
        content.link = request.POST.get('link', content.link)  # Update the link field
        content.image = request.FILES.get('image', content.image)
        content.save()

        return redirect('add_portfolio')  # Redirect to the portfolio view after editing

    return render(request, 'edit_portfolio.html', {'content': content})




def delete_portfolio(request, opening_id):
    content = get_object_or_404(Portfolio, id=opening_id)
    content.delete()
    return redirect('add_portfolio')


def web_development(request):
    logos = ClientLogo.objects.all()
    return render (request,'web_design.html',{'logos':logos})

def digital_marketing(request):
    logos = ClientLogo.objects.all()
    bloge = BlogPost.objects.all().order_by('-created_at')[:2]
    return render (request,'digital_marketing.html',{'logos':logos,'bloge':bloge})

def branding(request):
    logos = ClientLogo.objects.all()
    bloge = BlogPost.objects.all().order_by('-created_at')[:2]
    return render (request,'branding.html',{'logos':logos,'bloge':bloge})



def blog_details(request, blog_id, slug):
    blog = get_object_or_404(BlogPost, id=blog_id)

    # Dynamically generate the slug from the blog title
    generated_slug = slugify(blog.title)

    # Check if the slug in the URL matches the generated slug
    if slug != generated_slug:
        # If the slug doesn't match, redirect to the correct URL with the generated slug
        return redirect('blog_details', blog_id=blog.id, slug=generated_slug)
    

    logos = ClientLogo.objects.all()
    bloge = BlogPost.objects.all().order_by('-created_at')[:2]

    return render(request, 'blog_detail.html', {'blog': blog,'logos':logos,'bloge':bloge})



def blog_page(request):
    # Fetch all blog posts
    blogs = BlogPost.objects.all().order_by('-created_at')
    bloge = BlogPost.objects.all().order_by('-created_at')[:2]
    logos = ClientLogo.objects.all()
    return render(request, 'blog.html' , {'blogs': blogs,'logos':logos,'bloge':bloge})



def add_blog(request):
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        # Save the data to the database
        cards = BlogPost.objects.create(
            title=title,
            author=author,
            content=content,
            image=image,  # Save the meta description
            created_at=timezone.now()
        )
        cards.save()

        # Redirect after saving
        return redirect('add_blog')  # Replace with your actual redirect URL

    cards = BlogPost.objects.all()
    return render(request, 'add_blog.html', {'cards': cards})


   
    
       
def delete_blog(request, opening_id):
    content = get_object_or_404(BlogPost, id=opening_id)
    content.delete()
    return redirect('add_blog')

def edit_blog(request, service_id):
    blog = get_object_or_404(BlogPost, id=service_id)

    if request.method == 'POST':
        # Get the updated values from the form
        title = request.POST.get('title', blog.title)
        author = request.POST.get('author', blog.author)
        content = request.POST.get('content', blog.content)
        image = request.FILES.get('image') if 'image' in request.FILES else blog.image
       
        # Update the blog instance with the new data
        blog.title = title
        blog.author = author
        blog.content = content
        blog.image = image
        blog.save()

        # Redirect after saving the changes
        return redirect('add_blog')

    return render(request, 'edit_blog.html', {'blog': blog})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:  # Check if the user is an admin
                login(request, user)
                return redirect('admin_page')  # Replace with the URL of your admin dashboard
            else:
                messages.error(request, 'You do not have permission to access the admin panel.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')



@login_required(login_url='admin_login')
def admin_page(request):
    return render(request,'admin.html')


def logout_view(request):
    logout(request)
    return redirect('home')



def terms_and_conditions(request):
    logos = ClientLogo.objects.all()
    bloge = BlogPost.objects.all().order_by('-created_at')[:2]
    return render(request,'terms_and_conditions.html',{'logos':logos,'bloge':bloge})
# Create your views here.
