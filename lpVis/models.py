from django.db import models

class Portal(models.Model):
    portal_id = models.IntegerField()

class LandingPage(models.Model):
    portal = models.ForeignKey(Portal)
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=200)

class Visitor(models.Model):
    ip_address = models.IPAddressField()
    browser_width = models.IntegerField()
    browser_height = models.IntegerField()
    user_agent = models.CharField(max_length=200)

class InputEntry(models.Model):
    created = models.DateField(auto_now_add=True)
    # ID of whatever input field was focused or clicked on
    input_field = models.CharField(max_length=200)
    position_x = models.IntegerField()
    position_y = models.IntegerField()

class Visit(models.Model):
    landing_page = models.ForeignKey(LandingPage)
    visitor = models.ForeignKey(Visitor)
    input_entry = models.ForeignKey(InputEntry)
    created = models.DateField(auto_now_add=True)
    max_scroll_depth = models.IntegerField()

