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

	"name": <USER INPUT>

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

