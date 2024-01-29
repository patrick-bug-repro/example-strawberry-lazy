import strawberry

from .user import User


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: strawberry.ID) -> User:
        return User(id=id, name="Patrick", age=10)


schema = strawberry.Schema(query=Query)
