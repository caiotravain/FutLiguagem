# FutLiguagem
language de futebol

<p>
BLOCK = { STATEMENT }; </br>
STATEMENT = ( team_setup | match_declaration | player_action | goal_event ), "\n" ; </br>
team_setup  = "team", team_name, "{", { player_declaration }, "}" ; </br>
match_declaration = "match", team_name, "vs", team_name, "{", { player_action | match_action }, "}" ; </br>
player_declaration = "player", player_name, "with", "speed", speed_value, "skill", skill_value, "\n" ; </br>
player_action = player_name, action_type, [ player_name | goal_event ] ; </br>
match_action =["matchtime(", time_value ,")"] | ["end match"]; </br>
goal_event = player_name, "scores" ; </br>
team_name = letter, { letter | "_" | digit } ; </br>
player_name = letter, { letter | "_" | digit } ; </br>
action_type = "passes_to" | "dribbles" | "shoots"; </br>
goal_outcome = "scores" ; </br>
speed_value = digit, { digit } ; </br>
skill_value = digit, { digit } ; </br>
time_value = digit, { digit } ; </br>
LETTER = ( "a" | "..." | "z" | "A" | "..." | "Z" ) ; </br>
DIGIT = ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ; </br>
</p>
<img src="download.png"/>
