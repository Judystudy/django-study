from django.http import HttpResponse

from TestModel.models import Test

def testdb(request):
    response = ""
    response1 = ""

    list = Test.objects.all()

    response2 = Test.objects.filter(id=1)

    response3 = Test.objects.get(id=1)

    for var in list:
        response1 += var.name + ""
    response = response1
    # test1 = Test(name='runoob')
    # test1.save();
    return HttpResponse("<p>" + response + "</p>")

