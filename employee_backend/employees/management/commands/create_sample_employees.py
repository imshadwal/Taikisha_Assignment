from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from employees.models import Employee
from PIL import Image, ImageDraw, ImageFont
import io
import random

class Command(BaseCommand):
    help = 'Create sample employees with generated images'

    def handle(self, *args, **options):
        # Clear existing employees
        Employee.objects.all().delete()

        # Sample employee data
        employees_data = [
            {'name': 'John Smith', 'employee_id': 'EMP001', 'age': 28},
            {'name': 'Sarah Johnson', 'employee_id': 'EMP002', 'age': 32},
            {'name': 'Michael Brown', 'employee_id': 'EMP003', 'age': 29},
            {'name': 'Emily Davis', 'employee_id': 'EMP004', 'age': 26},
            {'name': 'David Wilson', 'employee_id': 'EMP005', 'age': 35},
            {'name': 'Lisa Anderson', 'employee_id': 'EMP006', 'age': 31},
            {'name': 'Shadwal Sinha', 'employee_id': 'EMP007', 'age': 25},
            {'name': 'Harsh Mittal', 'employee_id': 'EMP008', 'age': 23},
            {'name': 'Satyam Tiwari', 'employee_id': 'EMP009', 'age': 26},
            {'name': 'Rohit Chaudhary', 'employee_id': 'EMP0010', 'age': 27}
        ]

        colors = [
            (73, 109, 137),
            (67, 170, 139),
            (114, 82, 161),
            (150, 111, 51),
            (65, 131, 215),
            (203, 67, 53),
            (203, 67, 53),
            (65, 131, 215),
            (203, 67, 53),
            (65, 131, 215),
        ]

        for i, emp_data in enumerate(employees_data):
            # Create a simple colored placeholder image with initials
            img = Image.new('RGB', (200, 200), color=colors[i])
            draw = ImageDraw.Draw(img)

            # Get initials
            name_parts = emp_data['name'].split()
            initials = ''.join([part[0] for part in name_parts])

            # Draw initials in the center
            try:
                font = ImageFont.truetype("Arial", 60)
            except:
                font = ImageFont.load_default()

            # Calculate text position to center it
            bbox = draw.textbbox((0, 0), initials, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (200 - text_width) // 2
            y = (200 - text_height) // 2

            draw.text((x, y), initials, fill='white', font=font)

            # Save to bytes
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG')
            img_content = ContentFile(img_io.getvalue(), f"{emp_data['employee_id']}.jpg")

            employee = Employee.objects.create(
                name=emp_data['name'],
                employee_id=emp_data['employee_id'],
                age=emp_data['age'],
                photo=img_content
            )

            self.stdout.write(
                self.style.SUCCESS(f'Successfully created employee: {employee.name}')
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully created 10 sample employees with generated images')
        )
