from django.db import models

class Parentmodel(models.Model):
    fatherName = models.CharField(max_length=100)
    fatherOccupation = models.CharField(max_length=100)
    fatherEmail = models.CharField(max_length=100)
    fatherMobile = models.CharField(max_length=100)
    motherName = models.CharField(max_length=100)
    motherEmail = models.CharField(max_length=100)
    motherMobile = models.CharField(max_length=100)
    presentAddress = models.TextField()
    permanentAddress = models.TextField()

    def __str__(self):
        return f"{self.fatherName} && {self.motherName}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Student_id = models.CharField(max_length=100)
    
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]
    )

    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=100)
    religion = models.CharField(max_length=20)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=15)
    section = models.CharField(max_length=15)

    student_image = models.ImageField(upload_to='student/', blank=True)

    parent = models.OneToOneField(Parentmodel, on_delete=models.CASCADE)

    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.first_name
