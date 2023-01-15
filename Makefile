##
## EPITECH PROJECT, 2023
## maths
## File description:
## Makefile
##

NAME	=	307multigrains

all:
	chmod +x $(NAME)

clean:
	$(RM) -r __pycache__

fclean: clean

re: fclean all
