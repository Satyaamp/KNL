from django.contrib import admin
from .models import Registration
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
import os

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'fathers_name', 'contact', 'aadhar_number', 'batch', 'seat_number')
    search_fields = ('name', 'fathers_name', 'contact', 'aadhar_number', 'batch', 'seat_number')
    actions = ['export_as_pdf']

    def export_as_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="registrations.pdf"'

        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        # === Add Logo ===
        logo_path = os.path.join('static', 'images', 'logo.jpeg')  # Adjust path as needed
        try:
            p.drawImage(logo_path, 40, height - 80, width=60, height=60, preserveAspectRatio=True, mask='auto')
        except Exception as e:
            print(f"Logo error: {e}")

        # === Title ===
        p.setFont("Helvetica-Bold", 16)
        p.drawCentredString(width / 2.0, height - inch, "Library Registrations")

        # === Column Setup ===
        x_list = [
            40,   # Name
            110,  # Father's Name
            200,  # Contact
            270,  # Aadhaar
            340,  # Batch
            400,  # Seat No
            470,  # Profile Pic
        ]
        col_widths = [70, 90, 70, 70, 60, 70, 60]
        row_height = 80
        headers = ['Name', "Father's Name", 'Contact', 'Aadhaar', 'Batch', 'Seat No.', 'Profile']

        y = height - 1.5 * inch

        def draw_header():
            p.setFont("Helvetica-Bold", 9)
            for i, header in enumerate(headers):
                p.rect(x_list[i], y, col_widths[i], 20, stroke=1, fill=0)
                p.drawString(x_list[i] + 2, y + 5, header)

        draw_header()
        y -= row_height

        p.setFont("Helvetica", 7.5)

        for reg in queryset:
            if y < 100:
                p.showPage()
                y = height - 1.5 * inch

                # Redraw logo and title on new page
                try:
                    p.drawImage(logo_path, 40, height - 80, width=60, height=60, preserveAspectRatio=True, mask='auto')
                except Exception as e:
                    print(f"Logo error: {e}")

                p.setFont("Helvetica-Bold", 16)
                p.drawCentredString(width / 2.0, height - inch, "Library Registrations")

                p.setFont("Helvetica-Bold", 9)
                draw_header()
                y -= row_height
                p.setFont("Helvetica", 7.5)

            # Draw text fields
            fields = [
                str(reg.name or "N/A"),
                str(reg.fathers_name or "N/A"),
                str(reg.contact or "N/A"),
                str(reg.aadhar_number or "N/A"),
                str(reg.batch or "N/A"),
                str(reg.seat_number or "N/A")
            ]

            for i in range(6):
                p.rect(x_list[i], y, col_widths[i], row_height, stroke=1, fill=0)
                p.drawString(x_list[i] + 2, y + row_height - 12, fields[i])

            # Draw profile picture
            p.rect(x_list[6], y, col_widths[6], row_height, stroke=1, fill=0)
            try:
                if reg.pic:
                    p.drawImage(
                        ImageReader(reg.pic.path),
                        x_list[6] + 2, y + 5,
                        width=col_widths[6] - 4,
                        height=row_height - 10,
                        preserveAspectRatio=True
                    )
            except Exception as e:
                print(f"Profile pic error: {e}")

            y -= row_height

        p.save()
        return response

    export_as_pdf.short_description = "Export Selected as PDF"
