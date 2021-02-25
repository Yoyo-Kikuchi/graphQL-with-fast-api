import graphene
from .serializers import UserInfoModel, UserModel, UserCreateModel



class Query(graphene.ObjectType):
    get_user = graphene.Field(graphene.List(UserInfoModel), id=graphene.NonNull(graphene.Int))

    @staticmethod
    def resolve_get_user(parent, info, id):
        return[
            UserModel(
                id=1,
                user_name='t-yamada',
                first_name='taro',
                last_name='yamada'
            )
        ]


class CreateUser(graphene.Mutation):
    class Arguments:
        new_user = UserCreateModel()

    Output = UserInfoModel

    @staticmethod
    def mutate(parent, info, new_user):
        print(new_user)

        return UserModel(
                id=1,
                user_name='k-yamada',
                first_name='kenji',
                last_name='yamada'
            )

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()