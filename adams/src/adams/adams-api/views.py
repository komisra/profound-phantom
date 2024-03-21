import logging
from django.views.decorators.http import required_http_methods
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.forms.models import model_to_dict
from django.conf import settings
from 
import json

logger = logging.getLogger(__name__)

# get request
@require_http_methods(["GET"])
def get_data(request):

# post request
@require_http_methods(["POST"])
def post_data(request):
    if not request.body:
        return HttpResponseBadRequest

    try:
        # load data from JSON request body
        data = json.loads(request.body)
    except ValueError as e:
        return HttpResponseBadRequest()

    for value in data:
        if (all key in data for key in ('contract_name', 'location', 'external_first_last_name', 'internal_first_last_name')):
            new_entry = VendorData.objects.create(**test)
            inserted_rows.append(model_to_dict(new_test))

    return JsonResponse({"inserted_rows": inserted_rows, safe=False})

# remove displayed based on request
@require_http_methods(["POST"])
def update_data(request):
    # fail if NO REQUEST BODY
    if not request.body:
        return HttpResponseBadRequest

    try:
        # load data from JSON request body
        data = json.loads(request.body)
    except ValueError as e:
        return HttpResponseBadRequest()
