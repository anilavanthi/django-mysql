from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from Masters.models import State,District,City,Country,Branch,Religion,Caste,SubCaste,Occupation,Education,Language,Source
from Users.serializers import UserCommonSerializer
from Users.models import User
from Masters.models import Staff

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = '__all__'
		# read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs

class StateSerializer(serializers.ModelSerializer):
	country_name = ReadOnlyField(source='country.name')
	class Meta:
		model = State
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs

class DistrictSerializer(serializers.ModelSerializer):
	country_name = ReadOnlyField(source='country.name')
	state_name = ReadOnlyField(source='state.name')
	class Meta:
		model = District
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs


class CitySerializer(serializers.ModelSerializer):
	country_name = ReadOnlyField(source='country.name')
	state_name = ReadOnlyField(source='state.name')
	district_name = ReadOnlyField(source='district.name')
	class Meta:
		model = City
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs


class BranchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Branch
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs


class ReligionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Religion
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs


class CasteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Caste
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs

class SubCasteSerializer(serializers.ModelSerializer):
	caste_name = ReadOnlyField(source='caste.name')
	class Meta:
		model = SubCaste
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs


class OccupationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Occupation
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs

class EducationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Education
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs

class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs


class SourceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Source
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs

class StaffSerializer(serializers.ModelSerializer):
	user = UserCommonSerializer()

	class Meta:
		model = Staff
		fields = '__all__'

	def create(self,validate_data):
		user_data = validate_data.pop('user')
		user = User.objects.create(**user_data)
		staff = Staff.objects.create(user=user,**validate_data)
		return staff