from django.db import models

class Links(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=2555)

class Contact(models.Model):
    email_1 = models.CharField(max_length=255)
    email_2 = models.CharField(max_length=255)
    phone_1 = models.CharField(max_length=255)
    phone_2 = models.CharField(max_length=255)

class Carousel(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/')
    text = models.CharField(max_length=2555)

class Service(models.Model):
    title = models.CharField(('name'), max_length=255)
    icon_name = models.CharField(max_length=255)
    description = models.TextField(('description'))

    def __str__(self):
        return self.title

class ServicePhoto(models.Model):
    service = models.ForeignKey(Service, related_name='ServicePhotos', on_delete=models.CASCADE)
    photo = models.ImageField(('photo'), upload_to='service/photos/')

    def __str__(self):
        return f"Photo for {self.service.title}"


class Portfolio(models.Model):
    name = models.CharField(('name'), max_length=255)
    photo = models.ImageField(('photo'), upload_to='portfolio/')
    description = models.TextField(('description'), blank=True, null=False)
    process_work = models.TextField(('process work'), blank=True, null=False)
    def __str__(self):
        return self.name

class PortfolioPhoto(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='PortfolioPhotos', on_delete=models.CASCADE)
    photo = models.ImageField(('photo'), upload_to='portfolio/photos/')

    def __str__(self):
        return f"Photo for {self.portfolio.name}"

class PortfolioVideo(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='PortfolioVideos', on_delete=models.CASCADE)
    video = models.CharField(('video'), max_length=2555)

    def __str__(self):
        return f"Video for {self.portfolio.name}"


class Testimonials(models.Model):
    title_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    text = models.CharField(max_length=2555)

class Team(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    facebook = models.CharField(max_length=255, blank=True, null=False)
    instagram = models.CharField(max_length=255, blank=True, null=False)
    telegram = models.CharField(max_length=255, blank=True, null=False)
    whatsapp = models.CharField(max_length=255, blank=True, null=False)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=2555)
    img = models.ImageField(upload_to='images/')

class Creator(models.Model):
    mirzoahmad_url = models.CharField(max_length=255)
    najmiddin_url = models.CharField(max_length=255)