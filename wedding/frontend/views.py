from django.shortcuts import render, redirect
from wedding.guests.models import Party, Guest


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

    if request.method.lower() == 'post':
        accepts_str = request.POST.get('accepts', '0')
        try:
            accepts = int(accepts_str)
        except ValueError:
            return render(request, 'rsvp.html', {'party': party, 'msg': 'Could not parse number attending'})
        
        if accepts > party.guests_allowed:
            return render(request, 'rsvp.html', {
                'party': party,
                'msg': f'You are allowed a maximum of {party.guests_allowed} guests. Please contact us if you need more.'
            })
        
        party.attending = accepts
        party.save(update_fields=['attending'])

        Guest.objects.filter(id__in=party.guests.all()[party.attending:].values_list('id')).delete()

        if party.attending == 0:
            return redirect('decline', code=party.code)

        return redirect('rsvp-guests', code=party.code)
    return render(request, 'rsvp.html', {'party': party})


def rsvp_guests(request, code):
    party = Party.objects.filter(code=code).first()
    if not party:
        return redirect('/')
    
    if request.method.lower() == 'post':
        for idx in range(party.attending):
            try:
                details = {
                    'first_name': request.POST[f'first_{idx}'],
                    'last_name': request.POST[f'last_{idx}'],
                    'meal': request.POST[f'meal_{idx}'],
                    'requests': request.POST[f'requests_{idx}'],
                }
            except KeyError:
                return render(request, 'guests.html', {
                    'party': party,
                    'msg': f'Invalid data provided for guest #{idx + 1}.',
                    'msg_lvl': 'error'
                })
            
            guest = party.guests \
                         .filter(first_name__iexact=details['first_name'], last_name__iexact=details['last_name']) \
                         .first()
            if not guest:
                guest = Guest.objects.create(**details, party=party)
            else:
                guest.meal = details['meal']
                guest.requests = details['requests']
                guest.save(update_fields=['meal', 'requests'])

        return render(request, 'guests.html', {
            'party': party,
            'msg': f'Saved your RSVP! Feel free to redo this process with the same code if anything changes.',
            'msg_lvl': 'success'
        })
    return render(request, 'guests.html', {'party': party})


def decline(request, code):
    party = Party.objects.filter(code=code).first()
    if not party:
        return redirect('/')
    
    return render(request, 'decline.html', {'party': party})
