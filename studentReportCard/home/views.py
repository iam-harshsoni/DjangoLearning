from django.shortcuts import render
from home.models import *
from django.core.paginator import Paginator
from django.db.models import *
from home.seed import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def get_students(request):
    """
    Retrieve and display a paginated list of students, with optional search functionality.
    This view handles the retrieval of student records from the database, optionally filtering
    the results based on a search query provided via the GET parameters. The results are then
    paginated and rendered in the 'report/students.html' template.
    Args:
        request (HttpRequest): The HTTP request object containing GET parameters for search and pagination.
    Returns:
        HttpResponse: The rendered HTML page displaying the list of students.
    GET Parameters:
        search (str, optional): A search term to filter students by name or department.
        page (int, optional): The page number for pagination.
    Query Explanation:
        The query uses Django's Q objects to perform a case-insensitive search on the 'student_name' 
        and 'department_department' fields. The Q objects allow for complex queries with OR conditions.
    """

    queryset = Student.objects.all()

    # Code for search feature
    if request.GET.get('search'):
        search = request.GET.get('search')
    
        queryset = queryset.filter(
            Q(student_name__icontains = search) | 
            Q(department__department__icontains = search)|
            Q(student_id__id__icontains = search) |
            Q(student_age__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_address__icontains = search))

    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'report/students.html', {'queryset' : page_obj })

def get_marks(request, student_id):

    queryset = Subject_marks.objects.filter(student__student_id__studentId=student_id)
    student_queryset = Student.objects.filter(student_id__studentId = student_id)
        
    total_marks = queryset.aggregate(total_marks = Sum("marks"))

    # ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','student_age')    
    
    # current_rank = -1
    # i=1

    # for rank in ranks:
    #     print(student_id)
    #     if student_id == rank.student_id.studentId:
    #         current_rank = i
    #         break
    #     i += 1
    # print(current_rank)
   
    return render(request,"report/marks.html",{'queryset' : queryset, 
                                               'student_queryset' : student_queryset,
                                                'total_marks' : total_marks})
                                                # 'current_rank' : current_rank})
