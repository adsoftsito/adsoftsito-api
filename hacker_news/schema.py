import graphene
import graphql_jwt

import links.schema
import users.schema
import innsalud.schema
import sales.schema
import emisor.schema
import receptor.schema
import cats.schema
import cat40.schema
import precios.schema
import proveedor.schema

class Query(innsalud.schema.Query, users.schema.Query, links.schema.Query, sales.schema.Query, emisor.schema.Query, receptor.schema.Query, cats.schema.Query, cat40.schema.Query, precios.schema.Query, proveedor.schema.Query, graphene.ObjectType):
    pass

class Mutation(innsalud.schema.Mutation, users.schema.Mutation, links.schema.Mutation, sales.schema.Mutation, emisor.schema.Mutation, receptor.schema.Mutation, proveedor.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)
