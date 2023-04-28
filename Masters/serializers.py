from rest_framework import serializers
from Masters.models import State,District,City,Country,Branch,Religion,Caste,SubCaste,Occupation,Education,Language,Source

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = '__all__'
		# read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs

class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model = State
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs

class DistrictSerializer(serializers.ModelSerializer):
	class Meta:
		model = District
		fields = '__all__'
		read_only_fields = ['user']

	def validate(self, attrs):
		attrs['createdby'] = self.context['request'].user
		return attrs


class CitySerializer(serializers.ModelSerializer):
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

