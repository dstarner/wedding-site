from django.shortcuts import render, redirect
from wedding.guests.models import Party
from .forms import PartyRSVPForm


def rsvp_index(request):
    if request.method.lower() == 'post':
        code = request.POST.get('code', '')
        if len(code) != 4:
            return render(request, 'index.html', {'msg': 'Invalid code provided', 'code': code})
        party = Party.objects.filter(code=code).first()
        print(code, party)
        if not party:
            return render(request, 'index.html', {'msg': 'Party not found', 'code': code})
        return redirect('rsvp-party', code=code)
    return render(request, 'index.html', {'code': ''})


def rsvp_party(request, code):
    party = Party.objects.filter(code=code).first()
    if not party:
        return redirect('/')

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PartyRSVPForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            pass

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PartyRSVPForm()
    return render(request, 'rsvp.html', {'party': party, 'form': form})