# Django Rest Framework

## ViewSets

Rest Framework provides built-in class for creating a set of typically used view methods:

- list
- create
- retrieve
- update
- partial
- destroy

Instead of manually registering views in a viewset in the urlconf, you can automatically assign url to the views by registering the viewset with a router class and then including `router.url` to the desired path inside `urlpatterns` list.

- [ViewSets Document](https://www.django-rest-framework.org/api-guide/viewsets/)
