# Filters

&gt; Auto-generated documentation for the **Filters** module of the Gorgon C++ Game Engine.


## Contents

- [Enums](#enums)
- [Functions](#functions)

---

## Enums

### `OutOfBoundsPolicy`

**Namespace:** `Gorgon`

These are the policies that governs values outside the boundaries of the image. Not all values are available in all functions


### `OutOfRangePolicy`

**Namespace:** `Gorgon`

These are the policies that governs values that falls outside the allowed range of values. For performance reasons, these policies will not be applied to float or double images. If necessary, you may use Clamp, Abs and Scale functions separately.


---

## Functions

### `output({W, H}, mode)`

**Returns:** `Containers::basic_Image<CT_>`



### `for(int y=0; y<H; y++)`

**Returns:** ``



### `for(int x=0; x<W; x++)`

**Returns:** ``



### `for(int i=0; i<w; i++)`

**Returns:** ``



### `for(int j=0; j<h; j++)`

**Returns:** ``



### `if(cx >= 0 && cx < W && cy >= 0 && cy < H)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `if(std::is_integral<CT_>::value)`

**Returns:** ``



### `switch(outofrange)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int y=0; y<H; y++)`

**Returns:** ``



### `for(int x=0; x<W; x++)`

**Returns:** ``



### `for(int i=0; i<w; i++)`

**Returns:** ``



### `for(int j=0; j<h; j++)`

**Returns:** ``



### `if(cx < 0 || cx >= W || cy < 0 || cy >= H)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `if(std::is_integral<CT_>::value)`

**Returns:** ``



### `switch(outofrange)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `switch(outofbounds)`

**Returns:** ``



### `forpixels([&](auto, auto, auto &values, float kernel)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `forpixelsmultiplier()`

**Returns:** ``



### `forpixels([&](auto x, auto y, auto &values, float kernel)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `forpixels([&](auto x, auto y, auto &values, float kernel)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `forpixels([&](auto x, auto y, auto &values, float kernel)`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `if(noalpha && A != -1)`

**Returns:** ``



### `for(int y=0; y<H; y++)`

**Returns:** ``



### `for(int x=0; x<W; x++)`

**Returns:** ``


