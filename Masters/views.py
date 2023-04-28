from datetime import datetime

from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import generics, status, views, permissions

from Masters.models import Country, State, District, City, Branch, Religion, Caste, SubCaste, Occupation, Education, \
    Language, Source
from Masters.serializers import StateSerializer, DistrictSerializer, CitySerializer, CountrySerializer, \
    BranchSerializer, ReligionSerializer, \
    CasteSerializer, SubCasteSerializer, OccupationSerializer, EducationSerializer, LanguageSerializer, SourceSerializer


# Create your views here.

class CountryRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = CountrySerializer
    countries = Country.objects.all()
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

    def put(self, request):
        try:
            current_user = request.user
            country_json = self.countries.filter(id=request.data['id'])
            country_json.update(code=request.data['code'],
                                    name=request.data['name'],
                                    status=request.data['status'],
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = CountrySerializer(country_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Country Details Updated Successfully',
                        "country_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self,request,id=None):
        try:
            current_user = request.user
            # country_json = self.countries.filter(id=request.data['id'])
            country_json = self.countries.filter(id=id)
            country = Country.objects.get(id=id)
            if(country.status==1):
                statusValue=0
            else:
                statusValue=1
            country_json.update(status=statusValue,
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = CountrySerializer(country_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Country Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    def delete(self, request,id=None):
        try:
            self.countries.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' country deleted successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)

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

    def get(self,request,id=None):
        if id:
            state = State.objects.get(id=id)
            serializer = StateSerializer(state)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

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

    def get(self,request,id=None):
        if id:
            district = District.objects.get(id=id)
            serializer = DistrictSerializer(district)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


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

    def get(self,request,id=None):
        if id:
            city = City.objects.get(id=id)
            serializer = CitySerializer(city)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


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
    def get(self,request,id=None):
        if id:
            branch = Branch.objects.get(id=id)
            serializer = BranchSerializer(branch)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


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
    def get(self,request,id=None):
        if id:
            religion = Religion.objects.get(id=id)
            serializer = ReligionSerializer(religion)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        religions = Religion.objects.all()
        serializer = ReligionSerializer(religions, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

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
    def get(self,request,id=None):
        if id:
            caste = Caste.objects.get(id=id)
            serializer = CasteSerializer(caste)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        castes = Caste.objects.all()
        serializer = CasteSerializer(castes, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

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
    def get(self, request, id=None):
        if id:
            subcaste = SubCaste.objects.get(id=id)
            serializer = SubCasteSerializer(subcaste)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        subcastes = SubCaste.objects.all()
        serializer = SubCasteSerializer(subcastes, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

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
    def get(self, request, id=None):
        if id:
            occupation = Occupation.objects.get(id=id)
            serializer = OccupationSerializer(occupation)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        occupations = Occupation.objects.all()
        serializer = OccupationSerializer(occupations, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


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
    def get(self, request, id=None):
        if id:
            education = Education.objects.get(id=id)
            serializer = EducationSerializer(education)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        educations = Education.objects.all()
        serializer = EducationSerializer(educations, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


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
    def get(self, request, id=None):
        if id:
            language = Language.objects.get(id=id)
            serializer = LanguageSerializer(language)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


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
    def get(self, request, id=None):
        if id:
            source = Source.objects.get(id=id)
            serializer = SourceSerializer(source)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        sources = Source.objects.all()
        serializer = SourceSerializer(sources, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)