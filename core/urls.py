from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # 1. Pages App (Home, About, Contact) - The empty string '' means Homepage
    path('', include('pages.urls')),

    # 2. Auth App (Login, Register, Logout)
    path('auth/', include('accounts.urls')),

    # 3. Clubs App (All club related pages)
    path('clubs/', include('clubs.urls')),

    # 4. Dashboard App (Student private area)
    path('dashboard/', include('dashboard.urls')),

    # 5. Blog App (Articles, Event Recaps, Achievements)
    path('blog/', include('blog.urls')),
]

# --- Media File Configuration (For Local Development) ---
# This allows you to see uploaded images while working on your laptop.
# In production (Render), Supabase Storage handles this.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)