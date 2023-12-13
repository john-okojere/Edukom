from django.db import models
import uuid
from django.utils import timezone

cc= (
    ('Pre-nursery','Pre-nursery'),
    ('Nursery 1','Nursery 1'),
    ('Nursery 2','Nursery 2'),
    ('Primary 1','Primary 1'),
    ('Primary 1','Primary 1'),
    ('Primary 2','Primary 2'),
    ('Primary 3','Primary 3'),
    ('Primary 4','Primary 4'),
    ('Primary 5','Primary 5'),
    ('JSS 1','JSS 1'),
    ('JSS 2','JSS 2'),
    ('JSS 3','JSS 3'),
    ('SSS 1','SSS 1'),
    ('SSS 2','SSS 2'),
    ('SSS 3','SSS 3'),
)
lesson_choices = (
    ('Physical lessons', 'Physical lessons'),
    ('Online lessons', 'Online lessons'),
)

goals = (
    ('improve phonics, reading and writing', 'improve phonics, reading and writing'),
    ('Help with assignments and school work', 'Help with assignments and school work'),
    ('Bulid foundation and confidence','Bulid foundation and confidence'),
    ('Home schooling','Home schooling'),
    ('Special needs support','Special needs support'),
)
Curriculums = (
    ('Nigerian', 'Nigerian'),
    ('British', 'British'),
    ('American', 'American'),
    ('IPC', 'IPC'),
    ('Not sure', 'Not sure'),
)
tutor_gender = (
    ('Any gender is fine','Any gender is fine'),
    ('Male','Male'),
    ('Female','Female'),

)

subjects = (
    ('Math','Math'),
    ('English','English'),
    ('Physics','Physics'),
    ('Lit','Lit'),
    ('Chemistry','Chemistry'),
    ('History','History'),
    ('ICT','ICT'),
    ('French','French'),
    ('Government','Government'),
    ('Civic','Civic'),
    ('Business','Business'),
    ('Verbal','Verbal'),
    ('Geography','Geography'),
    ('Coding','Coding'),
    ('commercial','commercial'),
)
days = (
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
)

class Guardian(models.Model):
    uid = models.UUIDField( default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)    
    last_name = models.CharField(max_length=255)
    email = models.EmailField( verbose_name="Active Email")
    phone = models.CharField(verbose_name="Phone Number", max_length=255)
    hear = models.CharField(verbose_name="How did you hear about us", max_length=255)

    lesson_type = models.CharField(max_length=255, choices=lesson_choices, verbose_name="Do you prefer inlesson or online lesson?")
    date_joined = models.DateTimeField(default=timezone.now)
    curriculum = models.CharField(max_length=255)  

    def __str__(self):
        return f'{self.uid}'

class AboutChild(models.Model):
    guardian = models.OneToOneField(Guardian, on_delete=models.CASCADE, related_name='AboutChild')
    child_class = models.CharField(max_length=255, choices=cc, verbose_name="Class of child")
    goal = models.CharField(max_length=255, choices=goals)
    subject = models.CharField(max_length=255)
    about = models.TextField(verbose_name="Tell us a bit about this child")
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.guardian}'

class Location(models.Model):
    guardian = models.OneToOneField(Guardian, on_delete=models.CASCADE, related_name="Location")
    state = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.guardian}'

class Lesson(models.Model):
    guardian = models.OneToOneField(Guardian, on_delete=models.CASCADE, related_name="Lesson")
    days = models.CharField(max_length=255, verbose_name="What days do you want the lesson to hold?")
    start = models.DateField(verbose_name="What days do you want to start?")
    weeks = models.IntegerField(verbose_name="For how long (Weeks)?")
    hour_per_day = models.IntegerField(verbose_name="How many hours per day?")
    start_time = models.TimeField( verbose_name="from what time?")


class GuardianEmail(models.Model):
    guardian = models.OneToOneField(Guardian, on_delete=models.CASCADE, related_name="GuardianEmail")
    sent = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.guardian}'

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'
