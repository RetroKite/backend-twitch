# backend-twitch

## Get all channels

<strong> Get </strong> /channels/

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