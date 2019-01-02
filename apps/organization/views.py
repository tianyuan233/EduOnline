from django.shortcuts import render
# Create your views here.
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger

from organization.models import CityDict, CourseOrg


class OrgListView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        all_cities = CityDict.objects.all()

        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")

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
            'org_nums': org_nums,
            'category': category,
            'city_id': city_id,
            'hot_orgs': hot_orgs,
            'sort':sort,
        })
