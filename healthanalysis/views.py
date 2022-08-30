from django.http import HttpResponse
from sentinelhub import SentinelHubRequest, DataCollection, MimeType, CRS, BBox, SHConfig, Geometry
import matplotlib.pyplot as plt
import requests
import os
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from healthanalysis.models import HealthAnalysis
from account.models import User
from healthanalysis.serializers import HealthAnalysisSerializer
import re
import pdb
import rasterio
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser
from cloudinary.templatetags import cloudinary
import cloudinary.uploader
import cloudinary.api
import string
import random


class HealthAnalysisList(APIView):

    """
    List all healthanalysis, or create a new healthanalysis.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        healthanalysis = HealthAnalysis.objects.all()

        userhealth = HealthAnalysis.objects.filter(user=request.user)
        serializer = HealthAnalysisSerializer(userhealth, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        name = request.data['name']
        box2 = request.data['bbox']
        coordinates2 = request.data['coordinates']
        time_from = request.data['time_from']
        time_to = request.data['time_to']
        user = request.data['user']
        config = SHConfig()
        config.sh_client_id = 'ab1ffd68-997e-43ed-b861-abddd6786d80'
        config.sh_client_secret = 'b2Kv#B~4A4p%w-a?Rt_~~8Yf.fFEy//OeG5}g6Bx'
        evalscript = """
        //VERSION=3
        function setup() {
        return{
        input: [{
        bands: ["B04", "B08"],
        units: "DN"
        }],
        output: {
        id: "default",
        bands: 1,
       sampleType: SampleType.FLOAT32
        }
        }
        }
        function evaluatePixel(sample) {
        let ndvi = (sample.B08 - sample.B04) / (sample.B08 + sample.B04)
        return [ ndvi ]
        }
        """

        bbox = BBox(bbox=box2, crs=CRS.WGS84)
        geometry = Geometry(
            geometry={"type": "Polygon", "coordinates": coordinates2}, crs=CRS.WGS84)

        request = SentinelHubRequest(
            data_folder="test_dir",
            evalscript=evalscript,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L2A,
                    time_interval=(time_from,time_to)


                ),
            ],
            responses=[
                SentinelHubRequest.output_response('default', MimeType.TIFF),
            ],
            bbox=bbox,
            geometry=geometry,
            size=[512, 514.207],
            config=config
        )
        response = request.get_data()
        image = response[0]
        output = np.nan_to_num(image)
        max_value = np.nanmax(output)
        min_value = np.nanmin(output)
        mean_value = np.nanmean(output)
        letters = string.ascii_lowercase
        randoms = ''.join(random.choice(letters) for i in range(10))
        ndvi_image = rasterio.open(
            randoms+'.tif', 'w', driver='GTiff', height=500, width=500, count=1, dtype='float32', crs='EPSG:4326', transform=rasterio.transform.from_bounds(*box2, 500, 500))
        ndvi_image.write(image, 1)

        ndvi_image.close()

        cloudinary.uploader.upload(
            randoms+'.tif', public_id=randoms, overwrite=True)
        data = cloudinary.api.resource(randoms)
        file_path = data.get('url')
        file_paths = randoms+'.tif'
        os.remove(file_paths)
        print(time_to)

        serializer = HealthAnalysisSerializer(
            data={'name': name, 'bbox': box2, 'coordinates': coordinates2,  'path': file_path, 'time_from': time_from, "time_to": time_to, 'min_value': min_value, 'max_value': max_value, 'mean_value': mean_value, 'user': user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HealthAnalysisDetail(APIView):
    """
    Retrieve, update or delete a healthanalysis instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return HealthAnalysis.objects.get(pk=pk)
        except HealthAnalysis.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        healthanalysis = self.get_object(pk)
        if healthanalysis.user == request.user:
            serializer = HealthAnalysisSerializer(healthanalysis)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'You are not authorized to view this data'})

    def put(self, request, pk, format=None):
        healthanalysis = self.get_object(pk)
        serializer = HealthAnalysisSerializer(
            healthanalysis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        healthanalysis = self.get_object(pk)
        healthanalysis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
