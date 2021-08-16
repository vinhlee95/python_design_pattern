# Single Responsibility Principle

> A class should have one and only one reason to change, meaning that a class should have only one job.

The more responsibilities a class has, the more change requests it will get, and the harder those changes will be to implement.

**Easy example**

```python
# Following User class has 2 main responsibilities
# 1. To get_name
# 2. To save an user object to DB
# 🚧 This is an anti-SRP pattern
class  User:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, user: User):
        pass
```

To conform SRP pattern:

```python
# This User class only has 1 responsibility - to extract data from 
# an user object
class  User:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

# To handle DB CRUD, let's have a new class
class UserDB:
		def save(self, user: User) -> User:
				pass
```

**Real-life example**

Anti-pattern:

```python
class Survery_Stats(APIView):
def post(self, request):
  # Auth
  if request.data.user is None:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # Validation
  if request.data.get("answer1",None) is None:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  # Business Logic    
  survey = Survey.objects.create(answer1=request.data.get("answer1"))
    serializer = surveys_serializers.Survey_Stats(data=survey, many=False)
    # External Services
    email = Email("localhost", "New survey", survey.email)
    email.send()
    
  # Serialization
  return Response(serializer.data, status=status.HTTP_201_CREATED)
```

With SRP:

```python
class Survery_Stats(APIView):
  # Auth
  permission = (IsAuthenticaded)
  
  def post(self, request):
		# Validation
		validate_survey(request.data)
	
		# Business Logic    
		survey_services.create(request.data)
			
		# Serialization
		return Response(serializer.data, status=status.HTTP_201_CREATED)
```

# Resources

[Solid principles in Python and Django](https://www.designmycodes.com/examples/solid-principles-python-django.html)

[SOLID Principles made easy | Hacker Noon](https://hackernoon.com/solid-principles-made-easy-67b1246bcdf)