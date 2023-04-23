from django.urls import include, path

from . import views

urlpatterns = [

    path('countryadd/', views.CountryRegisterView.as_view(), name="countryadd"),
    path('countrylist/', views.CountryRegisterView.as_view(), name="countrylist"),
    path('countrylist/<int:id>', views.CountryRegisterView.as_view(), name="countrylist"),

    path('stateadd/', views.StateRegisterView.as_view(), name="stateadd"),
    path('districtadd/', views.DistrictRegisterView.as_view(), name="districtadd"),
    path('cityadd/', views.CityRegisterView.as_view(), name="cityadd"),

    path('branchadd/', views.BranchRegisterView.as_view(), name="branchadd"),
    path('religionadd/', views.ReligionRegisterView.as_view(), name="religionadd"),
    path('casteadd/', views.CasteRegisterView.as_view(), name="casteadd"),
    path('subcasteadd/', views.SubCasteRegisterView.as_view(), name="subcasteadd"),
    path('occupationadd/', views.OccupationRegisterView.as_view(), name="occupationadd"),
    path('educationadd/', views.EducationRegisterView.as_view(), name="educationadd"),

    path('languageadd/', views.LanguageRegisterView.as_view(), name="languageadd"),
    path('sourceadd/', views.SourceRegisterView.as_view(), name="sourceadd"),

]

