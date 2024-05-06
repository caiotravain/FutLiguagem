%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

int yylex(void);
void yyerror(char *s);

struct Node 
{ 
    // Any data type can be stored in this node 
    void  *data; 
  
    struct Node *next; 
}; 



struct Player_Struct {
    char* name;
    int skill;
    struct Player_Struct* next;
    bool ball;
    
};



struct Team_Struct {
    char* name;
    struct Player_Struct* players;
};

struct Game_Struct {
    char* name;
    struct Team_Struct* team1;
    struct Team_Struct* team2;
    int score1;
    int score2;
    struct Player_Struct* goal_scorer;
};
void push(struct Node** head_ref, void *new_data, size_t data_size) 
{ 
    // Allocate memory for node 
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node)); 
  
    new_node->data  = malloc(data_size); 
    new_node->next = (*head_ref); 
  
    // Copy contents of new_data to newly allocated memory. 
    // Assumption: char takes 1 byte. 
    int i; 
    for (i=0; i<data_size; i++) 
        *(char *)(new_node->data + i) = *(char *)(new_data + i); 
  
    // Change head pointer as new node is added at the beginning 
    (*head_ref)    = new_node; 
} 
void remove_team(struct Node** head_ref, char* name) {
    struct Node* current = *head_ref;
    struct Node* prev = NULL;
    while (current != NULL) {
        struct Team_Struct* team = (struct Team_Struct*)current->data;
        if (strcmp(team->name, name) == 0) {
            if (prev == NULL) {
                *head_ref = current->next;
            } else {
                prev->next = current->next;
            }
            free(team);
            free(current);
            return;
        }
        prev = current;
        current = current->next;
    }
}
void remove_player(struct Node** head_ref, char* team_name, char* player_name) {
    struct Node* current = *head_ref;
    struct Node* prev = NULL;
    while (current != NULL) {
        struct Team_Struct* team = (struct Team_Struct*)current->data;
        if (strcmp(team->name, team_name) == 0) {
            struct Player_Struct* current_player = team->players;
            struct Player_Struct* prev_player = NULL;
            while (current_player != NULL) {
                if (strcmp(current_player->name, player_name) == 0) {
                    if (prev_player == NULL) {
                        team->players = current_player->next;
                    } else {
                        prev_player->next = current_player->next;
                    }
                    free(current_player);
                    return;
                }
                prev_player = current_player;
                current_player = current_player->next;
            }
        }
        prev = current;
        current = current->next;
    }
}
void printList(struct Node *node, void (*fptr)(void *)) 
{ 
    while (node != NULL) 
    { 
        (*fptr)(node->data); 
        node = node->next; 
    } 
} 
void print_team(void *n) 
{ 
    struct Team_Struct* team = (struct Team_Struct*)n;
    printf("Team: %s\n", team->name);
    struct Player_Struct* player = team->players;
    int i = 0;
    while (player != NULL) {
        printf("Player_%d(%s)\n", i , player->name, player->skill);
        i++;
        player = player->next;
    }
}
void print_player(void *n) 
{ 
    struct Player_Struct* player = (struct Player_Struct*)n;
    printf("Player: %s, ", player->name);
    printf("Skill: %d, ", player->skill);
    printf("Ball: %s\n", player->ball ? "true" : "false");
}

struct Node* list_teams = NULL;
struct Team_Struct* teams;
struct Node* list_games = NULL;
struct Game_Struct* games;
struct Game_Struct* current_game = NULL;



void print_game(void *n) 
{ 
    struct Game_Struct* game = (struct Game_Struct*)n;
    printf("Game: %s vs %s\n", game->team1->name, game->team2->name);
    printf("Score: %d vs %d\n", game->score1, game->score2);
    //print all goal scorers
    struct Player_Struct* player = game->goal_scorer;
    while (player != NULL) {
        printf("Goal scorer: %s\n", player->name);
        player = player->next;
    }
}



struct Team_Struct* find_team(char* name) {
    struct Node* current = list_teams;
    while (current != NULL) {
        struct Team_Struct* team = (struct Team_Struct*)current->data;
        if (strcmp(team->name, name) == 0) {
            return team;
        }
        current = current->next;
    }
    return NULL;
}

struct Player_Struct* find_player(struct Team_Struct* team, char* name) {
    struct Player_Struct* current = team->players;
    while (current != NULL) {
        if (strcmp(current->name, name) == 0) {
            return current;
        }
        current = current->next;
    }
    return NULL;
}
struct Game_Struct* find_game(char* name) {
    struct Node* current = list_games;
    while (current != NULL) {
        struct Game_Struct* game = (struct Game_Struct*)current->data;
        if (strcmp(game->name, name) == 0) {
            return game;
        }
        current = current->next;
    }
    return NULL;
}

%}


%union {
    char *sval;
    int ival;
    struct Player_Struct* pval;
}

%type <pval> player_declaration team_Setup


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
%token MATCH VS DRIBBLES PASSES SHOOTS GOAL AS ARROW
%token BALLCONTROL TRUE false_id IF




%%

block:
    | statement EOL block
    | statement

statement:
    |  team_Setup
    |  skill_lookup
    |  player_declaration
    |  print_function
    |  remove
    |  match_declaration
    |  actions
    |  ball_control
    |  if_statement
    ;

team_Setup: 
    |  TEAM_DECLARATION IDENTIFIER
    {
        // printf("Setting up team %s\n", $2);
        struct Team_Struct* team = malloc(sizeof(struct Team_Struct));
        team->name = $2;
        team->players = NULL;
        push(&list_teams, team, sizeof(struct Team_Struct));
        struct Team_Struct* saida = find_team($2);

    }
    ;
player_declaration:
    | IDENTIFIER DOT ADDPLAYER LPAREN IDENTIFIER SKILL NUMBER RPAREN
    {
        // printf("Setting up players %s for team %s with skill %d\n", $5, $1, $7);
        struct Player_Struct* player = malloc(sizeof(struct Player_Struct));
        player->name = $5;
        player->skill = $7;
        player->ball = false;
        struct Team_Struct* team = find_team($1);
        //add player to the linked list of players in the team
        player->next = team->players;
        team->players = player;
    }

    ;

skill_lookup:
    | IDENTIFIER DOT IDENTIFIER DOT SKILL
    {
        // printf("Looking up skill for team %s and player %s\n", $1, $3);
        struct Team_Struct* team = find_team($1);
        struct Player_Struct* player = find_player(team, $3);
    }

print_function:
    | PRINT TEAM_DECLARATION IDENTIFIER
    {
        struct Team_Struct* team = find_team($3);
        print_team(team);
    }
    | PRINT PLAYER IDENTIFIER DOT IDENTIFIER
    {
        struct Team_Struct* team = find_team($3);
        
        struct Player_Struct* player = find_player(team, $5);
        print_player(player);
    }
    | PRINT MATCH IDENTIFIER
    {
        struct Game_Struct* game = find_game($3);
        print_game(game);
    }
    ; 

remove:
    | REDCARD IDENTIFIER DOT IDENTIFIER EOL remove 
    {
        remove_player(&list_teams, $2, $4);
    }
    | REDCARD IDENTIFIER EOL remove 
    {
        remove_team(&list_teams, $2);
    }
    | REDCARD IDENTIFIER DOT IDENTIFIER 
    {
        remove_player(&list_teams, $2, $4);
    }
    | REDCARD IDENTIFIER
    {
        remove_team(&list_teams, $2);
    }
match_declaration:
    | MATCH IDENTIFIER VS IDENTIFIER AS IDENTIFIER
    {
        // struct Game_Struct* game = malloc(sizeof(struct Game_Struct));
        // game->name = $6;
        // game->team1 = find_team($2);
        // game->team2 = find_team($4);
        // game->score1 = 0;
        // game->score2 = 0;
        // game->goal_scorer = NULL;
        // push(&list_games, game, sizeof(struct Game_Struct));
        // //give ball to a first player
        // struct Player_Struct* player = game->team1->players;
        // player->ball = true;
       }
    
    ;
actions:
    | remove 
    | player_action
    | ball_control
    ;
player_action:
    | IDENTIFIER ARROW IDENTIFIER DOT IDENTIFIER DRIBBLES IDENTIFIER DOT IDENTIFIER
    {
        // struct Game_Struct* game = find_game($1);
        // struct Team_Struct* team = find_team($3);
        // struct Player_Struct* player = find_player(team, $5);
        // struct Team_Struct* team2 = find_team($7);
        // struct Player_Struct* player2 = find_player(team2, $9);
        //if player 1 has better skill than player 2 tehre is a 20% chance of failure
        // if (player->skill >= player2->skill) {
        //     if (rand() % 100 < 20) {
        //         printf("Player %s failed to dribble\n", player->name);
        //     }
        //     else {
        //         player->ball = false;
        //         player2->ball = true;
        //     }
        // }
        // else {
        //     printf("Player %s failed to dribble player %s\n", player->name, player2->name);
        //     player->ball = false;
        //     player2->ball = true;

            
        // }

    }
    | IDENTIFIER ARROW IDENTIFIER DOT IDENTIFIER PASSES IDENTIFIER DOT IDENTIFIER
    {
        // struct Game_Struct* game = find_game($1);
        // struct Team_Struct* team = find_team($3);
        // struct Player_Struct* player = find_player(team, $5);
        // struct Team_Struct* team2 = find_team($7);
        // struct Player_Struct* player2 = find_player(team2, $9);
        // if (player->ball) {
        //     player->ball = false;
        //     player2->ball = true;
        // }
        // else {
        //     printf("Player %s does not have the ball\n", player->name);
        // }
    }
    | IDENTIFIER ARROW IDENTIFIER DOT IDENTIFIER SHOOTS
    
    | IDENTIFIER ARROW IDENTIFIER DOT IDENTIFIER GOAL
    {
        // struct Game_Struct* game = find_game($1);
        // struct Team_Struct* team = find_team($3);
        // //adicionando o jogador que fez o gol na lista de jogadores que fizeram gol
        // struct Player_Struct* player_action = find_player(team, $5);
        // if (player_action->ball) {
        //     struct Player_Struct* player = malloc(sizeof(struct Player_Struct));
        //     player->name = $5;
        //     player->next = game->goal_scorer;
        //     game->goal_scorer = player;

        //     if (strcmp(game->team1->name, team->name) == 0) {
        //         game->score1++;
        //     } else {
        //         game->score2++;
        //     }
        // }
        // else {
        //     printf("(GOAL)Player %s does not have the ball\n", player_action->name);
        // }
    }
ball_control:
    | BALLCONTROL IDENTIFIER false_id 
    // {
    //     struct Game_Struct* game = find_game($2);
    //     struct Team_Struct* team = game->team1;
    //     struct Player_Struct* player = team->players;
    //     while (player != NULL) {
    //         player->ball = true;
    //         player = player->next;
    //     }
    //     struct Team_Struct* team2 = game->team2;
    //     struct Player_Struct* player2 = team2->players;
    //     while (player2 != NULL) {
    //         player2->ball = true;
    //         player2 = player2->next;
    //     }

    // }
    | BALLCONTROL IDENTIFIER TRUE 
    // {
    //     struct Game_Struct* game = find_game($2);
    //     struct Team_Struct* team = game->team1;
    //     struct Player_Struct* player = team->players;
    //     while (player != NULL) {
    //         player->ball = false;
    //         player = player->next;
    //     }
    //     //set the ball to the first player and remove the ball from all other players
    //     struct Team_Struct* team2 = game->team2;
    //     struct Player_Struct* player2 = team2->players;
    //     while (player2 != NULL) {
    //         player2->ball = false;
    //         player2 = player2->next;
    //     }
    //     //give ball to a first player of team1
    //     struct Player_Struct* player3 = game->team1->players;
    //     player3->ball = true;


    // }
    ;
if_statement:
    | IF LPAREN IDENTIFIER DOT IDENTIFIER GT NUMBER RPAREN LBRACE actions RBRACE
    {
        struct Team_Struct* team = find_team($3);
        struct Player_Struct* player = find_player(team, $5);
        if (player->skill > $7) {
            //execute actions

        }
    }

    ;
%%

int main(int argc, char **argv) {
    yyparse();
}

void yyerror(char *s) {
    fprintf(stderr, "error: %s\n", s);
    //show where the error is

}
