#include <SDL/SDL.h>
#include <lua5.1/lua.hpp>
#include <iostream>

static SDL_Surface* screen = 0;
static lua_State * lstate = 0;

void dump_lua() {
	std::cout << "lua_gettop: " <<  lua_gettop(lstate) << std::endl;
}

void engine_init() {
	SDL_Init(SDL_INIT_EVERYTHING);
}

void engine_shutdown() {
	SDL_Quit();
}

void vid_init() {
	screen = SDL_SetVideoMode(400,400,32,SDL_SWSURFACE);
}

void script_init() {
	lstate = luaL_newstate();
}

void script_shutdown() {
	lua_close(lstate);
}

void load_ini() {
	luaL_loadfile(lstate, "tiny.lua");
}

int main(int argc, char* argv[]) {
	script_init();
	load_ini();
	engine_init();
	vid_init();

	dump_lua();
	
	engine_shutdown();
	script_shutdown();
	return 0;
}
