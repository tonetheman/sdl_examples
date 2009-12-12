#include <SDL/SDL.h>
#include <SDL/SDL_ttf.h>
#include <lua5.1/lua.hpp>
#include <iostream>

static SDL_Surface* screen = 0;
static lua_State * lstate = 0;
static TTF_Font* menu_font = 0;

void dump_lua() {
	std::cout << "lua_gettop: " <<  lua_gettop(lstate) << std::endl;
}

TTF_Font* loadfont(char * file, int ptsize) {
	TTF_Font* tmpfont;
	tmpfont = TTF_OpenFont(file,ptsize);
	if (tmpfont==0) {
		std::cout << "unable to open font " << file <<
		std::endl;
	}
	return tmpfont;
}

void engine_init() {
	SDL_Init(SDL_INIT_EVERYTHING);
	if (TTF_Init()==-1) {
		std::cout << "unable to init ttf" <<
		std::endl;
	}
	menu_font = loadfont("data/visitor1.ttf",10);
	if (menu_font==0) {
		std::cout << "unable to load menu font" <<
		std::endl;
	}
}

void engine_shutdown() {
	SDL_Quit();
}

void vid_init() {
	int width = 400, height = 400;
	lua_getglobal(lstate, "video_width");
	if (!lua_isnumber(lstate,-1)) {
		std::cout << "warn no video_width" << std::endl;
	} else {
		width = (int)lua_tonumber(lstate,-1);
	}

	lua_getglobal(lstate, "video_height");
	if (!lua_isnumber(lstate,-1)) {
		std::cout << "warn no video height" << std::endl;
	} else {
		height = lua_tonumber(lstate,-1);
	}

	screen = SDL_SetVideoMode(width,height,32,SDL_SWSURFACE);
}

void script_init() {
	lstate = luaL_newstate();
}

void script_shutdown() {
	lua_close(lstate);
}

void load_ini() {
	int result = luaL_loadfile(lstate, "tiny.lua");
	if (result==0) {
		std::cout << "loaded tiny fine" << std::endl;
		lua_pcall(lstate,0,0,0);
	} else if (LUA_ERRSYNTAX) {
		std::cout << "ERROR SYNTAX in loading tiny.lua" <<
		std::endl;
	} else if (LUA_ERRMEM) {
		std::cout << "ERROR MEM in loading tiny.lua" <<
		std::endl;
	}
}

void game_loop() {
	SDL_Event keyevt;
	bool running = true;
	while (running) {
		while(SDL_PollEvent(&keyevt)) {
			if (keyevt.type == SDL_QUIT) {
				std::cout << "got a quit event" << std::endl;
				running = false;
				break;
			}
			if (keyevt.type == SDL_KEYDOWN) {
			}
			if (keyevt.type == SDL_KEYUP) {
			}
		}
	}
}

int main(int argc, char* argv[]) {
	script_init();
	load_ini();
	engine_init(); // includes ttf init too
	vid_init();

	dump_lua();

	game_loop();
	
	engine_shutdown();
	script_shutdown();
	return 0;
}
