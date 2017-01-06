from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import xlwt

from bizzfuzz_app.models.user import User


class UserList(ListView):
    model = User


class UserCreate(CreateView):
    model = User
    success_url = reverse_lazy('user_list')
    fields = ['name', 'birthday', 'number']


class UserUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('user_list')
    fields = ['name', 'birthday', 'number']


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    users = User.objects.all()
    for user in users:
        col_num = 0
        row_num += 1

        ws.write(row_num, col_num, user.name, font_style)
        col_num += 1

        ws.write(row_num, col_num, user.birthday.strftime('%m/%d/%Y'), font_style)
        col_num += 1

        ws.write(row_num, col_num, user.get_eligibility(), font_style)
        col_num += 1

        ws.write(row_num, col_num, user.number, font_style)
        col_num += 1

        ws.write(row_num, col_num, user.get_bizzfuzz(), font_style)

    wb.save(response)
    return response
