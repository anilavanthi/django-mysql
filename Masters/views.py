from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status, views, permissions

from Masters.models import Country
from Masters.serializers import StateSerializer, DistrictSerializer, CitySerializer, CountrySerializer, \
    BranchSerializer, ReligionSerializer, \
    CasteSerializer, SubCasteSerializer, OccupationSerializer, EducationSerializer, LanguageSerializer, SourceSerializer


# Create your views here.

class CountryRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = CountrySerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        country=serializer.save()
        return Response({
            "country":CountrySerializer(country, context=self.get_serializer_context()).data,
            "message":"country created successfully"
        })
    def get(self,request,id=None):
        if id:
            country = Country.objects.get(id=id)
            serializer = CountrySerializer(country)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)



class StateRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = StateSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        state=serializer.save()
        return Response({
            "state":StateSerializer(state, context=self.get_serializer_context()).data,
            "message":"state created successfully"
        })

class DistrictRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = DistrictSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        district=serializer.save()
        return Response({
            "district":DistrictSerializer(district, context=self.get_serializer_context()).data,
            "message":"District created successfully"
        })


class CityRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = CitySerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city=serializer.save()
        return Response({
            "city":CitySerializer(city, context=self.get_serializer_context()).data,
            "message":"City created successfully"
        })

class BranchRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = BranchSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        branch=serializer.save()
        return Response({
            "branch":BranchSerializer(branch, context=self.get_serializer_context()).data,
            "message":"Branch created successfully"
        })

class ReligionRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = ReligionSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        religion=serializer.save()
        return Response({
            "religion":ReligionSerializer(religion, context=self.get_serializer_context()).data,
            "message":"Religion created successfully"
        })

class CasteRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = CasteSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        caste=serializer.save()
        return Response({
            "caste":CasteSerializer(caste, context=self.get_serializer_context()).data,
            "message":"Caste created successfully"
        })


class SubCasteRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = SubCasteSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subcaste=serializer.save()
        return Response({
            "subcaste":SubCasteSerializer(subcaste, context=self.get_serializer_context()).data,
            "message":"Sub-Caste created successfully"
        })

class OccupationRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = OccupationSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        occupation=serializer.save()
        return Response({
            "occupation":OccupationSerializer(occupation, context=self.get_serializer_context()).data,
            "message":"Occupation created successfully"
        })


class EducationRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = EducationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        education = serializer.save()
        return Response({
            "education": EducationSerializer(education, context=self.get_serializer_context()).data,
            "message": "Education created successfully"
        })


class LanguageRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = LanguageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        language = serializer.save()
        return Response({
            "language": LanguageSerializer(language, context=self.get_serializer_context()).data,
            "message": "Language created successfully"
        })


class SourceRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = SourceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        source = serializer.save()
        return Response({
            "source": SourceSerializer(source, context=self.get_serializer_context()).data,
            "message": "Source created successfully"
        })