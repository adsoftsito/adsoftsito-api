import graphene
from graphene_django import DjangoObjectType
from .models import Record
from .models import Profile
from users.schema import UserType
from django.db.models import Q

class RecordType(DjangoObjectType):
    class Meta:
        model = Record

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class Query(graphene.ObjectType):
    records = graphene.List(RecordType, search=graphene.String())
    profile = graphene.Field(ProfileType)

    def resolve_records(self, info, search=None, **kwargs):
        user = info.context.user 
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)

        if (search=="*"):
            filter = (
                Q(posted_by=user)
            )

            return Record.objects.filter(filter)[:10]
        else:
            filter = (
                Q(posted_by=user)
            )
            return Record.objects.filter(filter)

    def resolve_profile(self, info, **kwargs):
        user = info.context.user 
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)

        filter = (
            Q(posted_by=user)
        )
        return Profile.objects.filter(filter).first()



           
           


class CreateRecord(graphene.Mutation):
    id = graphene.Int()
    talla = graphene.Int()
    peso  = graphene.Float()
    cintura = graphene.Int()
    cadera = graphene.Int()
    actfisica = graphene.Int()
    actfisican = graphene.Int()
    bebidasugar = graphene.Int()
    bebidasugarn = graphene.Int()

    posted_by = graphene.Field(UserType)


    #2
    class Arguments:
        talla = graphene.Int()
        peso  = graphene.Float()
        cintura = graphene.Int()
        cadera = graphene.Int()
        actfisica = graphene.Int()
        actfisican = graphene.Int()
        bebidasugar = graphene.Int()
        bebidasugarn = graphene.Int()

    #3
    def mutate(self, info, talla, peso, cintura, cadera, actfisica, actfisican, bebidasugar, bebidasugarn):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')


        record = Record(
            talla=talla, 
            peso=peso, 
            cintura=cintura, 
            cadera=cadera, 
            actfisica=actfisica, 
            actfisican=actfisican, 
            bebidasugar=bebidasugar, 
            bebidasugarn=bebidasugarn,
            posted_by=user
        )

   
        record.save()
       
        return CreateRecord(
            id=record.id,
            talla=record.talla, 
            peso=record.peso, 
            cintura=record.cintura, 
            cadera=record.cadera, 
            actfisica=record.actfisica, 
            actfisican=record.actfisican, 
            bebidasugar=record.bebidasugar, 
            bebidasugarn=record.bebidasugarn,
            posted_by=record.posted_by

        )

class CreateProfile(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    apellido  = graphene.String()
    edad = graphene.Int()
    sexo = graphene.Int()
    email = graphene.String()
    diabetes = graphene.Int()
    diabetesp = graphene.Int()
    posted_by = graphene.Field(UserType)


    #2
    class Arguments:
        nombre = graphene.String()
        apellido  = graphene.String()
        edad = graphene.Int()
        sexo = graphene.Int()
        email = graphene.String()
        diabetes = graphene.Int()
        diabetesp = graphene.Int()


    #3
    def mutate(self, info, nombre, apellido, edad, sexo, email, diabetes, diabetesp):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        currentProfile = Profile.objects.filter(posted_by=user).first()

        profile = Profile(
            nombre=nombre, 
            apellido=apellido, 
            edad=edad, 
            sexo=sexo, 
            email=email, 
            diabetes=diabetes, 
            diabetesp=diabetesp, 
            posted_by=user
        )
        
        if currentProfile:
            profile.id = currentProfile.id
   
        profile.save()
       
        return CreateProfile(
            id=profile.id,
            nombre=profile.nombre, 
            apellido=profile.apellido, 
            edad=profile.edad, 
            sexo=profile.sexo, 
            email=profile.email, 
            diabetes=profile.diabetes, 
            diabetesp=profile.diabetesp, 
            posted_by=profile.posted_by

        )




class Mutation(graphene.ObjectType):
    create_record = CreateRecord.Field()
    create_profile = CreateProfile.Field()

