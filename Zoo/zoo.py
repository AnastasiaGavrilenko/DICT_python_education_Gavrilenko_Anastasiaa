def main():
    camel = r"""
    The camel habitat...
           _
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
    """
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
    """
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

    """
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
    """
    bat = r"""
    The bat habitat...


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
    """
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
    """
    animals = [camel, lion, deer, goose, bat, rabbit]
    while True:
        user_input = input("Please enter the number of the habitat you would like to view: ")
        if user_input == "exit":
            break
        if user_input.isdigit():
            habitat_num = int(user_input)
            if 0 <= habitat_num < len(animals):
                print(animals[habitat_num])
            else:
                print("No such habitat.")
    print("See you later!")

if __name__ == "__main__":
    main()
