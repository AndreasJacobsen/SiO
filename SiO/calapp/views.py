from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.views.generic import DeleteView, UpdateView, CreateView, ListView

from datetime import datetime

from SiO.CoAdmin.models import Event
# from SiO.member.models import Association
# from SiO.calapp.forms import CalForm


# def calendar(request):
#     return render(request, 'calapp/calendar.html', {})

class calendar(ListView):

    model = Event
    # form_class = RegForm
    template_name = 'calapp/calendar.html'

    # def get_queryset(self):
    #     queryset = Event.objects.filter(association=self.request.user.association)
    #     return queryset


def event_get(request, start, end):
    res = {'success': False}
    try:
        datetime.strptime(start, '%Y-%m-%dT%H:%M:%S.%fZ')
        datetime.strptime(end, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        res['message'] = \
            'Invalid params: ISO format start end dates expected'
        return JsonResponse(res)
    result = Event.objects.filter(start__range=(start,
                                                end)).order_by('start').values()

    res['data'] = list(result)
    res['success'] = True
    return JsonResponse(res)


def paramMissing(POST, param, res):
    if param not in POST:
        res['message'] = param + ' param missing'
        return True
    return False


def event_delete(request):
    if request.method == 'POST':
        res = {'success': False}

        if paramMissing(request.POST, 'eid', res):
            return JsonResponse(res)

        eid = request.POST['eid']
        Event.objects.filter(id=eid).delete()

        res['success'] = True
        res['message'] = 'deleted'
        res['eid'] = eid
        return JsonResponse(res)
    else:
        raise Http404


def event_add_edit(request):
    if request.method == 'POST':
        # form = CalForm(request.user, request.POST)
        res = {'success': False}

        if paramMissing(request.POST, 'name', res) \
                or paramMissing(request.POST, 'location', res) \
                or paramMissing(request.POST, 'start', res) \
                or paramMissing(request.POST, 'end', res) \
                or paramMissing(request.POST, 'allday', res) \
                or paramMissing(request.POST, 'description', res) \
                or paramMissing(request.POST, 'action', res) \
                or paramMissing(request.POST, 'synced', res):
            return JsonResponse(res)

        gid = request.POST.get('gid', '')
        # asoc_pk = form.cleaned_data.get('association')
        # asoc = Association.objects.get(id=asoc_pk.pk)
        # or paramMissing(request.POST, 'association', res) \ som ska være ovenfor

        action = request.POST['action']
        name = request.POST['name']
        location = request.POST['location']
        start = request.POST['start']
        end = request.POST['end']
        allday = request.POST['allday'] == 'true'
        description = request.POST['description']
        synced = request.POST['synced'] == 'true'
        # association_pk = Association.objects.filter(asoc_name=request.user.association)
        # asoc_pk = Association.objects.get(id=association_pk.pk)
        # asoc_pk = form.request.POST['association']
        # asoc_pk = form.cleaned_data.get('association')
        # asoc = Association.objects.get(id=asoc_pk.pk)

        if action == 'add':
            Event.objects.create(
                name=name,
                location=location,
                start=start,
                end=end,
                allday=allday,
                description=description,
                synced=synced,
                gid=gid,
                # association=asoc
            )

            res['success'] = True
            res['message'] = 'added'
            eid = Event.objects.latest('id').id
            res['eid'] = eid
            res['data'] = Event.objects.values().get(id=eid)
        elif action == 'edit':

            if paramMissing(request.POST, 'eid', res):
                return JsonResponse(res)

            eid = request.POST['eid']
            event = Event.objects.get(id=eid)
            event.name = name
            event.location = location
            event.start = start
            event.end = end
            event.allday = allday
            event.description = description
            event.synced = synced
            event.save()

            res['success'] = True
            res['message'] = 'edited'
            res['eid'] = eid
            res['data'] = Event.objects.values().get(id=eid)

        return JsonResponse(res)
    else:
        raise Http404


def event_setsync(request):
    if request.method == 'POST':
        res = {'success': False}

        if paramMissing(request.POST, 'eid', res) \
                or paramMissing(request.POST, 'gid', res):
            return JsonResponse(res)

        eid = request.POST['eid']
        gid = request.POST['gid']

        event = Event.objects.get(id=eid)
        event.synced = True
        event.gid = gid
        event.save()

        res['success'] = True
        res['message'] = 'sync set'
        res['eid'] = eid
        res['gid'] = gid
        return JsonResponse(res)
    else:
        raise Http404




















# from calendar import monthrange
# from sched import Event
# #
# from django.shortcuts import render, render_to_response
# # from django.template import RequestContext
# from django.utils.datetime_safe import datetime, date
#
#
# def named_month(month_number):
#     """
#     Return the name of the month, given the number.
#     """
#     return date(1900, month_number, 1).strftime("%B")
#
#
# def this_month(request):
#     """
#     Show calendar of calapp this month.
#     """
#     today = datetime.now()
#     return events(request, today.year, today.month)
#
#
# def events(request, year, month, series_id=None):
#     """
#     Show calendar of calapp for a given month of a given year.
#     ``series_id``
#     The event series to show. None shows all event series.
#
#     """
#
#     my_year = int(year)
#     my_month = int(month)
#     my_calendar_from_month = datetime(my_year, my_month, 1)
#     my_calendar_to_month = datetime(my_year, my_month, monthrange(my_year, my_month)[1])
#
#     my_events = Event.objects.filter(date_and_time__gte=my_calendar_from_month).filter(date_and_time__lte=my_calendar_to_month)
#     if series_id:
#         my_events = my_events.filter(series=series_id)
#
#     # Calculate values for the calendar controls. 1-indexed (Jan = 1)
#     my_previous_year = my_year
#     my_previous_month = my_month - 1
#     if my_previous_month == 0:
#         my_previous_year = my_year - 1
#         my_previous_month = 12
#     my_next_year = my_year
#     my_next_month = my_month + 1
#     if my_next_month == 13:
#         my_next_year = my_year + 1
#         my_next_month = 1
#     my_year_after_this = my_year + 1
#     my_year_before_this = my_year - 1
#     return render(request, 'calapp/events.html', {'events_list': my_events,
#                                                   'month': my_month,
#                                                   'month_name': named_month(my_month),
#                                                   'year': my_year,
#                                                   'previous_month': my_previous_month,
#                                                   'previous_month_name': named_month(my_previous_month),
#                                                   'previous_year': my_previous_year,
#                                                   'next_month': my_next_month,
#                                                   'next_month_name': named_month(my_next_month),
#                                                   'next_year': my_next_year,
#                                                   'year_before_this': my_year_before_this,
#                                                   'year_after_this': my_year_after_this})
# # , context_instance=RequestContext(request))
