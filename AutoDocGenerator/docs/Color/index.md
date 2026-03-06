# Color

&gt; Auto-generated documentation for the **Color** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `RGBA`

**Namespace:** `Gorgon`

This class represents a color information. Contains 4 channels, 8 bits each. Red is the lowest bit while alpha is the highest. Please note that conversion from/to integer will work in reverse of the HTML notation. 0xff800000 is dark blue not dark red.

#### Methods

##### `RGBA(—)`

**Returns:** ``

Data type for each channel Default constructor does not perform initialization

##### `Blend(second, alpha)`

**Returns:** ``

Copy constructor Copy constructor with new alpha value Copy constructor with new alpha value Copy constructor with new alpha value Copy constructor with new alpha value Blending constructor

##### `RGBA(const std::string &color)`

**Returns:** `explicit`

Blending constructor Blending constructor Filling constructor Constructs a grayscale color from the given luminance Constructs a grayscale color from the given luminance Conversion from integer Conversion from uint32_t Conversion from float. Assumes the given float value is a 0 to 1 luminance. Sets alpha to 255 Conversion from float. Assumes the given float value is a 0 to 1 luminance. Sets alpha to 255 From string

##### `RGBA(RGBAf color)`

**Returns:** ``

From string

##### `int(—)`

**Returns:** `operator`

Conversion to integer

##### `memcpy(&ret, this, 4)`

**Returns:** ``

##### `uint32_t(—)`

**Returns:** `operator`

Conversion to integer

##### `memcpy(&ret, this, 4)`

**Returns:** ``

##### `memcpy(this, &color, 4)`

**Returns:** ``

Copy assignment From integer assignment

##### `memcpy(this, &color, 4)`

**Returns:** ``

From integer assignment

##### `Luminance(—)`

**Returns:** `Byte`

From float assignment. Assumes the given float value is a 0 to 1 luminance. Sets alpha to 255 Compares two colors Compares two colors Returns the luminance of this color as a single byte number. The returned number could be supplied to a new color to create grayscale representation of this color. This function performs lots of shifts to calculate a luminance close to perceived grayscale value. Probably works even slower than accurate luminance, however, the value returned is directly a byte.

##### `AccurateLuminance(—)`

**Returns:** `float`

Returns the luminance of this color as a floating point value between 0 and 1. The conversion is done to preserve perceived luminance.

##### `HTMLColor(—)`

**Returns:** `std::string`

Returns a six nibble HTML color

##### `Blend(const RGBA &color)`

**Returns:** `void`

Blends the given color into this one. This operation performs regular alpha blending with the current color being blended over.

##### `Blend(color, 1.0f)`

**Returns:** ``

##### `Slide(const RGBA &color, float factor)`

**Returns:** `void`

Blends the given color into this one without performing alpha blending

##### `if(factor == 1)`

**Returns:** ``

##### `Blend(const RGBA &color, float alpha)`

**Returns:** `void`

Blends the given color into this one. This operation performs regular alpha blending with the current color being blended over.

##### `if(color.A * alpha == 255)`

**Returns:** ``

##### `if(aa > 0)`

**Returns:** ``

##### `BlendWith(const RGBA &color)`

**Returns:** `RGBA`

Blends the current color with the given color and returns the result

##### `BlendWith(const RGBA &color, float alpha)`

**Returns:** `RGBA`

Blends the current color with the given color and returns the result

##### `Convert(const Gorgon::Graphics::ColorMode &mode)`

**Returns:** `std::array<Gorgon::Byte, 4>`

Converts this color to a hex representation of this color Converts this color to the given color mode. At most GetChannelsPerPixel(mode) amount of values will be set

##### `switch(mode)`

**Returns:** ``


### `RGBAf`

**Namespace:** `Gorgon`

Represents a four channel 32 bit float per channel color information.

#### Methods

##### `RGBAf(—)`

**Returns:** ``

Data type for each channel Default constructor does not perform initialization

##### `RGBAf(const std::string &color)`

**Returns:** `explicit`

Filling constructor Constructor that sets all color channels to the given value to create a grayscale color. Alpha is set to 1.0f Constructor that sets all color channels to the given value to create a grayscale color. Alpha is set to 1.0f Converts a RGBA to RGBAf Converts a RGBA to RGBAf Converts a RGBA to RGBAf Converts from an unsigned int Converts from an unsigned int Converts from an unsigned int From string

##### `int(—)`

**Returns:** `explicit operator`

From string Copy assignment Assignment from RGBA Assignment from int Assignment from float Assignment from float Conversion to integer

##### `Convert(—)`

**Returns:** `RGBA`

Converts this color to RGBA by clipping the values

##### `Luminance(—)`

**Returns:** `float`

Returns the luminance of this color as a floating point value between 0 and 1. The conversion is done to preserve perceived luminance.

##### `Blend(const RGBAf &color)`

**Returns:** `void`

Compares two colors Compares two colors Blends the given color into this one. This operation performs regular alpha blending with the current color being blended over.

##### `Blend(color, 1.f)`

**Returns:** ``

##### `Blend(const RGBAf &color, float factor)`

**Returns:** `void`

Blends the given color into this one with the given factor that is applied to all channels.

##### `if(color.A==1.f)`

**Returns:** ``

##### `if(aa > 0)`

**Returns:** ``

##### `Slide(const RGBAf &color, float factor)`

**Returns:** `void`

Blends the given color into this one with the given factor that is applied to color and alpha channels separately. This is not regular alpha blending as source alpha is not used.

##### `Slide(const RGBAf &color, float factor_color, float factor_alpha)`

**Returns:** `void`

Blends the given color into this one with the given factor that is applied to color and alpha channels separately. This is not regular alpha blending as source alpha is not used.

##### `Slide(const RGBAf &color, const RGBAf &factor)`

**Returns:** `void`

Blends the given color into this one with the given factor that is applied to color and alpha channels separately. This is not regular alpha blending as source alpha is not used.


### `Pair`

**Namespace:** `Color`

Regular commonly used color. If the system has background image, background color should match the image Alternate colors, often used alternating lists Color for title fonts A color to emphasize a piece of text Inverted text or object A color to highlight a piece of code, often a border is drawn around code segments Keyword in a code segment Comment in a code segment Selection color, both background and foreground. Generally, selection background is drawn on top of regular background color Used to denote something is disabled Used to highlight a portion of text Used for editable text Used to separate pieces. Often forecolor is used as a border, backcolor is ignored Used for containers, often forecolor is used for border. A container that is activated. Often used for windows A container that is passive/unfocused. Often used for windows Used to denote an information section Used to denote a message section Used to denote warnings Used to denote errors Used to denote success messages Link to a page or an operation Used when the mouse hovers over an interactive object Used when the mouse is pressed on an activatable object Used to denote that a link is visited Used to mark active objects Used to mark focused objects Colors for a part which could be used a placeholder or a more pronounced separator Color pair that has a higher contrast then regular color pair A color that is used to draw non-text objects. Often regular color is used for these and in some cases, this might be ignored A color that is used for readonly edit fields A color that is used for list items A color that is used for alternate list items A color that is used for main window background User defined colors should start from this index. Some systems support user defined colors.


### `Triplet`

**Namespace:** `Color`


### `Pack`

**Namespace:** `Color`

#### Methods

##### `Pack(const C_ &forecolor)`

**Returns:** `explicit`

This constructor creates an empty pack, which may not be suitable for use This constructor initializes the pack with a regular color, which then will be used for every color combination.

##### `Pack(const std::initializer_list<std::pair<Designation, C_>> &colors)`

**Returns:** ``

Initializes the pack using designation, color pairs. You may use this constructor to pass color list as an argument. Example use:  namespace Color = Gorgon::Graphics::Color; Color::Pack pack = { {Color::Regular  , Color::Black}, {Color::Inverted , Color::White} };

##### `Set(Designation index, const C_ &color)`

**Returns:** `void`

Adds or replaces the color at the supplied designation

##### `Unset(Designation index)`

**Returns:** `void`

Removes the color at the supplied designation

##### `Get(Designation index)`

**Returns:** `C_`

Returns the color at the given designation. Returns the color at the given designation.

##### `Get(index)`

**Returns:** `return`

Returns the color at the given designation.

##### `Get(index)`

**Returns:** `return`

Returns the color at the given designation.

##### `Has(Designation index)`

**Returns:** `bool`

Returns if the color at the given designation exists.

##### `begin(—)`

**Returns:** `auto`

For iteration

##### `begin(—)`

**Returns:** `auto`

For iteration

##### `end(—)`

**Returns:** `auto`

For iteration

##### `end(—)`

**Returns:** `auto`

For iteration


---

## Enums

### `ColorMode`

**Namespace:** `Gorgon`

Color modes for images


### `Designation`

**Namespace:** `Color`

Constants for color designations. Often named colors are used in pairs of background and foreground colors.


---

## Functions

### `hexchartoint(char c)`

**Returns:** `int`



### `if(color[0] == '#')`

**Returns:** ``



### `if(color[0] == '0')`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `if(color[0] == '#')`

**Returns:** ``



### `if(color[0] == '0')`

**Returns:** ``



### `if(color[0] == '(')`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `ss(color)`

**Returns:** `std::stringstream`



### `catch(...)`

**Returns:** ``



### `GetNamedColor(std::string name)`

**Returns:** `Gorgon::Graphics::RGBA`



### `GetChannelsPerPixel(ColorMode mode)`

**Returns:** `inline unsigned long`


This is used to mark invalid color data This is used by some functions to mark color mode should be determined automatically 24bit red, green, blue color mode that has red component in the lowest byte order 24bit red, green, blue color mode that has blue component in the lowest byte order 8bit gray scale color mode 8bit alpha only color mode 32bit red, green, blue and alpha channel image. Red component is in the lowest byte order and 32bit red, green, blue and alpha channel image. Blue component is in the lowest byte order and alpha is in the highest byte order. 16bit gray scale image color mode with an alpha channel. Alpha channel is in the high byte Returns bytes per pixel for the given color mode


### `switch(mode)`

**Returns:** ``



### `HasAlpha(ColorMode mode)`

**Returns:** `inline bool`


Returns if the given color mode has alpha channel


### `GetAlphaIndex(ColorMode mode)`

**Returns:** `inline int`


Returns the index of alpha channel. If alpha channel does not exists, this function returns -1.


### `switch(mode)`

**Returns:** ``



### `Blend(RGBA first, const RGBA &second)`

**Returns:** `inline RGBA`


Red channel Green channel Blue channel Alpha channel Prints the given color to the stream Reads a color from the stream. This color can either be in full HTML format with # in front or a hex representation of the color with an optional 0x in front. Blends two colors together, you do not need to use namespace if calling on an RGBA object


### `Blend(RGBA first, const RGBA &second, float alpha)`

**Returns:** `inline RGBA`


Blends two colors together, you do not need to use namespace if calling on an RGBA object


### `GetNamedColor(std::string name)`

**Returns:** `Gorgon::Graphics::RGBA`


Returns the list of all named colors Returns the color of a named color. Returns transparent if the color does not exist.

