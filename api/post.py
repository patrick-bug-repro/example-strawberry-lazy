import strawberry

from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from .user import User


@strawberry.type
class Post:
    id: strawberry.ID
    title: str
    content: str
    user_id: strawberry.Private[strawberry.ID]

    @strawberry.field
    def user(self) -> Annotated["User", strawberry.lazy(".user")]:
        from .user import User

        return User(id=self.user_id, name="Patrick", age=10)
