camel = r"""
The camel habitat...

       .--' |
      /___^ |     .--.
          ) |    /    \
         /  |  /`      '.
        |   '-'    /     \
        \         |      |\
         \    /   \      /\|
          \  /'----`\   /
          |||       \\ |
          ((|        ((|
          |||        |||
         //_(       //_(

lion = r"""
The lion habitat...
\|\||
  -' ||||/
 /7   |||||/
/    |||||||/`-.____________
\-' |||||||||               `-._
 -|||||||||||               |` -`.
   ||||||               \   |   `\\
    |||||\  \______...---\_  \    \\
       |  \  \           | \  |    ``-.__--.
       |  |\  \         / / | |       ``---'
     _/  /_/  /      __/ / _| |
    (,__/(,__/      (,__/ (,__/
The lion is roaring!"""

deer = r"""
The deer habitat...
                     /|       |\
                  `__\\       //__'
                     ||      ||
                   \__`\     |'__/
                     `_\\   //_'
                     _.,:---;,._
                     \_:     :_/
                       |@. .@|
                       |     |
                       ,\.-./ \
                       ;;`-'   `---__________-----.-.
                       ;;;                         \_\
                       ';;;                         |
                        ;    |                      ;
                         \   \     \        |      /
                          \_, \    /        \     |\
                            |';|  |,,,,,,,,/ \    \ \_
                            |  |  |           \   /   |
                            \  \  |           |  / \  |
                             | || |           | |   | |
                             | || |           | |   | |
                             | || |           | |   | |
                             |_||_|           |_|   |_|
                            /_//_/           /_/   /_/
Pretty good!"""

goose = r"""
The goose habitat...
                                   ___
                               ,-""   `.
                             ,'  _   e )`-._
                            /  ,' `-._<.===-'
                           /  /
                          /  ;
              _          /   ;
 (`._    _.-"" ""--..__,'    |
 <_  `-""                     \
  <`-                          :
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<
                   `-'
Beautiful!"""

bat = r"""
,*-~"`^"*u_                                _u*"^`"~-*,
  p!^       /  jPw                            w9j \        ^!p
w^.._      /      "\_                      _/"     \        _.^w
     *_   /          \_      _    _      _/         \     _* 
       q /           / \q   ( `--` )   p/ \          \   p
       jj5****._    /    ^\_) o  o (_/^    \    _.****6jj
                *_ /      "==) ;; (=="      \ _*
                 `/.w***,   /(    )\   ,***w.\"
                  ^ ilmk ^c/ )    ( \c^      ^
                          'V')_)(_('V'
                              `` ``
It's doing fine."""

rabbit = r"""
The rabbit habitat...
            ,\
             \\\,_
              \` ,\
         __,.-" =__)
       ."        )
    ,_/   ,    \/\_
    \_|    )_-\ \_-`
      `-----` `--`
It looks fine!"""

animals = [camel, lion, deer, goose, bat, rabbit]
print("I love animals!")
print("Let's check out the animals...")
while True:
    print("Please enter the number of the habitat you would like to view (0-5):")
    user_input = input("> ")
    if user_input == "exit":
        break
    try:
        habitat_number = int(user_input)
        if 0 <= habitat_number < len(animals):
            print(animals[habitat_number])
        else:
            print("Invalid habitat number. Please enter a number between 0 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 0 and 5, or type 'exit' to end the program.")

print("See you later!")
