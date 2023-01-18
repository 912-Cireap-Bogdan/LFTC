%{
    #include <stdio.h>
    #include <stdlib.h>
%}

%token plus
%token minus
%token assign
%token equal
%token notEqual
%token less
%token greater

%token return
%token if
%token int
%token true
%token false
%token is
%token function


%token identifier
%token number
%token stringCh

%start program

%%

program : stmtlist
declaration : identifier is type
type : character | number | stringCh | boolean | function
stmtlist : stmt | stmt semicolon stmtlist
stmt : simplestmt | structstmt
simplestmt : asiignstmt | iostmt
assignstmt : identifier assign expression
expression : expression plus term | expression minus term | term
term : term mul factor | term div factor | term mod factor | factor
structstmt : ifstmt | whilestmt
logicalop : and | or
ifstmt :  if  condlist   stmtlist  | if condlist  stmtlist  else  stmtlist
condlist : condition | condition logicalop condlist
condition : expression relation expression | bool
relation : less | equal | notEqual | greater

%%

yyerror(char *s) {
    printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char ** argv) {
    if (argc > 1)
        yyin = fopen(argv[1], "r");
    if ((argc > 2) && (!strcmp(argv[2], "-d")))
        yydebug = 1;
    if (!yyparse())
        fprintf(stderr, "error\n");
}