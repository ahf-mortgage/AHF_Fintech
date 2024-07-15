from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse

class FileViewSet(APIView):
    """
    API endpoint that allows users to download a file.
    """

    def get(self, request, *args, **kwargs):
        # Open the file in binary mode
        with open("nodata.txt", "rb") as file:
            print("file=",file)
            # Create a FileResponse object with the file content
            response = FileResponse(file, content_type="application/octet-stream")

            # Set the Content-Disposition header to provide the file name
            response['Content-Disposition'] = 'attachment; filename="db.sqlite3"'

        return response
