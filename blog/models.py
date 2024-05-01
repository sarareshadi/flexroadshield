from django.db import models


class BlogPost(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', default='default.jpg')
    status = models.CharField(max_length=2, choices=Status.choices,default=Status.DRAFT)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30,)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey('blog.BlogPost', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
class Image(models.Model):
    name = models.CharField(max_length=300)
    shoot_date = models.DateField(null=True, blank=True,)
    upload = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to='images/')    
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.SET_NULL)
    like_counts = models.IntegerField(default=0)
    description = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.upload.date()}"