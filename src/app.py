from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp
from .graph import schema
from .routers import user


app = FastAPI()

app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=schema.Query, mutation=schema.Mutation)))

app.include_router(user.router)



