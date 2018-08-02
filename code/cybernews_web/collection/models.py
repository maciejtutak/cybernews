from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode


class Tag(models.Model):
    """Represents possible article tags."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    # override default save to create slugs
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Article(models.Model):
    """Represents a single article."""
    title = models.CharField(max_length=500)
    text = models.TextField()

    source = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    image_url = models.URLField(blank=True)

    length = models.IntegerField()
    author = models.CharField(max_length=100, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} | title: {}".format(self.id, self.title)

    # source domain and id added to the slug
    def _get_unique_slug(self):
        source_domain = self.source[:self.source.index('.')]
        slug = slugify(unidecode(source_domain + ' ' + self.title + ' ' + self.pub_date))
        return slug

    # override default save to create slugs
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']


class Entry(models.Model):
    """Connects a single article to tags."""
    tags = models.ManyToManyField(
        Tag,
        related_name='tags',
        related_query_name='entries',
        blank=True,
    )
    edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tagged = models.BooleanField(default=False)
    user_reviewed = models.BooleanField(default=False)
    slug = models.SlugField(max_length=520, unique=True)

    article = models.OneToOneField(
        Article,
        on_delete=models.CASCADE,
        related_name='article',
    )

    def __str__(self):
        return "Entry/Article: {}/{} | reviewed: {}".format(self.id, self.article.title, self.user_reviewed)

    # source domain and id added to the slug
    def _get_unique_slug(self):
        source_domain = self.article.source[:self.article.source.index('.')]
        slug = slugify(unidecode(source_domain + ' ' + self.article.title + ' ' + self.created))
        return slug

    # override default save to create slugs
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
        ordering = ['-article__pub_date', '-created', 'user_reviewed']

