from api.schema import schema
import rich

query = """
    query {
        user(id: "1") {
            name
            age
            posts {
                title
                content
                user {
                    id
                    name
                }
            }
        }
    }
"""

result = schema.execute_sync(query)


rich.print(result.data)
