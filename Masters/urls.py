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

    path('state/', views.StateRegisterView.as_view(), name="stateAddUpdateList"),
    path('state/<int:id>', views.StateRegisterView.as_view(), name="stateListDelete"),
    path('statecountries/<int:id>', views.StateCountriesView.as_view(), name="stateListCountries"),

    path('district/', views.DistrictRegisterView.as_view(), name="districtAddUpdateList"),
    path('district/<int:id>', views.DistrictRegisterView.as_view(), name="districtListDelete"),

    path('city/', views.CityRegisterView.as_view(), name="cityAddUpdateList"),
    path('city/<int:id>', views.CityRegisterView.as_view(), name="cityListDelete"),

    # path('cityadd/', views.CityRegisterView.as_view(), name="cityadd"),
    # path('citylist/', views.CityRegisterView.as_view(), name="citylist"),
    # path('citylist/<int:id>', views.CityRegisterView.as_view(), name="citylist"),

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

]

