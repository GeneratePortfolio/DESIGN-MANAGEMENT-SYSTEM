from django.db import models

# Create your models here.
class Design(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name=  models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    design_file= models.ImageField(upload_to=None)
    about_design= models.TextField()
    used_tool= models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    

    class Meta:
        verbose_name = _("Design")
        verbose_name_plural = _("Designs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Design_detail", kwargs={"pk": self.pk})
    
    
    
class Comment(models.Model):
    comment =models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})

