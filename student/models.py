from django.db import models
from clss.models import Clss
from staff.models import Staff
from django.utils import timezone

# Create your models here.
class Student(models.Model):

    GENDER = [
        ('m', 'male'),
        ('f', 'female'),
        ('o', 'other')
    ]
    
    avatar = models.ImageField(upload_to='uploads/', blank=True, null=True)
    firstname = models.CharField(max_length=20, blank=False, null=False, default='Firstname')
    lastname = models.CharField(max_length=50, blank=False, null=False, default='Last Name')
    other_names = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=30, blank=False, null=False)
    religion = models.CharField(max_length=30, blank=False, null=False)
    previous_school = models.CharField(verbose_name='Previous School (if any)', max_length=255, blank=True, null=True)
    has_siblings = models.BooleanField(default=False)
    number_of_siblings = models.IntegerField()
    gender = models.CharField(max_length=2, choices=GENDER, default='o')

    # parents
    guardian = models.CharField(verbose_name='Name of Guardian', blank=False, null=False, default='Guardian Name', max_length=255 )
    g_occupation = models.CharField(verbose_name='Guardian Occupation', blank=True, null=True, max_length=255)
    g_residential_address = models.CharField(verbose_name='Guardian Residential Address', blank=True, null=True, max_length=255)
    g_home_tel = models.CharField(verbose_name='Guardian Home Phone', blank=True, null=True, max_length=255)
    g_office_tel = models.CharField(verbose_name='Guardian Office Phone', blank=True, null=True, max_length=255)
    g_postal_address = models.CharField(verbose_name='Guardian Postal Address', blank=True, null=True, max_length=255)

    # bools
    lives_with_both_parents = models.BooleanField(verbose_name='Child lives with both parents', default=False)
    lives_with_mother = models.BooleanField(verbose_name='Child lives with Mother', default=False)
    lives_with_father = models.BooleanField(verbose_name='Child lives with Father', default=False)

    clss = models.ForeignKey(Clss, on_delete=models.CASCADE)
    assigned_teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class HealthReport(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    weight_at_birth = models.IntegerField(default=0)
    present_weight = models.IntegerField(default=0)
    doctor = models.CharField(verbose_name='Doctor name and Number', max_length=255, blank=False, null=False, default='eg. Jojo Thompson, 0540609437')

    # illness
    has_asthma = models.BooleanField(verbose_name='Has Asthma?', default=False)
    has_chicken_pox = models.BooleanField(verbose_name='Has Chicken Pox?', default=False)
    has_convulsion = models.BooleanField(verbose_name='Has Convulsion?', default=False)
    has_whooping_cough = models.BooleanField(verbose_name='Has Whooping cough?', default=False)
    has_mumps = models.BooleanField(verbose_name='Has Mumps?', default=False)
    has_typhoid = models.BooleanField(verbose_name='Has Typhoid?', default=False)
    has_tb = models.BooleanField(verbose_name='Has Tuberculosis?', default=False)
    has_measles = models.BooleanField(verbose_name='Has Measles?', default=False)
    has_sickle_cell = models.BooleanField(verbose_name='Has Sickle Cell?', default=False)
    allergies = models.TextField()
    date_of_application = models.DateField(default=timezone.now)

    def __str__(self):
        return self.student.get_full_name()