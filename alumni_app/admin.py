from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member, Membership

@admin.register(Member)
class MemberAdmin(UserAdmin):
    # Adding all fields to the admin panel
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {
            'fields': (
                'first_name', 'last_name', 'email', 'profile_picture',
                'home_address', 'home_city', 'home_state', 'home_country',
                'home_phone', 'mobile_phone', 'work_phone', 'other_phone',
                'batch', 'graduation_year', 'discipline', 'degree',
                'graduation_address', 'profile_link_ids',
            )
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
        ('Profile Status', {
            'fields': (
                'profile_active', 'deceased', 'profile_confirmed',
                'profile_duplicate', 'nedian'
            )
        }),
    )

    # Adding fields for user creation (overrides the default 'Add user' form)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2', 'first_name', 'last_name',
                'email', 'profile_picture', 'home_address', 'home_city', 'home_state',
                'home_country', 'home_phone', 'mobile_phone', 'work_phone',
                'other_phone', 'batch', 'graduation_year', 'discipline',
                'degree', 'graduation_address', 'profile_active', 'deceased',
                'profile_confirmed', 'nedian',
            ),
        }),
    )

    # List all fields in the list view
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'profile_active',
        'nedian', 'deceased', 'profile_confirmed', 'is_staff', 'is_superuser'
    )

    # Allow filtering by these fields
    list_filter = ('is_staff', 'is_superuser', 'profile_active', 'deceased', 'nedian', 'profile_confirmed')

    # Allow searching by these fields
    search_fields = ('username', 'email', 'first_name', 'last_name', 'home_city', 'mobile_phone', 'batch')

    # Ordering the list view
    ordering = ('username', 'email')

    # Exclude non-editable fields
    readonly_fields = ('profile_created', 'profile_edited', 'last_login_date')



@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('membership_id', 'member', 'membership_type', 'duration', 'amount_paid', 'payment_confirmed')
    list_filter = ('membership_type', 'duration', 'payment_confirmed')
    search_fields = ('membership_id', 'member__username', 'member__email')
