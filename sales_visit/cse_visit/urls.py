# from django.conf.urls import url
# from . import views
# from . import api

# urlpatterns = [
#     # URLS
#     url(r'^$', views.user_login, name='user_login'),
#     url(r'^register/$', views.register, name='register'),
#     url(r'^dashboard/$', views.dashboard, name='dashboard'),
#     url(r'^user_logout/$', views.user_logout, name='user_logout'),
#     url(r'^add_customer/$', views.add_customer, name='add_customer'),
#     url(r'^edit_customer/(?P<id>\d+)/$', views.edit_customer, name='edit_customer'),
#     url(r'^edit_status/$', views.edit_status, name='edit_status'),
#     url(r'^reports/$', views.reports, name='reports'),

#     # API'S
#     url(r'^api/customer_details/$', api.CustomerDetailApi.as_view(), name='customer_details_api'),
#     url(r'^api/customer_details/edit/(?P<customer_id>\d+)$', api.EditCustomerDetailApi.as_view(), name='customer_details_edit_api')
# ]

X = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'ap-south-1', 'eventTime': '2020-03-30T08:11:51.769Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AKS7EOC9CU2G8'}, 'requestParameters': {'sourceIPAddress': '223.227.1.114'}, 'responseElements': {'x-amz-request-id': 'D8B25E69B8A224F6', 'x-amz-id-2': 'hVkT7DRDuva47pw9YzeZYvCs1/MNVI05z+rddYUwz4XIZBcrz2cq+VbjbaZXHtLnQ+5ZRSn5Rdr3o3H6mxnuCVxVtj2u/Yp0'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'ff5b7d79-b133-41ee-a509-7f70217ad7e3', 'bucket': {'name': 'arundev-file', 'ownerIdentity': {'principalId': 'AKS7EOC9CU2G8'}, 'arn': 'arn:aws:s3:::arundev-file'}, 'object': {'key': 'Desert.jpg', 'size': 845941, 'eTag': 'ba45c8f60456a672e003a875e469d0eb', 'sequencer': '005E81A9CF7238E2DA'}}}]}
for i in X:
	print (X['Records'][0]['s3']['bucket']['name'])