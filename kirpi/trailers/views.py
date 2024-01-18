from datetime import datetime
from decimal import Decimal
from io import BytesIO
from typing import TYPE_CHECKING

from kirpi.paramaters.models import Price
from kirpi.trailers.models import Trailer
from kirpi.trailers.serializers import DetailTrailerSerializer, ListTrailersSerializer

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.views import APIView

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


if TYPE_CHECKING:
    from django.db.models.query import QuerySet


class ListCreateTrailersView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListTrailersSerializer

    def get_queryset(self) -> "QuerySet[Trailer]":
        return Trailer.objects.filter().order_by("-date")

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.check_object_permissions(request, self)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)


class DetailTrailerView(RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = DetailTrailerSerializer

    def get_queryset(self) -> "QuerySet[Trailer]":
        return Trailer.objects.filter(id=self.kwargs["pk"])
    
    def patch(self, request, *args, **kwargs):
        trailer = Trailer.objects.get(id=self.kwargs["pk"])
        trailer.last_date = trailer.date
        trailer.last_t0 = trailer.t0
        trailer.last_t1 = trailer.t1
        trailer.last_t2 = trailer.t2
        trailer.last_t3 = trailer.t3
        trailer.last_ri = trailer.ri
        trailer.last_rc = trailer.rc
        trailer.t0 = Decimal(request.data["t0"])
        trailer.t1 = Decimal(request.data["t1"])
        trailer.t2 = Decimal(request.data["t2"])
        trailer.t3 = Decimal(request.data["t3"])
        trailer.ri = Decimal(request.data["ri"])
        trailer.rc = Decimal(request.data["rc"])
        trailer.date = datetime.now()
        trailer.price = (trailer.t0 - trailer.last_t0) * Price.objects.first().price
        trailer.save()
        return Response(data=trailer.serial_number, status=HTTP_200_OK)


class TrailerCountView(APIView):
    def get(self, request, format=None):
        trailer_count = Trailer.objects.filter().count()
        return Response({"trailer_count": trailer_count}, status=HTTP_200_OK)
from reportlab.pdfgen import canvas

class TrailerBillView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        trailer = get_object_or_404(Trailer, id=pk)
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{trailer.serial_number}_{datetime.now().date()}.pdf"'

        pdf_buffer = BytesIO()
        pdf = SimpleDocTemplate(pdf_buffer, pagesize=letter)

        table_data = [
            ["ELEKTRIK BILDIRIM"],
            ["SERI NUMARASI", trailer.serial_number],
            ["ÖNCEKI SAYAÇ ÖLÇÜM TARIHI", str(trailer.last_date.date())],
            ["ÖNCEKI SAYAÇ ÖLÇÜM DEGERI", trailer.last_t0],
            ["SON SAYAÇ ÖLÇÜM TARIHI", str(trailer.date.date())],
            ["SON SAYAÇ ÖLÇÜM DEGERI", trailer.t0],
            ["FIYAT", trailer.price],
        ]

        table = Table(table_data, colWidths=[200, 200])
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.bisque),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.lightskyblue),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 30),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ])
        table.setStyle(style)

        pdf.build([table])

        pdf_buffer.seek(0)
        response.write(pdf_buffer.read())

        return response