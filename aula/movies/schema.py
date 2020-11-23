import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from aula.movies.models import Alumno, Materia, Asignacion_Materia

# Create a GraphQL type for the Alumno model
class AlumnoType(DjangoObjectType):
    class Meta:
        model = Alumno

# Create a GraphQL type for the Materia model
class MateriaType(DjangoObjectType):
    class Meta:
        model = Materia

# Create a GraphQL type for the movie model
class Asignacion_MateriaType(DjangoObjectType):
    class Meta:
        model = Asignacion_Materia

# Create a Query type
class Query(ObjectType):
    alumno = graphene.Field(AlumnoType, id=graphene.Int())
    materia = graphene.Field(MateriaType, id=graphene.Int())
    asiignacion = graphene.Field(Asignacion_MateriaType, id=graphene.Int())
    alumnos = graphene.List(AlumnoType)
    materias= graphene.List(MateriaType)
    asignaciones= graphene.List(Asignacion_MateriaType)

    def resolve_alumno(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Alumno.objects.get(pk=id)

        return None

    def resolve_materia(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Materia.objects.get(pk=id)

        return None

    def resolve_asignacion(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Asignacion_Materia.objects.get(pk=id)

        return None
 

    def resolve_alumnos(self, info, **kwargs):
        return Alumno.objects.all()

    def resolve_materias(self, info, **kwargs):
        return Materia.objects.all()  

    def resolve_asignaciones(self, info, **kwargs):
        return Asignacion_Materia.objects.all()   

    
    # Create Input Object Types
class AlumnoInput(graphene.InputObjectType):
    id = graphene.ID() 
    Codigo = graphene.String()
    Nombre =  graphene.String()
    Apellido = graphene.String()
    Email = graphene.String()
    Grado = graphene.String()
    Seccion = graphene.String()
    Genero = graphene.String()
    nacimiento = graphene.String()
    direccion = graphene.String()
    telefono = graphene.String()
    fechaingreso = graphene.String()

class MateriaInput(graphene.InputObjectType):
    id = graphene.ID()
    Nombre_Materia  = graphene.String()
    Fecha_Ingreso = graphene.String()

class AsignacionInput(graphene.InputObjectType):
    id = graphene.ID()
    Nota_Final = graphene.String()
    Alumno  = graphene.List(AlumnoInput)
    Materia  = graphene.List(MateriaInput)

# Create mutations for Alumnos
class CreateAlumno(graphene.Mutation):
    class Arguments:
        input = AlumnoInput(required=True)

    ok = graphene.Boolean()
    alumno = graphene.Field(AlumnoType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        alumno_instance = Alumno(Codigo=input.Codigo,Nombre=input.Nombre,Apellido=input.Apellido,Email=input.Email,Grado=input.Grado,Seccion=input.Seccion,Genero=input.Genero,nacimiento=input.nacimiento,direccion=input.direccion,telefono=input.telefono)
        alumno_instance.save()
        return CreateAlumno(ok=ok, alumno=alumno_instance)

class UpdateAlumno(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AlumnoInput(required=True)

    ok = graphene.Boolean()
    alumno = graphene.Field(AlumnoType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        alumno_instance = Alumno.objects.get(pk=id)
        if alumno_instance:
            ok = True
            alumno_instance.Codigo = input.Codigo
            alumno_instance.Nombre = input.Nombre
            alumno_instance.Apellido = input.Apellido
            alumno_instance.Email = input.Email
            alumno_instance.Grado = input.Grado
            alumno_instance.Seccion = input.Seccion
            alumno_instance.Genero = input.Genero
            alumno_instance.nacimiento = input.nacimiento
            alumno_instance.direccion = input.direccion
            alumno_instance.telefono = input.telefono
            alumno_instance.save()
            return UpdateAlumno(ok=ok, alumno=alumno_instance)
        return UpdateAlumno(ok=ok, alumno=None)



# Create mutations for materias
class CreateMateria(graphene.Mutation):
    class Arguments:
        input = MateriaInput(required=True)

    ok = graphene.Boolean()
    materia = graphene.Field(MateriaType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        materia_instance = Materia(Nombre_Materia =input.Nombre_Materia )
        materia_instance.save()
        return CreateMateria(ok=ok, materia=materia_instance)

class UpdateMateria(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = MateriaInput(required=True)

    ok = graphene.Boolean()
    materia = graphene.Field(MateriaType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        materia_instance = Materia.objects.get(pk=id)
        if materia_instance:
            ok = True
            materia_instance.Nombre_Materia = input.Nombre_Materia
            materia_instance.save()
            return UpdateMateria(ok=ok, materia=materia_instance)
        return UpdateMateria(ok=ok, materia=None)



# Create mutations for asignacion
class CreateAsignacion(graphene.Mutation):
    class Arguments:
        input = AsignacionInput(required=True)

    ok = graphene.Boolean()
    asignacion = graphene.Field(Asignacion_MateriaType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        asignacion_instance = Asignacion_Materia(Nota_Final=input.Nota_Final)
        alumnos = []
        materias = []
        for alumno_input in input.Alumno:
          alumno = Alumno.objects.get(pk=alumno_input.id)
          if alumno is None:
            return CreateAsignacion(ok=False, asignacion=None)
          alumnos.append(alumno)
        asignacion_instance.alumnos.set(alumnos)
        for materia_input in input.Materia:
          materia = Materia.objects.get(pk=materia_input.id)
          if materia is None:
            return CreateAsignacion(ok=False, asignacion=None)
          materias.append(materia)
        asignacion_instance.save()
        asignacion_instance.materias.set(materias)
        return CreateAsignacion(ok=ok, asignacion=asignacion_instance)





class UpdateAsignacion(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AsignacionInput(required=True)

    ok = graphene.Boolean()
    asignacion = graphene.Field(Asignacion_MateriaType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        asignacion_instance = Asignacion.objects.get(pk=id)
        if movie_instance:
            ok = True
            alumnos = []
            materias = []
            for alumno_input in input.alumnos:
              alumno = Alumno.objects.get(pk=alumno_input.id)
              if alumno is None:
                return UpdateAsignacion(ok=False, asignacion=None)
              alumnos.append(alumno)
            asignacion_instance.save()
            asignacion_instance.alumnos.set(alumnos)
            return UpdateAsignacion(ok=ok, asignacion=asignacion_instance)
            
            for materia_input in input.materias:
              materia = Materia.objects.get(pk=materia_input.id)
              if materia is None:
                return UpdateAsignacion(ok=False, movie=None)
              materias.append(materia)
            
            asignacion_instance.Nota_Final = input.Nota_Final
            asignacion_instance.save()
            asignacion_instance.materias.set(materias)
            return UpdateAsignacion(ok=ok, asignacion=asignacion_instance)
        return UpdateAsignacion(ok=ok, asignacion=None)


class Mutation(graphene.ObjectType):
    create_alumno = CreateAlumno.Field()
    update_alumno= UpdateAlumno.Field()
    create_materia = CreateMateria.Field()
    update_materia = UpdateMateria.Field()
    create_asignacion = CreateAsignacion.Field()
    update_asignacion = UpdateAsignacion.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)