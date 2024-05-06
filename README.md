# FutLiguagem
language de futebol

<p>
BLOCK = { STATEMENT };<br/>
STATEMENT = ( team_setup | match_declaration | player_declaration | print_function | skill_assignment | skill_lookup), "\n" ;<br/>
team_setup  = "TEAM", team_name ;<br/>
match_declaration = "match", team_name, "vs", team_name, "{", { actions}, "}" ;<br/>
player_declaration = TEAM, DOT, "AddPlayer", "(", NAME, "SKILL", SKILL_BOOL_EXPRESSION, ")", "\n" ;<br/>
SKILL_LOOKUP = TEAM, DOT, PLAYER,DOT, "SKILL";<br/>
actions = (player_action, | ball_control  | 
if_statement  |  remove,  | skill_assigment  |  match_action | print_function) ;<br/>

print_function = "PRINT", "TEAM", TEAM  |   "PRINT", "PLAYER", TEAM ,  DOT , PLAYER  |  "PRINT", "MATCH" , MATCH;<br/>

player_action= (TEAM, DOT, PLAYER, "DRIBBLES", TEAM, DOT, PLAYER  | TEAM, DOT, PLAYER, "PASSES", TEAM, DOT, PLAYER | 
TEAM, DOT, PLAYER, "SHOOTS" 
| 
TEAM, DOT, PLAYER, "SCORES" );<br/>
ball_control = "BALLCONTROL TRUE" | "BALLCONTROL FALSE"  ;<br/>
match_action =["matchtime(", time_value ,")"] | ["end match"];<br/>
goal_event = player_name, "scores" ;<br/>
if_statement = "if", "(" ,SKILL_BOOL_EXPRESSION, ")","{", actions, "}" ;<br/>
remove = "REDCARD" ,TEAM | "REDCARD", TEAM ,DOT, PLAYER  ;<br/>
skill_assignment =TEAM ,DOT, PLAYER , DOT , "SKILL", "=", SKILL_BOOL_EXPRESSION ;<br/>
team_name = letter, { letter | "_" | digit } ;<br/>
player_name = letter, { letter | "_" | digit } ;<br/>
time_value = digit, { digit } ;<br/>
SKILL_BOOL_EXPRESSION = { SKILL_BOOL_TERM |  OR};<br/>

SKILL_BOOL_TERM = { SKILL_REAL_EXPRESSION|  AND};<br/>

SKILL_REAL_EXPRESSION= { SKILL_EXPRESSION|  ">" |  "<" |  "==" |  "<=" |  ">=" |  "!=" };<br/>

SKILL_EXPRESSION= { SKILL_TERM, " +" |  "-" };<br/>

SKILL_TERM= { SKILL_FACTOR, " *" |  "/" };<br/>


SKILL_FACTOR= (DIGIT  | SKILL_LOOKUP| "(" , SKILL_EXPRESSION, ")"  | NOT, SKILL_FACTOR|  "+" , SKILL_FACTOR, "-", SKILL_FACTOR);<br/>


LETTER = ( "a" | "..." | "z" | "A" | "..." | "Z" ) ;<br/>
DIGIT = ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ;<br/>
DOT = "."; <br/>
</p>
<img src="download.png"/>
