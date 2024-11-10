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
            actfisican=actfisica, 
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
            actfisican=record.actfisica, 
            bebidasugar=record.bebidasugar, 
            bebidasugarn=record.bebidasugarn,
            posted_by=record.posted_by

        )


class Mutation(graphene.ObjectType):
    create_record = CreateRecord.Field()

