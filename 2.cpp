
#include <SDL/SDL.h>
#include <string>
#include <iostream>

const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;
const int SCREEN_BPP = 32;

SDL_Surface * message = 0;
SDL_Surface * background = 0;
SDL_Surface * screen = 0;

SDL_Surface * load_image(std::string filename) {
	SDL_Surface* loadedImage = 0;
	SDL_Surface* optimizedImage = 0;
	loadedImage = SDL_LoadBMP(filename.c_str());
	if (loadedImage!=0) {
		optimizedImage = SDL_DisplayFormat(loadedImage);
		SDL_FreeSurface(loadedImage);
	}
	return optimizedImage;
}

void apply_surface(int x, int y, SDL_Surface* source, SDL_Surface* destination) {
	SDL_Rect offset;
	offset.x = x;
	offset.y = y;
	SDL_BlitSurface(source,0,destination,&offset);
}

int main() {

	if (SDL_Init(SDL_INIT_EVERYTHING)==-1) {
		return -1;
	}

	screen = SDL_SetVideoMode(SCREEN_WIDTH, SCREEN_HEIGHT,
		SCREEN_BPP, SDL_SWSURFACE);
	if(screen==0) {
		return 1;
	}
	SDL_WM_SetCaption("hello world",0);
	message = load_image("data/hello.bmp");
	background = load_image("data/background.bmp");
	apply_surface(0,0,background,screen);
	apply_surface(320,0,background,screen);
	apply_surface(0,240,background,screen);
	apply_surface(320,240,background,screen);

	apply_surface(180,140,message,screen);

	if (SDL_Flip(screen)==-1) {
		return 1;
	}
	SDL_Delay(2000);
	
	SDL_FreeSurface(message);
	SDL_FreeSurface(background);
	
	SDL_Quit();
	return 0;
	return 0;
}
