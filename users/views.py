from django.shortcuts import render
from django.views import View
from .models import *

class UserFilterView(View):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        total_users_count = Usrs.objects.count()
        filtered_users_count = 0
        filtered_users = Usrs.objects.all()
        countries = Country.objects.all()
        regions = Region.objects.all()
        districts = District.objects.all()

        country_param = request.GET.get('country', '')
        region_param = request.GET.get('region', '')
        district_param = request.GET.get('district', '')
        min_age = request.GET.get('min_age', 0)
        max_age = request.GET.get('max_age', 100)

        if country_param:
            selected_country_places = Place.objects.filter(country__name=country_param)
            filtered_users = Usrs.objects.filter(place__in=selected_country_places)

            if region_param:
                selected_country_region_places = Place.objects.filter(country__name=country_param, region__name=region_param)
                filtered_users = filtered_users.filter(place__in=selected_country_region_places)

                if district_param:
                    selected_country_region_distric_places = Place.objects.filter(country__name=country_param, region__name=region_param, district__name=district_param)
                    filtered_users = filtered_users.filter(place__in=selected_country_region_distric_places)

                if min_age and max_age:
                    if type(min_age) == str:
                        min_age = int(min_age)
                    if type(max_age) == str:  # Fix the typo here
                        max_age = int(max_age)

                    filtered_users = filtered_users.filter(age__gte=min_age, age__lte=max_age)

        filtered_users_count = filtered_users.count()

        context = {
            'total_users_count': total_users_count,
            'filtered_users_count': filtered_users_count,
            'selected_param': bool(country_param or region_param or (min_age and max_age)),
            'filtered_users': filtered_users,
            'countries': countries,
            'regions': regions,
            'districts': districts,
        }   

        return render(request, self.template_name, context)


