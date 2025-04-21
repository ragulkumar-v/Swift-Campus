from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_complaint_confirmation(user_email, complaint_title, complaint_description, complaint_date):
    """
    Send a confirmation email to the user who submitted the complaint.
    """
    subject = "Don't Reply - Complaint Submission Confirmation"
    message = (
        f"Dear Student,\n\n"
        "Thank you for your submission."
        f"Your complaint titled '{complaint_title}' was submitted on {complaint_date}.\n\n"
        f"Complaint Details:\n{complaint_description}\n\n"
        "Regards,\n\n"
        "Swift Campus Team"
        
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return True
    except Exception as e:
        logger.error("Error sending complaint confirmation email: %s", e)
        return False

def send_resolution_notification(user_email, complaint_title, complaint_date):
    """
    Notify the complaining user that their issue has been resolved.
    """
    subject = f"[SwiftCampus] Your complaint “{complaint_title}” has been resolved"
    body = (
        f"Hello,\n\n"
        f"Your complaint titled “{complaint_title}” submitted on "
        f"{complaint_date.strftime('%Y-%m-%d %H:%M')} has now been marked as RESOLVED.\n\n"
        "Thank you for your patience. If you have any further questions or concerns, "
        "please feel free to get in touch.\n\n"
        "Regards,\n\n"
        "Swift Campus Team"
    )
    
    try:
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [user_email],  fail_silently=False)
        logger.debug("Complaint confirmation email successfully sent to %s", user_email)
        return True
    except Exception:
        return False
        logger.error("Error sending complaint confirmation email: %s", e)