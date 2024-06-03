%{
#include <stdio.h>
#include <string.h>


%}


%union {
    char *sval;
    int ival;
}



%token EOL
%token PLAYER
%token LPAREN RPAREN SEMICOLON
%token ASSIGN
%token TEAM_DECLARATION
%token <ival> NUMBER 
%token STRING
%token PLUS MINUS STAR SLASH
%token EQ NE LT LE GT GE
%token AND OR NOT DOT
%token <sval> IDENTIFIER
%token LBRACE RBRACE
%token <sval> SKILL
%token ADDPLAYER
%token PRINT
%token REDCARD
%token MATCH VS DRIBBLES PASSES SHOOTS SCORES AS ARROW
%token TRUE false_id IF ENDMATCH MATCHTIME
%token S 




%%

block:
    | statement EOL block
    | statement

statement:
    |  team_Setup
    |  skill_lookup
    |  player_declaration
    |  print_function
    |  match_declaration
    |  skill_assignment

    ;

team_Setup: 
    |  TEAM_DECLARATION IDENTIFIER
    ;
player_declaration:
    | IDENTIFIER DOT ADDPLAYER LPAREN IDENTIFIER SKILL skill_bool_expression RPAREN
    ;

skill_lookup:
    | IDENTIFIER DOT IDENTIFIER DOT SKILL

print_function:
    | PRINT TEAM_DECLARATION IDENTIFIER
    | PRINT PLAYER IDENTIFIER DOT IDENTIFIER
    | PRINT MATCH IDENTIFIER
    ; 



match_declaration:
    | MATCH IDENTIFIER VS IDENTIFIER LBRACE EOL actions RBRACE
    | MATCH IDENTIFIER VS IDENTIFIER LBRACE actions RBRACE
    | MATCH IDENTIFIER VS IDENTIFIER LBRACE actions RBRACE S
    | MATCH IDENTIFIER VS IDENTIFIER LBRACE EOL actions RBRACE S




    ;

    
actions:
    | player_action EOL actions 
    | if_statement EOL actions
    | remove EOL actions
    | match_declaration EOL actions
    | skill_assignment EOL actions
    | EOL actions
    | match_time EOL actions
    | print_function EOL actions
    | ENDMATCH EOL actions
    | player_action
    | if_statement
    | remove
    | skill_assignment
    | match_time
    | print_function
    | match_declaration
    | ENDMATCH


    
    ;

remove:
    | IDENTIFIER DOT IDENTIFIER REDCARD 
    ;
    
player_action:
    |IDENTIFIER DOT IDENTIFIER PASSES
    |IDENTIFIER DOT IDENTIFIER SHOOTS
    |IDENTIFIER DOT IDENTIFIER SCORES
    ;
if_statement:
    | IF LPAREN skill_bool_expression RPAREN LBRACE EOL actions RBRACE
    | IF LPAREN skill_bool_expression RPAREN LBRACE actions RBRACE


skill_bool_expression:
    | skill_bool_term OR skill_bool_expression
    | skill_bool_term

skill_bool_term:
    | skill_real_expression AND skill_bool_term
    | skill_real_expression

skill_real_expression:
    | skill_expression EQ skill_real_expression
    | skill_expression GT skill_real_expression
    | skill_expression GE skill_real_expression
    | skill_expression LT skill_real_expression
    | skill_expression LE skill_real_expression
    | skill_expression NE skill_real_expression
    | skill_expression

skill_expression:
    | skill_term PLUS skill_expression
    | skill_term MINUS skill_expression
    | skill_term 

skill_term:
    | skill_factor STAR skill_term
    | skill_factor SLASH skill_term
    | skill_factor

skill_factor:
    | NUMBER
    | skill_lookup
    | match_set_time
    | LPAREN skill_expression RPAREN
    | NOT skill_factor
    | PLUS skill_factor
    | MINUS skill_factor

match_set_time:
    | MATCHTIME

skill_assignment:
    | IDENTIFIER DOT IDENTIFIER DOT SKILL ASSIGN skill_bool_expression

match_time :
    | MATCHTIME LPAREN skill_bool_expression RPAREN


    


    ;
%%

int main(int argc, char **argv) {
    yyparse();
}

void yyerror(char *s) {
    fprintf(stderr, "error: %s\n", s); 

}
