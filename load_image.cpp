#include <SDL/SDL_image.h>
#include <string>

SDL_Surface* load_image(std::string filename) {
	SDL_Surface* loadedImage = 0;
	SDL_Surface* optimizedImage = 0;
	loadedImage = IMG_Load(filename.c_str());
	if (loadedImage!=0) {
		optimizedImage = SDL_DisplayFormat(loadedImage);
		SDL_FreeSurface(loadedImage);
	}
	return optimizedImage;
}
