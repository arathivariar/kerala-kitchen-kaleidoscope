from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Choice Fields
DISH_TYPES = (
    ("Breakfast", "Breakfast"),
    ("Curries", "Curries"),
    ("Snacks", "Snacks"),
    ("Drinks", "Drinks"),
)

PREP_TIME = (
    ("5 minutes", "5 min"),
    ("10 minutes", "10 min"),
    ("15 minutes", "15 min"),
    ("20 minutes", "20 min"),
    ("30 minutes", "30 min"),
    ("45 minutes", "45 min"),
    ("1 hour", "1 hour"),
    ("1+ hour", "More than 1h"),
)


class Recipe(models.Model):
    """
    A model to create and manage recipes
    Only the chef who created the recipe can edit or delete their own recipes
    """

    recipe_id = models.IntegerField()
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    chef = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="kitchen_recipes"
    )
    featured_image = CloudinaryField("image", default="placeholder")
    ingredients = models.TextField(max_length=10000, null=False, blank=False)
    method = models.TextField(max_length=10000, null=False, blank=False)
    dish_type = models.CharField(max_length=50, choices=DISH_TYPES, default="breakfast")
    prep_time = models.CharField(max_length=50, choices=PREP_TIME, default="15 minutes")
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-posted_on"]

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
