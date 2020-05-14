# backend-twitch

## Get all channels

<strong> Get </strong> /channels/


Response

{

    "success": true,

    "data": [

        {

            "id": 1,

            "name": "Ninja",

            "videos": [ <SERIALIZED ASSIGNMENT WITHOUT CHANNEL FIELD>, ... ],

            "subscribers": [ <SERIALIZED USER WITHOUT CHANNEL FIELD>, ... ],


            "supporters": [ <SERIALIZED USER WITHOUT CHANNEL FIELD>, ... ]

        },

        {
            "id": 2,

            "name": "Pokimane",

            "videos": [ <SERIALIZED ASSIGNMENT WITHOUT CHANNEL FIELD>, ... ],

            "subscribers": [ <SERIALIZED USER WITHOUT CHANNEL FIELD>, ... ],

            "supporters": [ <SERIALIZED USER WITHOUT CHANNEL FIELD>, ... ]

        }

        ...

    ]

}




## Create a channel

<strong> Post </strong> /channels/

Request

{

	"name": <USER INPUT FOR NAME>

}

Response

{

    "success": true,

    "data": {

        "id": <ID>,

        "name": <USER INPUT FOR NAME>,

        "videos": [],

        "subscribers": [],

        "supporters": []

    }

}




## Get a specific channel

<strong> Get </strong> /channels/{id}

Response

{

    "success": true,

    "data": { 
           
        "id": <ID>,

            "name": <USER INPUT FOR NAME>,

            "videos": [ <SERIALIZED ASSIGNMENT WITHOUT CHANNEL FIELD>, ... ],

            "subscribers": [ <SERIALIZED USER WITHOUT CHANNEL FIELD>, ... ],


            "supporters": [ <SERIALIZED USER WITHOUT CHANNEL FIELD>, ... ]

    }
}


## Delete a specific channel

<strong> Delete </strong> /channels/{id}

Response

{

    "success": true,

    "data": { 
           
        "id": <ID>,

            "name": <USER INPUT FOR NAME>,

            "videos": [ <SERIALIZED ASSIGNMENT WITHOUT CHANNEL FIELD>, ... ],

            "subscribers": [ <SERIALIZED USER WITHOUT CHANNEL FIELD>, ... ],


            "supporters": [ <SERIALIZED USER WITHOUT CHANNEL FIELD>, ... ]

    }
}

## Create a user

<strong> Post </strong> /users/


Request


{

	"name": <USER INPUT FOR NAME>,

	"tag": <USER INPUT FOR TAG>

}

Response

{

    "success": true,

    "data": {

        "id": <ID>,

        "name": <USER INPUT FOR NAME>,

        "tag": <USER INPUT FOR TAG>,

        "channels": []
    }
}

## Add a user to a channel

<Strong> Post </Strong> /channel/{id}/add/

Request

{

    "user_id": <USER INPUT>,

    "type": "subscriber" or "supporter"

}

## Add a video to a channel

<Strong> Post </Strong> /channel/{id}/video/

Request

{

    "title": <USER INPUT>

}

Response

{
    "success": true,

    "data": {

        "id": <ID>,

        "title": <USER INPUT FOR TITLE>

        "upload_time": <TIME OF INPUT>,

        "channels": {

            "id": 1,

            "name": "Ninja"

        }

    }

}