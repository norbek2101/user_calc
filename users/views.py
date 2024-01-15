from django.shortcuts import render
from django.views import View
from .models import Usrs

class UserFilterView(View):
    template_name = 'user_filter.html'

    def get(self, request, *args, **kwargs):
        total_users_count = Usrs.objects.count()
        filtered_users_count = 0
        filtered_users = Usrs.objects.all()

        regions = [
            'Andijan', 'Bukhara', 'Fergana', 'Jizzakh', 'Karakalpakstan',
            'Namangan', 'Navoiy', 'Qashqadaryo', 'Samarqand', 'Sirdaryo',
            'Surxondaryo', 'Tashkent'
        ]

        region_param = request.GET.get('region', '')
        min_age = request.GET.get('min_age', 0)
        max_age = request.GET.get('max_age', 100)

        if type(min_age) == str:
            min_age = int(min_age)
            
        if type(min_age) == str:
            min_age = int(min_age)


        if region_param:
            filtered_users = Usrs.objects.filter(city=region_param)
            if min_age and max_age:
                filtered_users = filtered_users.filter(age__gte=min_age, age__lte=max_age)

        if min_age and max_age:
            filtered_users = filtered_users.filter(age__gte=min_age, age__lte=max_age)

        filtered_users_count = filtered_users.count()

        context = {
            'total_users_count': total_users_count,
            'filtered_users_count': filtered_users_count,
            'selected_param': bool(region_param or (min_age and max_age)),
            'filtered_users': filtered_users,  # Pass the filtered users to the template
            'regions': regions,  # Pass the list of regions to the template
        }

        return render(request, self.template_name, context)
