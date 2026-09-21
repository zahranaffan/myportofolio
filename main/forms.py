from django.forms import ModelForm, TextInput, Textarea, URLInput, DateTimeInput, NumberInput, Select
from main.models import Experience, Achievement


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

class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        fields = [
            "title",
            "description",
            "year",
            "organization",
            "category",
            "photo",
        ]

        labels = {
            "title": "Nama Pencapaian",
            "description": "Deskripsi Pencapaian",
            "year": "Tahun",
            "organization": "Penyelenggara",
            "category": "Kategori",
            "photo": "URL Foto",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Juara 1 Business Case Competition",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pencapaianmu",
                    "rows": 3,
                }
            ),
            "year": NumberInput(
                attrs={
                    "placeholder": "2026",
                }
            ),
            "organization": TextInput(
                attrs={
                    "placeholder": "Contoh: Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "category": Select(),
            "photo": URLInput(
                attrs={
                    "placeholder": "https://example.com/image.jpg",
                }
            ),
        }