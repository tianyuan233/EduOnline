from datetime import datetime

from django.db import models


# Create your models here.

# 城市表
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市")
    # 城市描述：备用不一定展示出来
    desc = models.CharField(max_length=200, verbose_name="描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程机构表
class CourseOrg(models.Model):
    ORG_CHOICES = (
        ("pxjg", "培训机构"),
        ("gx", "高校"),
        ("gr", "个人"),
    )
    name = models.CharField(max_length=50, verbose_name="机构名称")
    # 机构描述，后面会替换为富文本展示
    desc = models.TextField(verbose_name="机构描述")
    # 机构类别:
    category = models.CharField(max_length=20, choices=ORG_CHOICES, verbose_name="机构类别", default="pxjg")
    tag = models.CharField(max_length=10, default="国内名校", verbose_name="机构标签")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="Logo", max_length=100, null=True,blank=True)
    address = models.CharField(max_length=150, verbose_name="机构地址")
    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name="所在城市")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    course_nums = models.IntegerField(default=0, verbose_name="课程数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "课程机构: {0}".format(self.name)


# 教师表
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name="教师名称")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    age = models.IntegerField(default=18, verbose_name="年龄")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(default='', upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100, null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "[{0}]的教师: {1}".format(self.org, self.name)
