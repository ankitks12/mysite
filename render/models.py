from django.db import models


class UserDetail(models.Model):
    install_ts = models.DateTimeField(auto_now_add=True)
    update_ts = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    aadhar_card_no = models.CharField(blank=False, null=True, max_length=12)
    phone = models.CharField(max_length=10, null=False, blank=False)
    email_id = models.EmailField(null=True)
    expected_date_of_joining = models.DateField(null=True)

    class Meta:
        db_table = "user_detail"
