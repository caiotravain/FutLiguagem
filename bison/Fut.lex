%{
# include "Fut.tab.h"
%}

WS     [ \t]
TEAM_DECLARATION  "TEAM"
DRIBBLES "DRIBBLES"
AS "AS"
TRUE "TRUE"
false_id "FALSE"
PASSES "PASSES"
SCORES "SCORES"	
SHOOTS "SHOOTS"
REDCARD "REDCARD"
MATCH "MATCH"
PLAYER "PLAYER"
SKILL "SKILL"
PRINT "PRINT"
IDENTIFIER [a-zA-Z][a-zA-Z0-9]*
NUMBER [0-9]+
STRING \".*\"
ADDPLAYER "AddPlayer"
ENDMATCH "ENDMATCH"
MATCHTIME "MATCHTIME"




%%

{WS}
"+"  { return PLUS; }
"-"  { return MINUS; }
"*"  { return STAR; }
"/"  { return SLASH; }
"="  { return ASSIGN; }
"("  { return LPAREN; }
")"  { return RPAREN; }
";"  { return SEMICOLON; }
"==" { return EQ; }
"!=" { return NE; }
"<"  { return LT; }
"<=" { return LE; }
">"  { return GT; }
">=" { return GE; }
"{"  { return LBRACE; }
"}"  { return RBRACE; }
"."  { return DOT; }
\n  { return EOL; }
"VS" { return VS; }
"->" { return ARROW; }
"if " { return IF; }
"and" { return AND; }
"or" { return OR; }
"not" { return NOT; }



{AS} {
    return AS;
}
{TEAM_DECLARATION} {
    return TEAM_DECLARATION;
}
{PLAYER} {
    return PLAYER;
}
{REDCARD} {
    return REDCARD;
}
{MATCH} {
    return MATCH;
}
{ENDMATCH} {
    return ENDMATCH;
}
{DRIBBLES} {
    return DRIBBLES;
}
{PASSES} {
    return PASSES;
}
{SCORES} {
    return SCORES;
}
{SHOOTS} {
    return SHOOTS;
}

{SKILL} {
    yylval.sval = strdup(yytext);
    return SKILL;
}
{ADDPLAYER} {
    return ADDPLAYER;
}
{PRINT} {
    return PRINT;
}
{TRUE} {
    return TRUE;
}

{false_id} {
    return false_id ;
}
{MATCHTIME} {
    return MATCHTIME;
}


{IDENTIFIER} {
    yylval.sval = strdup(yytext);
    return IDENTIFIER;
}



	


{NUMBER} {
    yylval.ival = atoi(yytext);
    return NUMBER;
}


{STRING} {
    return STRING;
}

. { return yytext[0]; }

%%
