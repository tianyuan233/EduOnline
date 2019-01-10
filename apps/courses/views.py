from pure_pagination import PageNotAnInteger, Paginator
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from courses.models import Course
from operation.models import UserFavorite


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

        # 取出标签找到标签相同的course
        tag = course.tag
        if tag:
            # 从1开始否则会推荐自己
            relate_courses = Course.objects.filter(tag=tag)[1:2]
        else:
            relate_courses = []

        # 是否收藏课程
        has_fav_course = False
        has_fav_org = False
        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        return render(request, "course-detail.html",
                      {
                          "course":course,
                          "relate_courses": relate_courses,
                          "has_fav_course": has_fav_course,
                          "has_fav_org": has_fav_org,
                      })







