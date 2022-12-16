from django.shortcuts import render, redirect
from APP.models import School


# Create School

def insert_sho(request):
    if request.method == "POST":
        SchoolId = request.POST['SchoolId']
        SchoolName = request.POST['SchoolName']
        SchoolAddress = request.POST['SchoolAddress']

        data = School(SchoolId=SchoolId,
                      SchoolName=SchoolName,
                      SchoolAddress=SchoolAddress)
        data.save()

        return redirect('show/')
    else:
        return render(request, 'insert.html')


# Retrive School

def show_sho(request):
    schools = School.objects.all()
    return render(request, 'show.html', {'schools': schools})


# Update School

def edit_sho(request, pk):
    schools = School.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('/show')

    context = {
        'schools': schools,
    }

    return render(request, 'edit.html', context)


# Delete School

def remove_sho(request, pk):
    schools = School.objects.get(id=pk)

    if request.method == 'POST':
        schools.delete()
        return redirect('/show')

    context = {
        'schools': schools,
    }

    return render(request, 'delete.html', context)
