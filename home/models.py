from django.db import models


# Create your models here.


class side_bar(models.Model):
    side_bar_name = models.CharField(max_length=250, default="No data")

    def __str__(self) -> str:
        return str(self.side_bar_name)


class Folder(models.Model):
    folder_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.folder_name)


class Farmer(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True,blank=True)
    supporting_files = models.FileField(default='no file', upload_to="files", null=True, blank=True)
    supporting_images = models.ImageField(default='no image', upload_to='pics', null=True, blank=True)
    time = models.TimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Employement(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    supporting_files = models.FileField(default='no file', upload_to="files", null=True, blank=True)
    supporting_images = models.ImageField(default='no image', upload_to='pics', null=True, blank=True)
    time = models.TimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.title)


class School(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    supporting_files = models.FileField(default='no file', upload_to="files", null=True, blank=True)
    supporting_images = models.ImageField(default='no image', upload_to='pics', null=True, blank=True)
    time = models.TimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Blood_Donor(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    supporting_files = models.FileField(default='no file', upload_to="files", null=True, blank=True)
    supporting_images = models.ImageField(default='no image', upload_to='pics', null=True, blank=True)
    time = models.TimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Convid_Plasma(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    supporting_files = models.FileField(default='no file', upload_to="files", null=True, blank=True)
    supporting_images = models.ImageField(default='no image', upload_to='pics', null=True, blank=True)
    time = models.TimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.title)


class APCS_Rules(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    supporting_files = models.FileField(default='no file', upload_to="files", null=True, blank=True)
    supporting_images = models.ImageField(default='no image', upload_to='pics', null=True, blank=True)
    time = models.TimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.title)


class APCS_Conduct_Rules(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    supporting_files = models.FileField(default='no file', upload_to="files", null=True, blank=True)
    supporting_images = models.ImageField(default='no image', upload_to='pics', null=True, blank=True)
    time = models.TimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.title)


class APCS_Leave_Rules(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    supporting_files = models.FileField(default='no file', upload_to="files", null=True, blank=True)
    supporting_images = models.ImageField(default='no image', upload_to='pics', null=True, blank=True)
    time = models.TimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.title)
