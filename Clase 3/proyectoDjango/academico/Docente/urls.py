from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import DocenteList, DocenteCreate, DocenteUpdate , DocenteDelete
from django.urls import path, include


urlpatterns = [
    path('listar/', DocenteList.as_view(), name="docentes_list"),
    # localhost:8000/Docente/crear
    path('crear/', DocenteCreate.as_view(), name="docentes_form"),
    path('editar/<int:pk>', DocenteUpdate.as_view(), name="docentes_update"),
    path('borrar/<int:pk>', DocenteDelete.as_view(), name="docentes_borrar"),
    
]
