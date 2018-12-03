from django.shortcuts import render
# Create your views here.
from django.views.generic import View

from organization.models import CityDict, CourseOrg


class OrgListView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        all_cities = CityDict.objects.all()
        return render(request, 'org_list.html', {
            'all_cities': all_cities,
            'all_orgs': all_orgs,
            'org_nums':org_nums})
