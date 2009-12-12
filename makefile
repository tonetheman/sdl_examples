
all: 1 2 load_image.o tiny

tiny : tiny.cpp
	g++ -o tiny tiny.cpp `sdl-config --libs` -llua5.1

load_image.o : load_image.cpp
	g++ -o load_image.o -c load_image.cpp

1: 1.cpp
	g++ -o 1 1.cpp `sdl-config --libs`

2: 2.cpp
	g++ -o 2 2.cpp `sdl-config --libs`

clean:
	rm -rf 1
	rm -rf 2
	rm -rf load_image.o
