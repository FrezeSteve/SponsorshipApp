from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404

from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Scholarship, Sponsor
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


# from .models import Scholarship


# Create your views here.
def index(request):
    return render(request, 'step.html')


# scholarship view
def scholarshipview(request):
    # form
    if request.method == "POST":  # pass
        field = request.POST.dict()
        username = field['uname']
        email = field['email']
        firstname = field['fname']
        lastname = field['lname']
        password = field['pwd']
        password2 = field['pwd2']
        # form validation
        if password != password2 or len(password) < 8 or len(username) < 1 \
                or '@' not in email or '.' not in email \
                or len(firstname) < 1 \
                or len(lastname) < 1:
            return HttpResponseRedirect(reverse('error'))
        # create user
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        # create a scholarship record
        contact1 = field['phno']
        contact2 = field['pwd2']
        school = field['school']
        address = field['address']
        level = field['level']
        year = field['year']
        reason = field['reason']
        birth = request.FILES['birth']
        naid = request.FILES['id']
        letter = request.FILES['rec']
        s = Scholarship.objects.create(
            user=user
        )
        s.contact1 = contact1
        s.contact2 = contact2
        s.birth = birth
        s.naid = naid
        s.letter = letter
        s.school = school
        s.address = address
        s.level = level
        s.year = year
        s.reason = reason
        s.save()
        return HttpResponseRedirect(reverse('success'))
    return HttpResponseNotFound('<h1>Wrong Request</h1>')


def success(request):
    return render(request, 'finish.html')


def error(request):
    return render(request, 'error.html')


@login_required
def list_scholarship(request):
    # Make sure that its a staff accessing this view
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse('login')+'?next='+request.path)
    qs = Scholarship.objects.filter(approved=False).all()
    return render(request, 'list.html', context={'qs': qs})


@login_required
def detail_scholarship(request, pk):
    # Make sure that its a staff accessing this view
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse('login') + '?next=' + request.path)
    object = get_object_or_404(Scholarship, pk=pk)
    return render(request, 'detail.html', context={'object': object})


@login_required
def approve(request, pk):
    if not request.user.is_staff:
        HttpResponseNotFound('<h1>Not Authorized</h1>')
    object = get_object_or_404(Scholarship, pk=pk)
    send_mail(
        'Approval for the scholarship',
        'You have been successfully approved',
        'from@example.com',
        [str(object.user.email)],
        fail_silently=True,
    )
    return HttpResponseRedirect(reverse_lazy('successfully'))


def successfully(request):
    return render(request, 'success.html')


@login_required
def list_scholarship_for_sponsors(request):
    # Make sure that its a sponsor accessing this view
    s = Sponsor.objects.filter(user=request.user).first()
    # get_object_or_404(Sponsor, user=request.user)
    if s is None:
        return HttpResponseRedirect(reverse('login') + '?next=' + request.path)
    qs = Scholarship.objects.filter(approved=True).filter(sponsored=False).all()
    return render(request, 'listsp.html', context={'qs': qs})


@login_required
def detail_scholarship_for_sponsors(request, pk):
    # Make sure that its a sponsor accessing this view
    s = Sponsor.objects.filter(user=request.user).first()
    # get_object_or_404(Sponsor, user=request.user)
    if s is None:
        return HttpResponseRedirect(reverse('login') + '?next=' + request.path)
    object = get_object_or_404(Scholarship, pk=pk)
    return render(request, 'detailsp.html', context={'object': object})


@login_required
def approvesp(request, pk):
    s = Sponsor.objects.filter(user=request.user).first()
    if s is None:
        HttpResponseNotFound('<h1>Not Authorized</h1>')
    object = get_object_or_404(Scholarship, pk=pk)
    message = ('You have been successfully sponsored. Name of Sponsor: {name}, email address: {email}'.format(
        name=s.user.username, email=s.user.email))
    send_mail(
        'Sponsorship',
        message,
        'from@example.com',
        [str(object.user.email)],
        fail_silently=True,
    )
    return HttpResponseRedirect(reverse_lazy('successfully'))


