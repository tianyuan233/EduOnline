from django.shortcuts import render
# Create your views here.
from django.views.generic import View

from organization.models import CityDict, CourseOrg
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

class OrgListView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        all_cities = CityDict.objects.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, 'org_list.html', {
            'all_cities': all_cities,
            'all_orgs': orgs,
            'org_nums':org_nums})
