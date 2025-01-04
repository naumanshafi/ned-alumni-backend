import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('home_address', models.TextField(blank=True, null=True)),
                ('home_city', models.CharField(blank=True, max_length=100, null=True)),
                ('home_state', models.CharField(blank=True, max_length=100, null=True)),
                ('home_country', models.CharField(blank=True, max_length=100, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('work_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('other_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('batch', models.CharField(blank=True, max_length=20, null=True)),
                ('graduation_year', models.PositiveIntegerField(blank=True, null=True)),
                ('discipline', models.CharField(blank=True, max_length=255, null=True)),
                ('degree', models.CharField(blank=True, choices=[('Undergraduate', 'Undergraduate'), ('Masters', 'Masters'), ('PhD', 'PhD')], max_length=20, null=True)),
                ('nedian', models.BooleanField(default=False)),
                ('graduation_address', models.TextField(blank=True, null=True)),
                ('profile_confirmed', models.BooleanField(default=False)),
                ('last_login_date', models.DateField(blank=True, null=True)),
                ('profile_created', models.DateField(auto_now_add=True)),
                ('profile_edited', models.DateField(auto_now=True)),
                ('profile_active', models.BooleanField(default=True)),
                ('deceased', models.BooleanField(default=False)),
                ('profile_duplicate', models.BooleanField(default=False)),
                ('profile_link_ids', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('membership_id', models.AutoField(primary_key=True, serialize=False)),
                ('membership_type', models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid')], max_length=10)),
                ('duration', models.PositiveIntegerField(choices=[(0, 'Free'), (1, '1 Year'), (3, '3 Years'), (99, 'Lifetime')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_mode', models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Check', 'Check'), ('Paypal', 'Paypal'), ('Stripe', 'Stripe')], max_length=20, null=True)),
                ('payment_reference', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_confirmed', models.BooleanField(default=False)),
                ('confirmation_mode', models.CharField(blank=True, choices=[('Email', 'Email'), ('Verbal', 'Verbal')], max_length=20, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('member_since', models.DateField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
