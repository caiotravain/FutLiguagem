/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_FUT_TAB_H_INCLUDED
# define YY_YY_FUT_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    EOL = 258,                     /* EOL  */
    PLAYER = 259,                  /* PLAYER  */
    LPAREN = 260,                  /* LPAREN  */
    RPAREN = 261,                  /* RPAREN  */
    SEMICOLON = 262,               /* SEMICOLON  */
    ASSIGN = 263,                  /* ASSIGN  */
    TEAM_DECLARATION = 264,        /* TEAM_DECLARATION  */
    NUMBER = 265,                  /* NUMBER  */
    STRING = 266,                  /* STRING  */
    PLUS = 267,                    /* PLUS  */
    MINUS = 268,                   /* MINUS  */
    STAR = 269,                    /* STAR  */
    SLASH = 270,                   /* SLASH  */
    EQ = 271,                      /* EQ  */
    NE = 272,                      /* NE  */
    LT = 273,                      /* LT  */
    LE = 274,                      /* LE  */
    GT = 275,                      /* GT  */
    GE = 276,                      /* GE  */
    AND = 277,                     /* AND  */
    OR = 278,                      /* OR  */
    NOT = 279,                     /* NOT  */
    DOT = 280,                     /* DOT  */
    IDENTIFIER = 281,              /* IDENTIFIER  */
    LBRACE = 282,                  /* LBRACE  */
    RBRACE = 283,                  /* RBRACE  */
    SKILL = 284,                   /* SKILL  */
    ADDPLAYER = 285,               /* ADDPLAYER  */
    PRINT = 286,                   /* PRINT  */
    REDCARD = 287,                 /* REDCARD  */
    MATCH = 288,                   /* MATCH  */
    VS = 289,                      /* VS  */
    DRIBBLES = 290,                /* DRIBBLES  */
    PASSES = 291,                  /* PASSES  */
    SHOOTS = 292,                  /* SHOOTS  */
    SCORES = 293,                  /* SCORES  */
    AS = 294,                      /* AS  */
    ARROW = 295,                   /* ARROW  */
    BALLCONTROL = 296,             /* BALLCONTROL  */
    TRUE = 297,                    /* TRUE  */
    false_id = 298,                /* false_id  */
    IF = 299,                      /* IF  */
    ENDMATCH = 300,                /* ENDMATCH  */
    MATCHTIME = 301                /* MATCHTIME  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 9 "Fut.y"

    char *sval;
    int ival;

#line 115 "Fut.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_FUT_TAB_H_INCLUDED  */