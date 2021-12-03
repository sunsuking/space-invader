HELP_CONTEXT = [
    {
        'name': 'SHOOT',
        'key': 'SPACE'
    },
    {
        'name': 'MOVE LEFT',
        'key': 'LEFT'
    },
    {
        'name': 'MOVE RIGHT',
        'key': 'RIGHT'
    },
    {
        'name': 'MOVE DOWN',
        'key': 'DOWN'
    },
    {
        'name': 'MOVE UP',
        'key': 'UP'
    }
]

SETTING_CONTEXT = [
    {
        'name': 'MOVE LEFT (PRESS KEY TO CHANGE)',
        'key': 'A'
    },
    {
        'name': 'MOVE RIGHT (PRESS KEY TO CHANGE)',
        'key': 'D'
    },
    {
        'name': 'SPEED (PRESS X OR Z TO CHANGE)',
        'key': '|'
    },
    {
        'name': 'VOLUME (PRESS X OR Z TO CHANGE)',
        'key': '|'
    },
    {
        'name': 'MUTE AUDIO',
        'key': 'M'
    }
]

LOADING_CONTEXT = [
    {
        'text': 'PLAY',
        'action': 'game'
    },
    {
        'text': 'SCORES',
        'action': 'explain'
    },
    {
        'text': 'SUMMARY',
        'action': 'summary'
    },
    {
        'text': 'SETTING',
        'action': 'setting'
    },
    {
        'text': 'Help',
        'action': 'help',
    },
]

EXPLAIN_CONTEXT = {
    'begin': [
        {
            'stage': 1,
            'text': [
                '000 대..원... ㄷ...어..라...',
                '현ㅈ... 외계 ..ㅁ..체.... 지구...를 ㅊ..략 했다....',
                '그ㄷ..이 현재 지구 생..명..ㅊ... ㅈ종... 시작 했....',
                '다...시.. 한....번 반ㅂ... 한다...',
                '현... 외계 ㅅ...명..체.... ㅈ...구... 침.. ㅎ..다..',
                '통...ㅅ..이... ㅈ...지.. 못하...다....',
                '조종 당...ㅎ..는... 지..ㄱ...생....를 ㅁ..찔...라...',
                '빠ㄹ...게.... 정...리..ㅎ...도...록...행..ㅇ.... 비..네...',
            ]
        },
        {
            'stage': 2,
            'text': [
                '000 대..원... 고....ㅅ..많았....다...',
                '지구..생..ㅁ..체를...처...ㄹ..하...느...라...',
                '하...ㅈ..만...아...직... 끝ㅇ...난..ㄱ..아..니..네..',
                '우ㄹ..는... 이..들의... 우...ㅈ...로...쫓ㅇ..낼거...네..',
                '다..ㅅ..는.. 지..구를.. 침..ㄹ..하지..못..하도..ㄹ...',
                '이들..은...전..ㄴ.. 다..게.. 공..ㄱ.. 조심...하..ㄷ..록',
                '보...ㅇ..는.. 모....ㄷ..적들... 을.. 무ㅉ...르도...록...',
                'ㅃ..르..게.. 정...ㄹ...하...ㄷ...록...ㅎ..운을... ㅂ..네...',
            ]
        }
    ],
    'ending': [
        {
            'stage': 1,
            'text': [
                '지구를 지키지 못했다...',
                '지구 생명체들은 모두 최면에 걸려 노예가 되었다...'
            ]
        }
    ]
}

PAUSE_CONTEXT = [
    {
        'text': ' Press [ESC] to return Game!!'
    },
    {
        'text': '   Your Score is'
    }
]
