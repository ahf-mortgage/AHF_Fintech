from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    otp_code = models.CharField(max_length=6)  # OTP code, typically 6 digits
    generated_at = models.DateTimeField(default=timezone.now)  # Time when OTP was generated
    is_used = models.BooleanField(default=False)  # Flag to check if the OTP has been used

    class Meta:
        verbose_name = "OTP"
        verbose_name_plural = "OTPs"
        ordering = ['-generated_at']  # Order OTPs by generation time

    def __str__(self):
        return f"OTP for {self.user.username}: {self.otp_code} (Used: {self.is_used})"