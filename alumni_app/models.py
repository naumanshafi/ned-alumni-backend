from django.contrib.auth.models import AbstractUser
from django.db import models

class Member(AbstractUser):
    home_address = models.TextField(blank=True, null=True)
    home_city = models.CharField(max_length=100, blank=True, null=True)
    home_state = models.CharField(max_length=100, blank=True, null=True)
    home_country = models.CharField(max_length=100, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    work_phone = models.CharField(max_length=20, blank=True, null=True)
    other_phone = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    batch = models.CharField(max_length=20, blank=True, null=True)  # Example: 1981-82
    graduation_year = models.PositiveIntegerField(blank=True, null=True)
    discipline = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=20, choices=[
        ('Undergraduate', 'Undergraduate'),
        ('Masters', 'Masters'),
        ('PhD', 'PhD')
    ], blank=True, null=True)
    nedian = models.BooleanField(default=False)
    graduation_address = models.TextField(blank=True, null=True)
    profile_confirmed = models.BooleanField(default=False)
    last_login_date = models.DateField(blank=True, null=True)
    profile_created = models.DateField(auto_now_add=True)
    profile_edited = models.DateField(auto_now=True)
    profile_active = models.BooleanField(default=True)
    deceased = models.BooleanField(default=False)
    profile_duplicate = models.BooleanField(default=False)
    profile_link_ids = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.email})"


class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="memberships")
    membership_type = models.CharField(max_length=10, choices=[
        ('Free', 'Free'),
        ('Paid', 'Paid')
    ])
    duration = models.PositiveIntegerField(choices=[
        (0, 'Free'),
        (1, '1 Year'),
        (3, '3 Years'),
        (99, 'Lifetime')
    ])
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    # Payment Details
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_mode = models.CharField(max_length=20, choices=[
        ('Cash', 'Cash'),
        ('Check', 'Check'),
        ('Paypal', 'Paypal'),
        ('Stripe', 'Stripe')
    ], blank=True, null=True)
    payment_reference = models.CharField(max_length=255, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    payment_confirmed = models.BooleanField(default=False)
    confirmation_mode = models.CharField(max_length=20, choices=[
        ('Email', 'Email'),
        ('Verbal', 'Verbal')
    ], blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    member_since = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Membership {self.membership_id} for {self.member.username}"
