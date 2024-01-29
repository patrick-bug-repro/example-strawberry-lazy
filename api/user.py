import strawberry

from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from .post import Post


@strawberry.type
class User:
    id: strawberry.ID
    name: str
    age: int

    @strawberry.field
    def posts(self) -> list[Annotated["Post", strawberry.lazy(".post")]]:
        from .post import Post

        return [
            Post(
                id=strawberry.ID("1"),
                title="First post",
                content="Lorem ipsum",
                user_id=self.id,
            ),
            Post(
                id=strawberry.ID("2"),
                title="Second post",
                content="Lorem ipsum",
                user_id=self.id,
            ),
        ]
