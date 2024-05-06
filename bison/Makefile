Fut: Fut.lex Fut.y
	bison -d -Wother Fut.y
	lex Fut.lex
	gcc -o $@ Fut.tab.c lex.yy.c -lfl

clean:
	rm -f Fut
	rm -f lex.yy.c
	rm -f Fut.tab.c
	rm -f Fut.tab.h
