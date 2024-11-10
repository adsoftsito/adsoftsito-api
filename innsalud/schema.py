import graphene
from graphene_django import DjangoObjectType
from .models import Record
from users.schema import UserType
from django.db.models import Q
#from cat40.models import ClaveUnidad, ClaveProdServ

class RecordType(DjangoObjectType):
    class Meta:
        model = Record



class Query(graphene.ObjectType):
    records = graphene.List(RecordType, search=graphene.String())

    def resolve_records(self, info, search=None, **kwargs):
        user = info.context.user 
        #if user.is_anonymous:
        #    raise Exception('Not logged in!')

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

           


class CreateRecord(graphene.Mutation):
    id = graphene.Int()
    description = graphene.String()
    posted_by = graphene.Field(UserType)


    #2
    class Arguments:
        idlinea = graphene.Int()
        description = graphene.String()

    #3
    def mutate(self, info, idlinea, description):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')


        currentLinea = Record.objects.filter(id=idlinea).first()
        linea = Linea(
            description=description,
            posted_by = user
            )

        if currentLinea:
            linea.id = idlinea
   
        linea.save()
       
        return CreateRecord(
            id=linea.id,
            description=linea.description,
            posted_by=linea.posted_by
        )


class Mutation(graphene.ObjectType):
    create_record = CreateRecord.Field()

