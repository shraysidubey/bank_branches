from django.shortcuts import render
from bank.models import Branch
from django.http import JsonResponse, HttpResponse
from django.db.models import Q


def possible_matches(request):
    try:
        branch_string = request.GET.get('q','')
        branch_string = branch_string.upper()
        limit = request.GET.get('limit', '10')
        offset = request.GET.get('offset', '0')

        branches_queryset = Branch.objects.filter(branch__contains=branch_string).order_by('ifsc')[int(offset):int(offset)+int(limit)]
        data = list(branches_queryset.values())
        branch_dic = {"branches":data}

        return JsonResponse(branch_dic, safe=False)
    except:
        return HttpResponse(status=500)


def all_possible_matches(request):

    try:

        search_string = request.GET.get('q','')
        search_string = search_string.upper()
        limit = request.GET.get('limit', '10')
        offset = request.GET.get('offset', '0')
        print search_string
        print limit
        print offset

        branches_queryset = Branch.objects.filter(Q(ifsc=search_string) | Q(branch=search_string)
                        | Q(address=search_string) | Q(city=search_string) | Q(district=search_string)|
                        Q(state=search_string)).order_by('ifsc')[int(offset):int(offset)+int(limit)]
        #print branches_queryset
        data = list(branches_queryset.values())
        #print data

        branch_dic = {"branches": data}


        return JsonResponse(branch_dic, safe=False)
    except:

        return HttpResponse(status=500)