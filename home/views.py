import os
import subprocess
from tempfile import NamedTemporaryFile

import requests
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class RunNGSpiceCodeView(APIView):
    def post(self, request):
        ngspice_code = request.data.get("code", "")

        if not ngspice_code:
            return Response({"success": "false", "message": "No Ngspice code provided"})

        with NamedTemporaryFile(delete=False, suffix=".cir") as temp_input_file:
            temp_input_file.write(ngspice_code.encode())
            temp_input_file_path = temp_input_file.name

        with NamedTemporaryFile(delete=False, suffix=".out") as temp_output_file:
            temp_output_file_path = temp_output_file.name

        try:
            result = subprocess.run(
                ["ngspice", "-b", temp_input_file_path,
                    "-o", temp_output_file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            if result.returncode != 0:
                return Response({"error": result.stderr.strip() or "Ngspice failed to run"}, status=500)

            with open(temp_output_file_path, "r") as file:
                output_data = file.read()

            return Response({"output": output_data})

        finally:
            os.remove(temp_input_file_path)
            os.remove(temp_output_file_path)
