from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you that I love you"
    #     )

    def handle(self, *args, **options):
        amenities = [
            "Beach essentials",
            "Dryer",
            "Essential",
            "Laptop-friendly workspace",
            "Washer",
            "Wifi",
            "Facilities",
            "Pool",
            "Coffee maker",
            "Cooking basics",
            "Dishes and silverware",
            "Kitchen",
            "Refrigerator",
            "Stove",
            "Lockbox",
            "Private entrance",
            "Luggage dropoff allowed",
            "Long term stays allowed",
            "Bed linens",
            "Hair dryer",
            "Hangers",
            "Shampoo",
            "BBQ grill",
            "Patio or balcony",
            "Garden or backyard",
            "Fire extinguisher",
            "Carbon monoxide alarm",
            "Smoke alarm",
            "First aid kit",
            "Air conditioning",
            "Heating",
            "TV",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(amenities)} Amenities created!"))
