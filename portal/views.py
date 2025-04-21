import re
from .forms import ComplaintForm
from django.shortcuts import render, redirect, get_object_or_404  
from django.contrib import messages  
from .models import Complaint, CustomUser
from datetime import datetime
from .utils import send_complaint_confirmation, send_resolution_notification

def home(request):
    items = Complaint.objects.all()
    return render(request, 'home.html', {'complaints': items})

def complaint(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        discription = request.POST.get('discription')
        faculty = request.POST.get('faculty')
        location = request.POST.get('location')
        image = request.FILES.get('image')
        pub_date = datetime.now()
        status = "Pending"

        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            messages.error(request, "❌ User not found. Please log in again.")
            return redirect('login')

        if Complaint.objects.filter(user=user, title=title, location=location).exists():
            messages.warning(request, "⚠️ You have already submitted a complaint with this title and location.")
            return render(request, 'complaint.html')

        Complaint.objects.create(
            user=user,
            user_email=user.email,
            title=title,
            discription=discription,
            faculty=faculty,
            location=location,
            image=image,
            pub_date=pub_date,
            status=status
        )

        email_sent = send_complaint_confirmation(
            user_email=user.email,
            complaint_title=title,
            complaint_description=discription,
            complaint_date=pub_date.strftime("%Y-%m-%d %H:%M")
        )
        if email_sent:
            messages.success(request, "✅ Your complaint has been submitted successfully. A confirmation email was sent.")
        else:
            messages.warning(request, "✅ Complaint submitted, but there was an issue sending the confirmation email.")

        return redirect('student_dashboard')

    return render(request, 'complaint.html')

def staff(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        messages.error(request, "❌ User not found. Please log in again.")
        return redirect('login')

    items = Complaint.objects.filter(faculty__iexact=user.department)
    return render(request, 'staff.html', {'complaints': items})

def resolve_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, complaint_id=complaint_id)

    if request.method == 'POST':
        was_resolved = (complaint.status == "Resolved")
        complaint.status = "Pending" if was_resolved else "Resolved"
        complaint.save()

        if complaint.status == "Resolved":
            sent = send_resolution_notification(
                user_email=complaint.user_email,
                complaint_title=complaint.title,
                complaint_date=complaint.pub_date,
            )
            if sent:
                messages.success(request, "✅ User has been notified of resolution.")
            else:
                messages.warning(request, "⚠️ Complaint resolved but notification failed.")

        return redirect('staff')

def withdraw_complaint(request, complaint_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        messages.error(request, "❌ User not found. Please log in again.")
        return redirect('login')

    try:
        complaint = Complaint.objects.get(complaint_id=complaint_id, user=user)
        complaint.delete()
        messages.success(request, "✅ Complaint withdrawn successfully.")
    except Complaint.DoesNotExist:
        messages.error(request, "⚠️ Complaint not found or you don't have permission to withdraw it.")

    return redirect('student_dashboard')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm_password', '')
        role = 'student'

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "❌ Username already taken.")
            return redirect('signup')

        if password != confirm:
            messages.error(request, "❌ Passwords do not match.")
            return redirect('signup')

        if len(password) < 8 or \
           not re.search(r'[A-Z]', password) or \
           not re.search(r'[a-z]', password) or \
           not re.search(r'\d', password) or \
           not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
            messages.error(request, "❌ Password must be at least 8 characters long and include uppercase, lowercase, number, and special character.")
            return redirect('signup')

        user = CustomUser(username=username, email=email, role=role)
        user.set_password(password)
        user.save()
        messages.success(request, "✅ Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'signup.html')

def student_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        messages.error(request, "❌ User not found or session expired.")
        return redirect('login')

    complaints = Complaint.objects.filter(user=user)
    return render(request, 'student_dashboard.html', {'complaints': complaints})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = CustomUser.objects.filter(username=username).first()
        if user and user.check_password(password):
            request.session['user_id'] = user.id
            if user.role == 'staff':
                return redirect('staff')
            elif user.role == 'student':
                return redirect('student_dashboard')
            else:
                return redirect('home')
        
        messages.error(request, "❌ Incorrect username or password.")
        return redirect('login')

    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    messages.success(request, "✅ You have been logged out.")
    return redirect('login')

def faq(request):
    user_role = None
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = CustomUser.objects.get(id=user_id)
            user_role = user.role
        except CustomUser.DoesNotExist:
            pass
    return render(request, 'faq.html', {'user_role': user_role})

def about(request):
    user_role = None
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = CustomUser.objects.get(id=user_id)
            user_role = user.role
        except CustomUser.DoesNotExist:
            pass
    return render(request, 'about.html', {'user_role': user_role})

def report_issue(request):
    user_role = None
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = CustomUser.objects.get(id=user_id)
            user_role = user.role
        except CustomUser.DoesNotExist:
            pass
    return render(request, 'report_issue.html', {'user_role': user_role})
