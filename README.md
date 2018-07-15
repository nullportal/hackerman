# hackerman
A linux terminal script to spit out open source software on your screen. Befudle managers, entertain co-workers, annoy girlfriends!

### Example output (captured with [Peek](https://github.com/phw/peek#arch-linux)!)
![Low FPS Example of Hackerman Script Running](https://raw.githubusercontent.com/jm-janzen/home/gh-pages/assets/img/hackerman.gif)

### Get it
`git clone git@github.com:nullportal/hackerman.git`

### Try it
```
cd hackerman
./bin/hackerman "abc"  # or whatever
ctrl+c                 # to exit
```

### Get help
```
./bin/hackerman --help
usage: hackerman [OPTS]

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY_STR, --query-str QUERY_STR
                        general string to search for using Github API
  -l QUERY_LANG, --query-lang QUERY_LANG
                        programming language to filter results by (eg: cpp)
  -s TYPING_SPEED, --typing-speed TYPING_SPEED
                        typing (default 20)
  -S CLIENT_CREDENTIALS, --client-credentials CLIENT_CREDENTIALS
                        string matching 'CLIENT_ID:CLIENT_SECRET', with proper
                        id and secret
```
