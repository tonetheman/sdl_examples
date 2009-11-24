#include <SDL/SDL.h>

int main(int argc, char* argv[]) {
	SDL_Init(SDL_INIT_EVERYTHING);

	SDL_Surface* hello = 0;
	SDL_Surface* screen = 0;

	screen = SDL_SetVideoMode(640,480,32,SDL_SWSURFACE);
	hello = SDL_LoadBMP("data/hello.bmp");

	SDL_BlitSurface(hello, 0, screen, 0);
	SDL_Flip(screen);
	SDL_Delay(2000);
	SDL_FreeSurface(hello);

	SDL_Quit();
	return 0;
}
