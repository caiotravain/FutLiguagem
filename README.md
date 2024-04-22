# FutLiguage
language de futebol

<p>
BLOCK = { STATEMENT };
STATEMENT = ( team_setup | match_declaration | player_action | goal_event ), "\n" ;
team_setup  = "team", team_name, "{", { player_declaration }, "}" ;
match_declaration = "match", team_name, "vs", team_name, "{", { player_action | match_action }, "}" ;
player_declaration = "player", player_name, "with", "speed", speed_value, "skill", skill_value, "\n" ;
player_action = player_name, action_type, [ player_name | goal_event ] ;
match_action =["matchtime(", time_value ,")"] | ["end match"];
goal_event = player_name, "scores" ;
team_name = letter, { letter | "_" | digit } ;
player_name = letter, { letter | "_" | digit } ;
action_type = "passes_to" | "dribbles" | "shoots";
goal_outcome = "scores" ;
speed_value = digit, { digit } ;
skill_value = digit, { digit } ;
time_value = digit, { digit } ;
LETTER = ( "a" | "..." | "z" | "A" | "..." | "Z" ) ;
DIGIT = ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ;
</p>
