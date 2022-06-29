# Balance game
balance game rest api

Build with django and django rest framework

[api design guidelines](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9)

Api Examples

#### [api paths](#Paths)
#### [games request and response example](#games-request-body-and-response-example)
#### [users request and response example](#)

### Paths
```
games/
games/<int:game_id>

users/signup/
users/signin/
users/signout/
```

### ```games/``` request body and response example

GET
```json
// games/  

{
    "games": [
        {
            "id": 9,
            "title": "Cpt.America vs IronMan",
            "choices": [
                {
                    "id": 1,
                    "text": "Cpt.America",
                    "votes": 0
                },
                {
                    "id": 2,
                    "text": "IronMan",
                    "votes": 0
                }
            ]
        },
        {
            "id": 10,
            "title": "woooo",
            "choices": [
                {
                    "id": 3,
                    "text": "fuuuuu",
                    "votes": 0
                },
                {
                    "id": 4,
                    "text": "barrr",
                    "votes": 0
                }
            ]
        }
    ]
}

// games/<int:game_id>/

{
    "id": 10,
    "title": "woooo",
    "choices": [
        {
            "id": 3,
            "text": "fuuuuu",
            "votes": 0
        },
        {
            "id": 4,
            "text": "barrr",
            "votes": 0
        }
    ]
}
```

POST
```json
// games/
// request body

{
    "title": "fooooo vs barrrrrr",
    "choices": [
        {
            "text": "buuuuu"
        },

        {
            "text": "barrrrrr"
        }
    ]
}
```

```json
// response body
{
    "status": 201,
    "description": "new game is successfully created.",
    "game": {
        "id": 18,
        "title": "fooooo vs barrrrrr",
        "choices": [
            {
                "id": 19,
                "text": "buuuuu",
                "votes": 0
            },
            {
                "id": 20,
                "text": "barrrrrr",
                "votes": 0
            }
        ]
    }
}
```

PUT
```json
// games/<int:game_id>/
// reqeuest body

{
    "title": "woooo",

    "choices": [
        {"text": "fuuuuu"},
        {"text": "barrr"}
    ]
}
```

```json
// response body

{
    "status": "200",
    "description": "game is updated",
    "game": {
        "id": 10,
        "title": "woooo",
        "choices": [
            {
                "id": 3,
                "text": "fuuuuu",
                "votes": 0
            },
            {
                "id": 4,
                "text": "barrr",
                "votes": 0
            }
        ]
    }
}
```

DELETE
```json
// games/<int:game_id>/
// response body
{
    "deleted_game_id": 18,
    "deleted_game_title": "fooooo vs barrrrrr",
    "description": "game is successfully deleted"
}
```

### ```users/``` request body and response example

### sign up
method: POST

```json
// request body
{
    "id": "foo",
    "password": "bar"
}
```

```json
// response body
{
    "Token": "<tooooooooooooooooooooooooookeeeeeeeeeeen>"
}
```

### sign in
method: POST
```json
// request body
{
    "id": "foo",
    "password": "bar"
}
```

```json
// response body
{
    "Token": "<tooooooooooooooooooooooooookeeeeeeeeeeen>"
}
```

### sign out
send request with header that contains token

response HTTP code 204 No content
