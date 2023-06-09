import json
import os
from datetime import datetime
from django.utils.text import slugify
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework import generics, status, views, permissions
from django.contrib.auth.hashers import make_password
from Masters.models import Country, State, District, City, Branch, Religion, Caste, SubCaste, Occupation, Education, \
    Language, Source, Staff, MemberShip, Agent
from Users.models import User
from Masters.serializers import StateSerializer, DistrictSerializer, CitySerializer, CountrySerializer, \
    BranchSerializer, ReligionSerializer, \
    CasteSerializer, SubCasteSerializer, OccupationSerializer, EducationSerializer, LanguageSerializer, SourceSerializer, StaffSerializer, \
    MemberShipSerializer,AgentSerializer

from Users.serializers import UserCommonSerializer

# Create your views here.

class CountryRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = CountrySerializer
    countries = Country.objects.all()
    def post(self, request, *args, **kwargs):
        try:
            serializer=self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            country=serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,
                        'message': 'Country Created Successfully',
                        'country':CountrySerializer(country, context=self.get_serializer_context()).data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'Adding Failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
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
    states = State.objects.all()
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

    def put(self, request):
        try:
            current_user = request.user
            state_json = self.states.filter(id=request.data['id'])
            state_json.update(name=request.data['name'],
                              code=request.data['code'],
                               country=request.data['country'],
                               status=request.data['status'],
                               modifiedby=current_user.id,
                               modifiedon=datetime.utcnow())
            serializer = StateSerializer(state_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,
                        'message': 'State Details Updated Successfully',
                        "state_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self, request, id=None):
        try:
            current_user = request.user
            state_json = self.states.filter(id=id)
            state = State.objects.get(id=id)
            if (state.status == 1):
                statusValue = 0
            else:
                statusValue = 1
            state_json.update(status=statusValue,
                               modifiedby=current_user.id,
                               modifiedon=datetime.utcnow())
            serializer = StateSerializer(state_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,
                        'message': 'State Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def delete(self, request, id=None):
        try:
            self.states.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' state deleted successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)


class StateCountriesView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = StateSerializer
    states = State.objects.all()

    def get(self,request,id=None):
        if id:
            states = State.objects.filter(country=id)
            serializer = StateSerializer(states,many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)



class DistrictRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = DistrictSerializer
    districts = District.objects.all()
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

    def put(self, request):
        try:
            current_user = request.user
            district_json = self.districts.filter(id=request.data['id'])
            district_json.update(name=request.data['name'],
                              code=request.data['code'],
                               country=request.data['country'],
                               state=request.data['state'],
                               status=request.data['status'],
                               modifiedby=current_user.id,
                               modifiedon=datetime.utcnow())
            serializer = DistrictSerializer(district_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,
                        'message': 'District Details Updated Successfully',
                        "district_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self, request, id=None):
        try:
            current_user = request.user
            district_json = self.districts.filter(id=id)
            district = District.objects.get(id=id)
            if (district.status == 1):
                statusValue = 0
            else:
                statusValue = 1
            district_json.update(status=statusValue,
                               modifiedby=current_user.id,
                               modifiedon=datetime.utcnow())
            serializer = DistrictSerializer(district_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,
                        'message': 'District Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def delete(self, request, id=None):
        try:
            self.districts.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' district deleted successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)


class DistrictStateCountriesView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = DistrictSerializer
    district = District.objects.all()

    def get(self,request,id=None):
        if id:
            districts = District.objects.filter(state=id)
            serializer = DistrictSerializer(districts,many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class CityDistrictStateCountriesView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = DistrictSerializer
    city = City.objects.all()

    def get(self,request,id=None):
        if id:
            cities = City.objects.filter(district=id)
            serializer = CitySerializer(cities,many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class CityRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = CitySerializer
    cities = City.objects.all()
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

    def put(self, request):
        try:
            current_user = request.user
            city_json = self.cities.filter(id=request.data['id'])
            city_json.update(name=request.data['name'],
                              code=request.data['code'],
                               country=request.data['country'],
                               state=request.data['state'],
                                district=request.data['district'],
                               status=request.data['status'],
                               modifiedby=current_user.id,
                               modifiedon=datetime.utcnow())
            serializer = CitySerializer(city_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,
                        'message': 'City Details Updated Successfully',
                        "city_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self, request, id=None):
        try:
            current_user = request.user
            city_json = self.cities.filter(id=id)
            city = City.objects.get(id=id)
            if (city.status == 1):
                statusValue = 0
            else:
                statusValue = 1
            city_json.update(status=statusValue,
                               modifiedby=current_user.id,
                               modifiedon=datetime.utcnow())
            serializer = CitySerializer(city_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,
                        'message': 'City Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def delete(self, request, id=None):
        try:
            self.cities.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' city deleted successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)



class BranchRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = BranchSerializer
    branches = Branch.objects.all()
    users = User.objects.all()
    def post(self, request, *args, **kwargs):
        # data = json.loads(request.data)
        data = request.data
        passwordNew = make_password(data['user']['password'])
        data['user']['password'] = passwordNew
        # serializer=self.get_serializer(data=request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        branch=serializer.save(createdby=self.request.user, modifiedby=self.request.user)
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

    def put(self, request):
        try:
            current_user = request.user
            branch_json = self.branches.filter(id=request.data['id'])
            branch_json.update(name=request.data['name'],
                             address=request.data['address'],
                             status=request.data['status'],
                             modifiedby=current_user.id,
                             modifiedon=datetime.utcnow())
            serializer = BranchSerializer(branch_json, many=True)

            branch = Branch.objects.get(pk=request.data['id'])
            user = User.objects.get(pk=branch.user_id)
            user_data = {
                'state' : request.data['user']['state'],
                'district': request.data['user']['district'],
                'city' : request.data['user']['city'],
                'phone' : request.data['user']['phone'],
                'email' : request.data['user']['email'],
                'username' : request.data['user']['username'],
                'password' : request.data['user']['password'],
            }
            user_serializer = UserCommonSerializer(user, data=user_data, partial=True)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Branch Details Updated Successfully',
                                "branch_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    # def put(self, request):
    #     try:
    #         current_user = request.user
    #         branch_json = self.branches.filter(id=request.data['id'])
    #         branch=Branch.objects.get(pk=request.data['id'])
    #         user_json = self.users.filter(id=branch.user_id)
    #         user_json.update(state=request.data['user']['state'],
    #                          district=request.data['user']['district'],
    #                          city=request.data['user']['city'],
    #                          phone=request.data['user']['phone'],
    #                          email=request.data['user']['email'],
    #                          username=request.data['user']['username'],
    #                          password=request.data['user']['password'])
    #         branch_json.update(name=request.data['name'],
    #                             address=request.data['address'],
    #                                 status=request.data['status'],
    #                                 user=user_json,
    #                                 modifiedby=current_user.id,
    #                                 modifiedon=datetime.utcnow())
    #         serializer = BranchSerializer(branch_json, many=True)
    #         status_code = status.HTTP_201_CREATED
    #         response = {'status': 'success', 'status_code': status_code, 'message': 'Branch Details Updated Successfully',
    #                     "branch_details": serializer.data, }
    #     except Exception as error:
    #         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    #         response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
    #                     'system_message': str(error)}
    #     return Response(response, status=status_code)

    def patch(self,request,id=None):
        try:
            current_user = request.user
            branch_json = self.branches.filter(id=id)
            branch = Branch.objects.get(id=id)
            if(branch.status==1):
                statusValue=0
            else:
                statusValue=1
            branch_json.update(status=statusValue,
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = BranchSerializer(branch_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Branch Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    def delete(self, request,id=None):
        try:
            self.branches.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' branch deleted successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)


class ReligionRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = ReligionSerializer
    religions = Religion.objects.all()
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

    def put(self, request):
        try:
            current_user = request.user
            religion_json = self.religions.filter(id=request.data['id'])
            religion_json.update(name=request.data['name'],
                                    status=request.data['status'],
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = ReligionSerializer(religion_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Religion Details Updated Successfully',
                        "religion_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self,request,id=None):
        try:
            current_user = request.user
            religion_json = self.religions.filter(id=id)
            religion = Religion.objects.get(id=id)
            if(religion.status==1):
                statusValue=0
            else:
                statusValue=1
            religion_json.update(status=statusValue,
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = ReligionSerializer(religion_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Religion Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    def delete(self, request,id=None):
        try:
            self.religions.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' Religion Deleted Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)

class CasteRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = CasteSerializer
    castes = Caste.objects.all()
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
    def put(self, request):
        try:
            current_user = request.user
            caste_json = self.castes.filter(id=request.data['id'])
            caste_json.update(name=request.data['name'],
                                    status=request.data['status'],
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = CasteSerializer(caste_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Caste Details Updated Successfully',
                        "caste_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self, request, id=None):
        try:
            current_user = request.user
            caste_json = self.castes.filter(id=id)
            caste = Caste.objects.get(id=id)
            if (caste.status == 1):
                statusValue = 0
            else:
                statusValue = 1
            caste_json.update(status=statusValue,
                                modifiedby=current_user.id,
                                modifiedon=datetime.utcnow())
            serializer = CasteSerializer(caste_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,
                        'message': 'Caste Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    def delete(self, request,id=None):
        try:
            self.castes.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' Caste Deleted Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)


class SubCasteRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = SubCasteSerializer
    subcastes = SubCaste.objects.all()
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

    def put(self, request):
        try:
            current_user = request.user
            subcaste_json = self.subcastes.filter(id=request.data['id'])
            subcaste_json.update(name=request.data['name'],
                                 caste=request.data['caste'],
                                    status=request.data['status'],
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = SubCasteSerializer(subcaste_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Sub Caste Details Updated Successfully',
                        "sub-caste_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self, request, id=None):
        try:
            current_user = request.user
            subcaste_json = self.subcastes.filter(id=id)
            subcaste = SubCaste.objects.get(id=id)
            if (subcaste.status == 1):
                statusValue = 0
            else:
                statusValue = 1
            subcaste_json.update(status=statusValue,
                                modifiedby=current_user.id,
                                modifiedon=datetime.utcnow())
            serializer = SubCasteSerializer(subcaste_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,
                        'message': 'Sub Caste Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    def delete(self, request,id=None):
        try:
            self.subcastes.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': 'Sub Caste Deleted Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)


class OccupationRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = OccupationSerializer
    occupations = Occupation.objects.all()
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

    def put(self, request):
        try:
            current_user = request.user
            occupation_json = self.occupations.filter(id=request.data['id'])
            occupation_json.update(name=request.data['name'],
                                    status=request.data['status'],
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = OccupationSerializer(occupation_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Occupation Details Updated Successfully',
                        "occupation_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self, request, id=None):
        try:
            current_user = request.user
            occupation_json = self.occupations.filter(id=id)
            occupation = Occupation.objects.get(id=id)
            if (occupation.status == 1):
                statusValue = 0
            else:
                statusValue = 1
            occupation_json.update(status=statusValue,
                                modifiedby=current_user.id,
                                modifiedon=datetime.utcnow())
            serializer = OccupationSerializer(occupation_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,
                        'message': 'Occupation Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    def delete(self, request,id=None):
        try:
            self.occupations.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' Occupation Deleted Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)

class EducationRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = EducationSerializer
    educations = Education.objects.all()
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

    def put(self, request):
        try:
            current_user = request.user
            education_json = self.educations.filter(id=request.data['id'])
            education_json.update(name=request.data['name'],
                                    status=request.data['status'],
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = EducationSerializer(education_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Education Details Updated Successfully',
                        "education_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self, request, id=None):
        try:
            current_user = request.user
            education_json = self.educations.filter(id=id)
            education = Education.objects.get(id=id)
            if (education.status == 1):
                statusValue = 0
            else:
                statusValue = 1
            education_json.update(status=statusValue,
                                modifiedby=current_user.id,
                                modifiedon=datetime.utcnow())
            serializer = EducationSerializer(education_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,'message': 'Education Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    def delete(self, request,id=None):
        try:
            self.educations.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' Education Deleted Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)


class LanguageRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = LanguageSerializer
    languages = Language.objects.all()
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

    def put(self, request):
        try:
            current_user = request.user
            language_json = self.languages.filter(id=request.data['id'])
            language_json.update(name=request.data['name'],
                                    status=request.data['status'],
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = LanguageSerializer(language_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Language Details Updated Successfully',
                        "language_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self, request, id=None):
        try:
            current_user = request.user
            language_json = self.languages.filter(id=id)
            language = Language.objects.get(id=id)
            if (language.status == 1):
                statusValue = 0
            else:
                statusValue = 1
            language_json.update(status=statusValue,
                                modifiedby=current_user.id,
                                modifiedon=datetime.utcnow())
            serializer = LanguageSerializer(language_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,'message': 'Language Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    def delete(self, request,id=None):
        try:
            self.languages.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' Language Deleted Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)

class SourceRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = SourceSerializer
    sources = Source.objects.all()
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

    def put(self, request):
        try:
            current_user = request.user
            source_json = self.sources.filter(id=request.data['id'])
            source_json.update(name=request.data['name'],
                                    status=request.data['status'],
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = SourceSerializer(source_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Source Details Updated Successfully',
                        "source_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self, request, id=None):
        try:
            current_user = request.user
            source_json = self.sources.filter(id=id)
            source = Source.objects.get(id=id)
            if (source.status == 1):
                statusValue = 0
            else:
                statusValue = 1
            source_json.update(status=statusValue,
                                modifiedby=current_user.id,
                                modifiedon=datetime.utcnow())
            serializer = SourceSerializer(source_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,'message': 'Source Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    def delete(self, request,id=None):
        try:
            self.sources.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' Source Deleted Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)

class MemberShipRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = MemberShipSerializer
    memberships = MemberShip.objects.all()
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        membership = serializer.save()
        return Response({
            "membership": MemberShipSerializer(membership, context=self.get_serializer_context()).data,
            "message": "Membership created successfully"
        })
    def get(self, request, id=None):
        if id:
            membership = MemberShip.objects.get(id=id)
            serializer = MemberShipSerializer(membership)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        memberships = MemberShip.objects.all()
        serializer = MemberShipSerializer(memberships, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            current_user = request.user
            membership_json = self.memberships.filter(id=request.data['id'])
            membership_json.update(planname=request.data['planname'],
                                   plantype=request.data['plantype'],
                                   duration=request.data['duration'],
                                   contactsno=request.data['contactsno'],
                                   amount=request.data['amount'],
                                    status=request.data['status'],
                                   smsenable=request.data['smsenable'],
                                   emailenable=request.data['emailenable'],
                                   personalassistance=request.data['personalassistance'],
                                   photozoom=request.data['photozoom'],
                                   sendinterest=request.data['sendinterest'],
                                   profilesuggestions=request.data['profilesuggestions'],
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            serializer = MemberShipSerializer(membership_json, many=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code, 'message': 'Membership Details Updated Successfully',
                        "source_details": serializer.data, }
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)

    def patch(self, request, id=None, param1=None):
        try:
            current_user = request.user
            membership_json = self.memberships.filter(id=id)
            membership = MemberShip.objects.get(id=id)
            if param1 == 'status':
                if (membership.status == 1):
                    statusValue = 0
                else:
                    statusValue = 1
                membership_json.update(status=statusValue,
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            if param1 == 'sms':
                if (membership.smsenable == 1):
                    smsValue = 0
                else:
                    smsValue = 1
                membership_json.update(smsenable=smsValue,
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            if param1 == 'email':
                if (membership.emailenable == 1):
                    emailValue = 0
                else:
                    emailValue = 1
                membership_json.update(emailenable=emailValue,
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            if param1 == 'passt':
                if (membership.personalassistance == 1):
                    passtValue = 0
                else:
                    passtValue = 1
                membership_json.update(personalassistance=passtValue,
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            if param1 == 'zoom':
                if (membership.photozoom == 1):
                    zoomValue = 0
                else:
                    zoomValue = 1
                membership_json.update(photozoom=zoomValue,
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            if param1 == 'interest':
                if (membership.sendinterest == 1):
                    interestValue = 0
                else:
                    interestValue = 1
                membership_json.update(sendinterest=interestValue,
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())
            if param1 == 'psugg':
                if (membership.profilesuggestions == 1):
                    psuggValue = 0
                else:
                    psuggValue = 1
                membership_json.update(profilesuggestions=psuggValue,
                                    modifiedby=current_user.id,
                                    modifiedon=datetime.utcnow())

            serializer = MemberShipSerializer(membership_json, partial=True)
            status_code = status.HTTP_201_CREATED
            response = {'status': 'success', 'status_code': status_code,'message': 'MemberShip Status Updated Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status_code, "message": "something went wrong",
                        'system_message': str(error)}
        return Response(response, status=status_code)
    def delete(self, request,id=None):
        try:
            self.memberships.filter(id=id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' Memberships Deleted Successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)
class StaffRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = StaffSerializer
    staff = Staff.objects.all()
    users = User.objects.all()
    def post(self, request, *args, **kwargs):
        parser_classes = (MultiPartParser, FormParser)
        photo = request.FILES["photo"]
        data = json.loads(request.data['data'])
        passwordNew = make_password(data['user']['password'])
        data['user']['password']=passwordNew
        original_filename, extension = os.path.splitext(photo.name)
        # file_name = slugify(data['user']['username'])
        photo.name =data['user']['username'] + extension
        # # fss = FileSystemStorage()
        # # file = fss.save(upload.name, upload)
        serializer = self.get_serializer(data=data)
        # serializer.is_valid(raise_exception=True)
        # staff = serializer.save()
        # serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        staff = serializer.save(photo=photo)
        return Response({
            "staff": StaffSerializer(staff, context=self.get_serializer_context()).data,
            "message": "Staff created successfully"
        })

    def get(self, request, id=None):
        if id:
            staff = Staff.objects.get(id=id)
            serializer = StaffSerializer(staff)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        staffall = Staff.objects.all()
        serializer = StaffSerializer(staffall, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request,id=None):
        try:
            staff = Staff.objects.get(id=id)
            photo_path = staff.photo.url
            self.staff.filter(id=id).delete()
            self.users.filter(id=staff.user_id).delete()
            # if photo_path:
            #     try:
            #         os.remove(photo_path)
            #     except FileNotFoundError:
            #         pass  # Image file doesn't exist
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': ' staff deleted successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)

class AgentRegisterView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = AgentSerializer
    agent = Agent.objects.all()
    users = User.objects.all()
    def post(self, request, *args, **kwargs):
        parser_classes = (MultiPartParser, FormParser)
        photo = request.FILES["photo"]
        data = json.loads(request.data['data'])
        passwordNew = make_password(data['user']['password'])
        data['user']['password'] = passwordNew
        original_filename, extension = os.path.splitext(photo.name)
        photo.name =data['user']['username'] + extension
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        agent = serializer.save(photo=photo)
        return Response({
            "agent": AgentSerializer(agent, context=self.get_serializer_context()).data,
            "message": "Agent created successfully"
        })

    def get(self, request, id=None):
        if id:
            agent = Agent.objects.get(id=id)
            serializer = AgentSerializer(agent)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        agentall = Agent.objects.all()
        serializer = AgentSerializer(agentall, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request,id=None):
        try:
            agent = Agent.objects.get(id=id)
            photo_path = agent.photo.url
            self.agent.filter(id=id).delete()
            self.users.filter(id=agent.user_id).delete()
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status_code': status_code, 'message': 'agent deleted successfully'}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {'status': 'failure', 'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': str(error)}
        return Response(response, status=status_code)

class StaffUserView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = StaffSerializer
    staff = Staff.objects.all()
    users = User.objects.all()

    def get(self, request, id=None):
        if id:
            staff = Staff.objects.get(user_id=id)
            serializer = StaffSerializer(staff)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        staffall = Staff.objects.all()
        serializer = StaffSerializer(staffall, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class AgentUserView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    serializer_class = AgentSerializer
    agent = Agent.objects.all()
    users = User.objects.all()

    def get(self, request, id=None):
        if id:
            agent = Agent.objects.get(user_id=id)
            serializer = AgentSerializer(agent)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        agentall = Agent.objects.all()
        serializer = AgentSerializer(agentall, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)