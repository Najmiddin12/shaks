from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.mail import send_mail

def home(request):
    contact = Contact.objects.all()
    carousels = Carousel.objects.all()
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    testimonials = Testimonials.objects.all()
    teams = Team.objects.all()
    blogs = Blog.objects.all()
    links = Links.objects.all()
    creators = Creator.objects.all()
    return render(request, 'project/index.html', {"contact": contact, "carousels": carousels, "services": services, "portfolios": portfolios, "testimonials": testimonials, "teams": teams, "blogs": blogs, "links": links, "creators": creators})

def about(request):
    links = Links.objects.all()
    contact = Contact.objects.all()
    testimonials = Testimonials.objects.all()
    creators = Creator.objects.all()
    return render(request, 'project/about.html', {"links": links, "contact": contact, "testimonials": testimonials, "creators": creators})

def contact(request):
    contact = Contact.objects.all()
    links = Links.objects.all()
    creators = Creator.objects.all()
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text = request.POST.get('text')

        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'text': text,
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['text'], data['email'])
        send_mail(data['phone'], message, data['email'], ['design@shaksmedia.com'], ['sales@shaksmedia.com'], ['tatiana@shaksmedia.com'])

    return render(request, 'project/contact.html', {"contact": contact, "links": links, "creators": creators})


def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    photos = ServicePhoto.objects.filter(service=service)
    return render(request, 'project/service.html', {'service': service, 'photos': photos})

def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'project/portfolio.html', {'portfolios': portfolios})

def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    photos = PortfolioPhoto.objects.filter(portfolio=portfolio)
    videos = PortfolioVideo.objects.filter(portfolio=portfolio)
    return render(request, 'project/portfolio-detail.html', {'portfolio': portfolio, 'photos': photos, 'videos': videos})

def blog_detail(request, pk):
    contact = Contact.objects.all()
    links = Links.objects.all()
    blog = Blog.objects.get(pk=pk)
    creators = Creator.objects.all()
    return render(request, 'project/blog ru.html', {"contact": contact, "links": links, "blog": blog, "creators": creators})

