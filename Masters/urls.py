from django.urls import include, path

from . import views

urlpatterns = [

    # path('countryadd/', views.CountryRegisterView.as_view(), name="countryadd"),
    # path('countrylist/', views.CountryRegisterView.as_view(), name="countrylist"),
    # path('countrylist/<int:id>', views.CountryRegisterView.as_view(), name="countrylist"),
    # path('country/update', views.CountryRegisterView.as_view(), name="countryupdatedelete"),
    # path('countrydelete/<int:id>', views.CountryRegisterView.as_view(), name="countrylist"),

    path('country/', views.CountryRegisterView.as_view(), name="countryAddUpdateList"),
    path('country/<int:id>', views.CountryRegisterView.as_view(), name="countryListDelete"),

    path('stateadd/', views.StateRegisterView.as_view(), name="stateadd"),
    path('statelist/', views.StateRegisterView.as_view(), name="statelist"),
    path('statelist/<int:id>', views.StateRegisterView.as_view(), name="statelist"),


    path('districtadd/', views.DistrictRegisterView.as_view(), name="districtadd"),
    path('districtlist/', views.DistrictRegisterView.as_view(), name="districtlist"),
    path('districtlist/<int:id>', views.DistrictRegisterView.as_view(), name="districtlist"),

    path('cityadd/', views.CityRegisterView.as_view(), name="cityadd"),
    path('citylist/', views.CityRegisterView.as_view(), name="citylist"),
    path('citylist/<int:id>', views.CityRegisterView.as_view(), name="citylist"),

    path('branch/', views.BranchRegisterView.as_view(), name="branchAddUpdateList"),
    path('branch/<int:id>', views.BranchRegisterView.as_view(), name="branchListDelete"),

    path('religion/', views.ReligionRegisterView.as_view(), name="religionAddUpdateList"),
    path('religion/<int:id>', views.ReligionRegisterView.as_view(), name="religionListDelete"),

    path('caste/', views.CasteRegisterView.as_view(), name="casteAddUpdateList"),
    path('caste/<int:id>', views.CasteRegisterView.as_view(), name="casteListDelete"),

    path('subcasteadd/', views.SubCasteRegisterView.as_view(), name="subcasteadd"),
    path('subcastelist/', views.SubCasteRegisterView.as_view(), name="subcastelist"),
    path('subcastelist/<int:id>', views.SubCasteRegisterView.as_view(), name="subcastelist"),

    path('occupation/', views.OccupationRegisterView.as_view(), name="occupationAddUpdateList"),
    path('occupation/<int:id>', views.OccupationRegisterView.as_view(), name="occupationListDelete"),

    path('education/', views.EducationRegisterView.as_view(), name="educationAddUpdateList"),
    path('education/<int:id>', views.EducationRegisterView.as_view(), name="educationListDelete"),

    path('language/', views.LanguageRegisterView.as_view(), name="languageAddUpdateList"),
    path('language/<int:id>', views.LanguageRegisterView.as_view(), name="languageListDelete"),

    path('source/', views.SourceRegisterView.as_view(), name="sourcecAddUpdateList"),
    path('source/<int:id>', views.SourceRegisterView.as_view(), name="sourceListDelete"),
    #
    # path('sourceadd/', views.SourceRegisterView.as_view(), name="sourceadd"),
    # path('sourcelist/', views.SourceRegisterView.as_view(), name="sourcelist"),
    # path('sourcelist/<int:id>', views.SourceRegisterView.as_view(), name="sourcelist"),

]

