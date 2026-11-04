from django.forms import ModelForm, TextInput, Textarea, URLInput, DateTimeInput, Select
from main.models import Experience, Project

from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori",
            "thumbnail": "URL Thumbnail",
            "ended_at": "Tanggal Berakhir",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Software Engineer Intern",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalamanmu",
                    "rows": 3,
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/image.jpg",
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Judul pengalaman tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError("Deskripsi pengalaman tidak boleh hanya berisi tag HTML.")
        return description

    def clean_thumbnail(self):
        return strip_tags(self.cleaned_data["thumbnail"]).strip()

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Tech Stack",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Aplikasi Jadwal",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan fungsi dan tujuan proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Contoh: Django, Python, JavaScript",
                    "maxlength": 255,
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://example.com",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://example.com/image.jpg",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError("Deskripsi proyek tidak boleh hanya berisi tag HTML.")
        return description

    def clean_tech_stack(self):
        tech_stack = strip_tags(self.cleaned_data["tech_stack"]).strip()
        if not tech_stack:
            raise ValidationError("Tech stack tidak boleh hanya berisi tag HTML.")
        return tech_stack

    def clean_project_url(self):
        return strip_tags(self.cleaned_data["project_url"]).strip()

    def clean_project_image_url(self):
        return strip_tags(self.cleaned_data["project_image_url"]).strip()
