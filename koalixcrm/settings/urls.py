"""test_koalixcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls.static import *
from django.contrib.staticfiles.urls import static
from django.contrib import admin
from django.shortcuts import redirect
from django.conf.urls import include, url
from filebrowser.sites import site
from rest_framework import routers

from koalixcrm.accounting.rest.restinterface import AccountAsJSON, AccountingPeriodAsJSON, BookingAsJSON, \
    ProductCategoryAsJSON
from koalixcrm.crm.rest.restinterface import ContractAsJSON, CurrencyAsJSON, ProductAsJSON, ProjectAsJSON, TaskAsJSON, \
    TaskStatusAsJSON, TaxAsJSON, UnitAsJSON, CustomerGroupAsJSON, CustomerBillingCycleAsJSON, \
    CustomerAsJSON, ContactPostalAddressAsJSON, ContactEmailAddressAsJSON, ContactPhoneAddressAsJSON, \
    ProjectStatusAsJSON

router = routers.DefaultRouter()
router.register(r'accounts', AccountAsJSON)
router.register(r'accountingPeriods', AccountingPeriodAsJSON)
router.register(r'bookings', BookingAsJSON)
router.register(r'contracts', ContractAsJSON)
router.register(r'currencies', CurrencyAsJSON)
router.register(r'customers', CustomerAsJSON)
router.register(r'customerBillingCycles', CustomerBillingCycleAsJSON)
router.register(r'contactPostalAddresses', ContactPostalAddressAsJSON)
router.register(r'contactPhoneNumbers', ContactPhoneAddressAsJSON)
router.register(r'contactEmailAddresses', ContactEmailAddressAsJSON)
router.register(r'customerGroups', CustomerGroupAsJSON)
router.register(r'products', ProductAsJSON)
router.register(r'productCategories', ProductCategoryAsJSON)
router.register(r'projects', ProjectAsJSON)
router.register(r'projectStatus', ProjectStatusAsJSON)
router.register(r'tasks', TaskAsJSON)
router.register(r'taskstatus', TaskStatusAsJSON)
router.register(r'taxes', TaxAsJSON)
router.register(r'units', UnitAsJSON)

admin.autodiscover()

urlpatterns = [
    path('', lambda _: redirect('admin:index'), name='index'),
    path('', include(router.urls)),
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('koalixcrm/crm/reporting/', include('koalixcrm.crm.reporting.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

