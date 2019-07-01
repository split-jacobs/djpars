from django.shortcuts import render
from .models import Table

def table(request):
	data = Table.objects.all()
	return render (request, 'table/table.html', {'employ' : data })
	
'''
						
						employer = Table()
						
						employer.title = title
						employer.link = link
						employer.name = name
						employer.number = number
						employer.email = email
						employer.address = address
						employer.date_public = date_public
						employer.save()
					
				    
'''		
					
		

	
