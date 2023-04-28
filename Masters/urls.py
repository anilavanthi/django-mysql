from django.urls import include, path

from . import views

urlpatterns = [

    path('country/', views.CountryRegisterView.as_view(), name="countryAddUpdateList"),
    path('country/<int:id>', views.CountryRegisterView.as_view(), name="countryListDelete"),

    # path('countryadd/', views.CountryRegisterView.as_view(), name="countryadd"),
    # path('countrylist/', views.CountryRegisterView.as_view(), name="countrylist"),
    # path('countrylist/<int:id>', views.CountryRegisterView.as_view(), name="countrylist"),
    # path('country/update', views.CountryRegisterView.as_view(), name="countryupdatedelete"),
    # path('countrydelete/<int:id>', views.CountryRegisterView.as_view(), name="countrylist"),

    path('stateadd/', views.StateRegisterView.as_view(), name="stateadd"),
    path('statelist/', views.StateRegisterView.as_view(), name="statelist"),
    path('statelist/<int:id>', views.StateRegisterView.as_view(), name="statelist"),


    path('districtadd/', views.DistrictRegisterView.as_view(), name="districtadd"),
    path('districtlist/', views.DistrictRegisterView.as_view(), name="districtlist"),
    path('districtlist/<int:id>', views.DistrictRegisterView.as_view(), name="districtlist"),

    path('cityadd/', views.CityRegisterView.as_view(), name="cityadd"),
    path('citylist/', views.CityRegisterView.as_view(), name="citylist"),
    path('citylist/<int:id>', views.CityRegisterView.as_view(), name="citylist"),

    path('branchadd/', views.BranchRegisterView.as_view(), name="branchadd"),
    path('branchlist/', views.BranchRegisterView.as_view(), name="branchlist"),
    path('branchlist/<int:id>', views.BranchRegisterView.as_view(), name="branchlist"),

    path('religionadd/', views.ReligionRegisterView.as_view(), name="religionadd"),
    path('religionlist/', views.ReligionRegisterView.as_view(), name="religionlist"),
    path('religionlist/<int:id>', views.ReligionRegisterView.as_view(), name="religionlist"),

    path('casteadd/', views.CasteRegisterView.as_view(), name="casteadd"),
    path('castelist/', views.CasteRegisterView.as_view(), name="castelist"),
    path('castelist/<int:id>', views.CasteRegisterView.as_view(), name="castelist"),

    path('subcasteadd/', views.SubCasteRegisterView.as_view(), name="subcasteadd"),
    path('subcastelist/', views.SubCasteRegisterView.as_view(), name="subcastelist"),
    path('subcastelist/<int:id>', views.SubCasteRegisterView.as_view(), name="subcastelist"),

    path('occupationadd/', views.OccupationRegisterView.as_view(), name="occupationadd"),
    path('occupationlist/', views.OccupationRegisterView.as_view(), name="occupationlist"),
    path('occupationlist/<int:id>', views.OccupationRegisterView.as_view(), name="occupationlist"),

    path('educationadd/', views.EducationRegisterView.as_view(), name="educationadd"),
    path('educationlist/', views.EducationRegisterView.as_view(), name="educationlist"),
    path('educationlist/<int:id>', views.EducationRegisterView.as_view(), name="educationlist"),

    path('languageadd/', views.LanguageRegisterView.as_view(), name="languageadd"),
    path('languagelist/', views.LanguageRegisterView.as_view(), name="languagelist"),
    path('languagelist/<int:id>', views.LanguageRegisterView.as_view(), name="languagelist"),

    path('sourceadd/', views.SourceRegisterView.as_view(), name="sourceadd"),
    path('sourcelist/', views.SourceRegisterView.as_view(), name="sourcelist"),
    path('sourcelist/<int:id>', views.SourceRegisterView.as_view(), name="sourcelist"),

]

