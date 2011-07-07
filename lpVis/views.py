from django.shortcuts import render_to_response, get_object_or_404
from lpVis.models import LandingPage, Portal

def lp_listing(request):
	customer_portal_id = request.GET.get("hubspot.marketplace.portal_id", None)
	if not customer_portal_id:
		# the customer's portal ID should not be 0
		return render_to_response("lpVis/error.html",
			{"error_message": "Need hubspot.marketplace.portal_id in the GET params"})
	landing_pages = LandingPage.objects.filter(portal=customer_portal_id)
	return render_to_response('lpVis/index.html', 
		{'latest_landing_pages': landing_pages })
