from pure_pagination import PageNotAnInteger, Paginator
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from courses.models import Course


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all()

        hot_courses = Course.objects.all().order_by("-students")[:3]

        search_keywords = request.GET.get('keywords', '')

        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_courses, 6, request=request)
        courses = p.page(page)
        return render(request, "course-list.html", {
            "all_course": courses,
            "sort": sort,
            "hot_courses": hot_courses,
            "search_keywords": search_keywords
        })


class CourseDetailView(View):
    def get(self, request, course_id):
        """课程详情页"""
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        return render(request, "course-detail.html",
                      {
                          "course":course
                      })







