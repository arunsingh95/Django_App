from .models import *
from .serializers import CustomerDetailSerializer, CustomerDetailPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CustomerDetailApi(APIView):
    def get_queryset(self):
        params = self.request.query_params
        query_dict = {i:params[i][0] for i in params}
        queryset = CustomerVisitDetails.objects.filter(**query_dict)
        return queryset

    def get(self, request):
        model = self.get_queryset()
        serializer = CustomerDetailSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerDetailPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditCustomerDetailApi(APIView):
    def get(self, request, customer_id):
        queryset = CustomerVisitDetails.objects.get(id=customer_id)
        print('get', queryset)
        serializer = CustomerDetailSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, customer_id):
        queryset = CustomerVisitDetails.objects.get(id=customer_id)
        serializer = CustomerDetailPostSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)