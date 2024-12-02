import graphene
import myapp.schema

class Query(myapp.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
