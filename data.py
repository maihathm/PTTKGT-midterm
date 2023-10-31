initialPheromoneLevel = (1)

graph = {
    'a': [{
        'name': 'b',
        'distance': 2,
        'pheromones': initialPheromoneLevel
    },
        {
            'name': 'd',
            'distance': 12,
            'pheromones': initialPheromoneLevel
        },
        {
            'name': 'e',
            'distance': 5,
            'pheromones': initialPheromoneLevel

        }],
    'b': [{
        'name': 'a',
        'distance': 2,
        'pheromones': initialPheromoneLevel
    },
        {
            'name': 'd',
            'distance': 8,
            'pheromones': initialPheromoneLevel
        },
        {
            'name': 'c',
            'distance': 4,
            'pheromones': initialPheromoneLevel
        }],
    'c': [{
        'name': 'd',
        'distance': 3,
        'pheromones': initialPheromoneLevel
    },
        {
            'name': 'e',
            'distance': 3,
            'pheromones': initialPheromoneLevel
        },
        {
            'name': 'b',
            'distance': 4,
            'pheromones': initialPheromoneLevel
        }],
    'd': [{
        'name': 'a',
        'distance': 12,
        'pheromones': initialPheromoneLevel
    },
        {
            'name': 'b',
            'distance': 8,
            'pheromones': initialPheromoneLevel
        },
        {
            'name': 'c',
            'distance': 3,
            'pheromones': initialPheromoneLevel
        },
        {
            'name': 'e',
            'distance': 10,
            'pheromones': initialPheromoneLevel
        }],
    'e': [{
        'name': 'a',
        'distance': 5,
        'pheromones': initialPheromoneLevel
    },
        {
            'name': 'c',
            'distance': 3,
            'pheromones': initialPheromoneLevel
        },
        {
            'name': 'd',
            'distance': 10,
            'pheromones': initialPheromoneLevel
        }],

}

graph15 = {
    "a": [
        {
            "name": "b",
            "distance": 4,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "c",
            "distance": 17,
            "pheromones": initialPheromoneLevel
        }],
    "b": [
        {
            "name": "a",
            "distance": 4,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "e",
            "distance": 2,
            "pheromones": initialPheromoneLevel
        }
    ],
    "c": [
        {
            "name": "a",
            "distance": 17,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "d",
            "distance": 3,
            "pheromones": initialPheromoneLevel
        }
    ],
    "d": [
        {
            "name": "c",
            "distance": 3,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "g",
            "distance": 2,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "j",
            "distance": 7,
            "pheromones": initialPheromoneLevel
        }
    ],
    "e": [
        {
            "name": "b",
            "distance": 2,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "f",
            "distance": 4,
            "pheromones": initialPheromoneLevel
        }
    ],
    "f": [
        {
            "name": "e",
            "distance": 4,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "g",
            "distance": 3,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "h",
            "distance": 14,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "i",
            "distance": 2,
            "pheromones": initialPheromoneLevel
        }

    ],
    "g": [
        {
            "name": "d",
            "distance": 2,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "f",
            "distance": 3,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "h",
            "distance": 7,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "j",
            "distance": 11,
            "pheromones": initialPheromoneLevel
        }
    ],
    "h": [
        {
            "name": "f",
            "distance": 14,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "g",
            "distance": 7,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "i",
            "distance": 2,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "o",
            "distance": 3,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "n",
            "distance": 7,
            "pheromones": initialPheromoneLevel
        }

    ],
    "i": [
        {
            "name": "h",
            "distance": 2,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "m",
            "distance": 4,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "l",
            "distance": 3,
            "pheromones": initialPheromoneLevel
        }
    ],

    "j": [
        {
            "name": "d",
            "distance": 7,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "g",
            "distance": 11,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "k",
            "distance": 8,
            "pheromones": initialPheromoneLevel
        }
    ],
    "k": [
        {
            "name": "j",
            "distance": 8,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "l",
            "distance": 7,
            "pheromones": initialPheromoneLevel
        }
    ],
    "l": [
        {
            "name": "k",
            "distance": 7,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "n",
            "distance": 2,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "i",
            "distance": 3,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "m",
            "distance": 4,
            "pheromones": initialPheromoneLevel
        }
    ],
    "m": [
        {
            "name": "i",
            "distance": 4,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "o",
            "distance": 6,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "l",
            "distance": 4,
            "pheromones": initialPheromoneLevel
        }
    ],
    "n": [
        {
            "name": "l",
            "distance": 2,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "o",
            "distance": 4,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "h",
            "distance": 7,
            "pheromones": initialPheromoneLevel
        }
    ],
    "o": [
        {
            "name": "m",
            "distance": 6,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "n",
            "distance": 4,
            "pheromones": initialPheromoneLevel
        },

        {
            "name": "h",
            "distance": 3,
            "pheromones": initialPheromoneLevel
        },
    ],
}

graphGR17 = {
    "633": [
        {
            "name": "257",
            "distance": 390,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 661,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 227,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 488,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 572,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 530,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 555,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 289,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 282,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 638,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 567,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 466,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 420,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 745,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 518,
            "pheromones": initialPheromoneLevel
        }
    ],
    "257": [
        {
            "name": "633",
            "distance": 390,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 228,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 169,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 112,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 196,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 154,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 372,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 262,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 110,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 437,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 191,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 74,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 53,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 472,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 142,
            "pheromones": initialPheromoneLevel
        }
    ],
    "91": [
        {
            "name": "633",
            "distance": 661,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 228,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 383,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 120,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 77,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 105,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 175,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 476,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 324,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 240,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 27,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 182,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 239,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 237,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 84,
            "pheromones": initialPheromoneLevel
        }
    ],
    "412": [
        {
            "name": "633",
            "distance": 227,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 169,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 383,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 267,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 351,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 309,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 338,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 196,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 61,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 421,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 346,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 243,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 199,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 528,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 297,
            "pheromones": initialPheromoneLevel
        }
    ],
    "150": [
        {
            "name": "633",
            "distance": 488,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 112,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 120,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 267,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 63,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 34,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 264,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 360,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 208,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 329,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 83,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 105,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 123,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 364,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 35,
            "pheromones": initialPheromoneLevel
        }
    ],
    "80": [
        {
            "name": "633",
            "distance": 572,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 196,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 77,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 351,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 63,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 29,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 232,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 444,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 292,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 297,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 47,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 150,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 207,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 332,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 29,
            "pheromones": initialPheromoneLevel
        }
    ],
    "134": [
        {
            "name": "633",
            "distance": 530,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 154,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 105,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 309,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 34,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 29,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 249,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 402,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 250,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 314,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 68,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 108,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 165,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 349,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 36,
            "pheromones": initialPheromoneLevel
        }
    ],
    "259": [
        {
            "name": "633",
            "distance": 555,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 372,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 175,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 338,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 264,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 232,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 249,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 495,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 352,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 95,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 189,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 326,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 383,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 202,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 236,
            "pheromones": initialPheromoneLevel
        }
    ],
    "505": [
        {
            "name": "633",
            "distance": 289,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 262,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 476,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 196,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 360,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 444,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 402,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 495,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 154,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 578,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 439,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 336,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 240,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 685,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 390,
            "pheromones": initialPheromoneLevel
        }
    ],
    "353": [
        {
            "name": "633",
            "distance": 282,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 110,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 324,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 61,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 208,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 292,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 250,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 352,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 154,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 435,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 287,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 184,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 140,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 542,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 238,
            "pheromones": initialPheromoneLevel
        }
    ],
    "324": [
        {
            "name": "633",
            "distance": 638,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 437,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 240,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 421,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 329,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 297,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 314,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 95,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 578,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 435,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 254,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 391,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 448,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 157,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 301,
            "pheromones": initialPheromoneLevel
        }
    ],
    "70": [
        {
            "name": "633",
            "distance": 567,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 191,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 27,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 346,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 83,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 47,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 68,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 189,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 439,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 287,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 254,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 145,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 202,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 289,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 55,
            "pheromones": initialPheromoneLevel
        }
    ],
    "211": [
        {
            "name": "633",
            "distance": 466,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 74,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 182,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 243,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 105,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 150,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 108,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 326,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 336,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 184,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 391,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 145,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 57,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 426,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 96,
            "pheromones": initialPheromoneLevel
        }
    ],
    "268": [
        {
            "name": "633",
            "distance": 420,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 53,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 239,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 199,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 123,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 207,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 165,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 383,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 240,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 140,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 448,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 202,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 57,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 483,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 153,
            "pheromones": initialPheromoneLevel
        }
    ],
    "246": [
        {
            "name": "633",
            "distance": 745,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 472,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 237,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 528,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 364,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 332,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 349,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 202,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 685,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 542,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 157,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 289,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 426,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 483,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "121",
            "distance": 336,
            "pheromones": initialPheromoneLevel
        }
    ],
    "121": [
        {
            "name": "633",
            "distance": 518,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "257",
            "distance": 142,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "91",
            "distance": 84,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "412",
            "distance": 297,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "150",
            "distance": 35,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "80",
            "distance": 29,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "134",
            "distance": 36,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "259",
            "distance": 236,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "505",
            "distance": 390,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "353",
            "distance": 238,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "324",
            "distance": 301,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "70",
            "distance": 55,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "211",
            "distance": 96,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "268",
            "distance": 153,
            "pheromones": initialPheromoneLevel
        },
        {
            "name": "246",
            "distance": 336,
            "pheromones": initialPheromoneLevel
        }
    ]
}
