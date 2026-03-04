# Image

> Auto-generated documentation for the **Image** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `basic_Image`

**Namespace:** `Containers`

This class is a container for image data. It supports different color modes and access to the underlying data through () operator. This object implements move semantics. Since copy constructor is expensive, it is deleted against accidental use. If a copy of the object is required, use Duplicate function. TODO Separate non-rgba related images, export/import with rgbaf

#### Methods

##### `basic_Image(—)`

**Returns:** ``

Constructs an empty image data

##### `Swap(data)`

**Returns:** ``

Constructs a new image data with the given width, height and color mode. This constructor does not initialize data inside the image Copy constructor is disabled Move constructor

##### `Destroy(—)`

**Returns:** ``

Copy assignment is disabled Move assignment

##### `Swap(other)`

**Returns:** ``

##### `Destroy(—)`

**Returns:** ``

Destructor

##### `Duplicate(—)`

**Returns:** `basic_Image`

Duplicates this image, essentially performing the work of copy constructor

##### `Resize(const Geometry::Size &size, Graphics::ColorMode mode)`

**Returns:** `void`

Resizes the image to the given size and color mode. This function discards the contents of the image and does not perform any initialization.

##### `if(data)`

**Returns:** ``

##### `free(data)`

**Returns:** ``

##### `Assign(Byte *newdata, const Geometry::Size &size, Graphics::ColorMode mode)`

**Returns:** `void`

Assigns the image to the copy of the given data. Ownership of the given data is not transferred. If the given data is not required elsewhere, consider using Assume function. This variant performs resize and copy at the same time. The given data should have the size of width*height*Graphics::GetBytesPerPixel(mode)*sizeof(T_). This function does not perform any checks for the data size while copying it. If width or height is 0, the newdata is not accessed and this method effectively Destroys the current image. In this case, both width and height should be specified as 0.

##### `if(data && data!=newdata)`

**Returns:** ``

##### `free(data)`

**Returns:** ``

##### `Assign(Byte *newdata)`

**Returns:** `void`

Assigns the image to the copy of the given data. Ownership of the given data is not transferred. If the given data is not required elsewhere, consider using Assume function. The size and color mode of the image stays the same. The given data should have the size of width*height*Graphics::GetBytesPerPixel(mode)*sizeof(T_). This function does not perform any checks for the data size while copying it.t

##### `Assume(Byte *newdata, const Geometry::Size &size, Graphics::ColorMode mode)`

**Returns:** `void`

Assumes the ownership of the given data. This variant changes the size and color mode of the image. The given data should have the size of width*height*Graphics::GetBytesPerPixel(mode)*sizeof(T_). This function does not perform any checks for the data size while assuming it. newdata could be nullptr however, in this case width, height should be 0. mode is not assumed to be ColorMode::Invalid while the image is empty, therefore it could be specified as any value.

##### `if(data && data!=newdata)`

**Returns:** ``

##### `free(data)`

**Returns:** ``

##### `Assume(Byte *newdata)`

**Returns:** `void`

Assumes the ownership of the given data. The size and color mode of the image stays the same. The given data should have the size of width*height*Graphics::GetBytesPerPixel(mode)*sizeof(T_). This function does not perform any checks for the data size while assuming it.

##### `if(data && data!=newdata)`

**Returns:** ``

##### `free(data)`

**Returns:** ``

##### `Destroy(—)`

**Returns:** ``

Returns and disowns the current data buffer. If image is empty, this method will return a nullptr.

##### `Clear(—)`

**Returns:** `void`

Cleans the contents of the buffer by setting every byte it contains to 0.

##### `if(!data)`

**Returns:** ``

##### `Destroy(—)`

**Returns:** `void`

Destroys this image by setting width and height to 0 and freeing the memory used by its data. Also color mode is set to ColorMode::Invalid

##### `if(data)`

**Returns:** ``

##### `free(data)`

**Returns:** ``

##### `Swap(basic_Image &other)`

**Returns:** `void`

Swaps this image with another. This function is used to implement move semantics.

##### `swap(data, other.data)`

**Returns:** ``

##### `swap(size, other.size)`

**Returns:** ``

##### `swap(mode, other.mode)`

**Returns:** ``

##### `swap(cpp, other.cpp)`

**Returns:** ``

##### `swap(alphaloc, other.alphaloc)`

**Returns:** ``

##### `ConvertToRGBA(—)`

**Returns:** `void`

Returns the raw data pointer Returns the raw data pointer Converts this image data to RGBA buffer

##### `switch(mode)`

**Returns:** ``

##### `for(int i=0; i<size.Area()`

**Returns:** ``

##### `for(int i=0; i<size.Area()`

**Returns:** ``

##### `for(int i=0; i<size.Area()`

**Returns:** ``

##### `for(int i=0; i<size.Area()`

**Returns:** ``

##### `for(int i=0; i<size.Area()`

**Returns:** ``

##### `for(int i=0; i<size.Area()`

**Returns:** ``

##### `CopyTo(basic_Image &dest, Geometry::Point target = {0, 0})`

**Returns:** `bool`

Copies data from one image to another. This operation does not perform blending. Additionally, color modes should be the same. However, this function will do clipping for overflows. Do not use negative values for target. Will return false if nothing is copied.

##### `for(int y=0; y<GetHeight()`

**Returns:** ``

##### `memcpy(dd + di, sd + si, cs)`

**Returns:** ``

##### `CopyTo(basic_Image &dest, Geometry::Bounds source, Geometry::Point target = {0, 0})`

**Returns:** `bool`

Copies data from one image to another. This operation does not perform blending. Additionally, color modes should be the same. However, this function will do clipping. Source bounds should be within the image. Will return false if nothing is copied.

##### `if(target.X < 0)`

**Returns:** ``

##### `if(target.Y < 0)`

**Returns:** ``

##### `for(int y=source.Top; y<source.Bottom; y++)`

**Returns:** ``

##### `memcpy(dd + di, sd + si, cs)`

**Returns:** ``

##### `CopyToRGBABuffer(Byte *buffer)`

**Returns:** `void`

Copies this image to a RGBA buffer, buffer should be resize before calling this function

##### `switch(mode)`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `CopyToBGRABuffer(Byte *buffer)`

**Returns:** `void`

Copies this image to a RGBA buffer, buffer should be resize before calling this function. This function is here mostly to create icon for Win32

##### `switch(mode)`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `CopyToBGRABufferLong(unsigned long *buffer)`

**Returns:** `void`

Copies this image to a RGBA buffer, buffer should be resize before calling this function. This function is here mostly to create icon for X11

##### `switch(mode)`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `for(i=0; i<size.Area()`

**Returns:** ``

##### `ShrinkMultiple(const Geometry::Size& factor)`

**Returns:** `basic_Image`

Shrinks the size of the image using integer area interpolation.

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(int yy=ys; yy<th; yy++)`

**Returns:** ``

##### `for(int xx=xs; xx<tw; xx++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `Scale(const Geometry::Size &newsize, InterpolationMethod method = InterpolationMethod::Cubic)`

**Returns:** `basic_Image`

Scales this image to the given size. In the image is shrunk more than 2x its original size Area interpolation is used along with the specified interpolation method.

##### `if(fx > 2 || fy > 2)`

**Returns:** ``

##### `if(method == InterpolationMethod::NearestNeighbor)`

**Returns:** ``

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `if(method == InterpolationMethod::Linear)`

**Returns:** `else`

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `if(method == InterpolationMethod::Cubic)`

**Returns:** `else`

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `if(i == 1 || i == 2)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `if(i == 1 || i == 2)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `for(int j=0; j<4; j++)`

**Returns:** ``

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `Rotate(Float angle, InterpolationMethod method = InterpolationMethod::Cubic)`

**Returns:** `basic_Image`

Rotates this image with the given angle.

##### `Rotate(angle, {size.Width/2.f, size.Height/2.f}, method)`

**Returns:** `return`

##### `Rotate(Float angle, const Geometry::Pointf origin, InterpolationMethod method = InterpolationMethod::Cubic)`

**Returns:** `basic_Image`

Rotates this image with the given angle.

##### `if(method == InterpolationMethod::NearestNeighbor)`

**Returns:** ``

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `if(method == InterpolationMethod::Linear)`

**Returns:** `else`

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `if(method == InterpolationMethod::Cubic)`

**Returns:** `else`

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `if(i == 1 || i == 2)`

**Returns:** ``

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `if(i == 1 || i == 2)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `for(int j=0; j<4; j++)`

**Returns:** ``

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `SkewX(Float perpixel, InterpolationMethod method = InterpolationMethod::Cubic)`

**Returns:** `basic_Image`

Rotates this image with the given angle.

##### `SkewX(perpixel, {0.f, 0.f}, method)`

**Returns:** `return`

##### `SkewX(Float perpixel, const Geometry::Pointf origin, InterpolationMethod method = InterpolationMethod::Cubic)`

**Returns:** `basic_Image`

Rotates this image with the given angle.

##### `if(method == InterpolationMethod::NearestNeighbor)`

**Returns:** ``

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `if(method == InterpolationMethod::Linear)`

**Returns:** `else`

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `if(method == InterpolationMethod::Cubic)`

**Returns:** `else`

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `if(i == 1 || i == 2)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `SkewY(Float perpixel, InterpolationMethod method = InterpolationMethod::Cubic)`

**Returns:** `basic_Image`

Rotates this image with the given angle.

##### `SkewY(perpixel, {0.f, 0.f}, method)`

**Returns:** `return`

##### `SkewY(Float perpixel, const Geometry::Pointf origin, InterpolationMethod method = InterpolationMethod::Cubic)`

**Returns:** `basic_Image`

Rotates this image with the given angle.

##### `if(method == InterpolationMethod::NearestNeighbor)`

**Returns:** ``

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `if(method == InterpolationMethod::Linear)`

**Returns:** `else`

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `if(method == InterpolationMethod::Cubic)`

**Returns:** `else`

##### `for(int x=0; x<newsize.Width; x++)`

**Returns:** ``

##### `for(int y=0; y<newsize.Height; y++)`

**Returns:** ``

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `if(i == 1 || i == 2)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `MirrorX(—)`

**Returns:** `basic_Image`

Mirrors this bitmap along X axis as a new one.

##### `for(int y=0; y<size.Height; y++)`

**Returns:** ``

##### `for(int x=0; x<size.Width; x++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `MirrorY(—)`

**Returns:** `basic_Image`

Mirrors this bitmap along Y axis as a new one.

##### `for(int x=0; x<size.Width; x++)`

**Returns:** ``

##### `for(int y=0; y<size.Height; y++)`

**Returns:** ``

##### `for(unsigned c=0; c<cpp; c++)`

**Returns:** ``

##### `FlipX(—)`

**Returns:** `basic_Image`

Flips this bitmap along X axis as a new one.

##### `MirrorY(—)`

**Returns:** `return`

##### `FlipY(—)`

**Returns:** `basic_Image`

Flips this bitmap along Y axis as a new one.

##### `MirrorX(—)`

**Returns:** `return`

##### `ImportBMP(const std::string &filename, bool dib = false)`

**Returns:** `bool`

Imports a given bitmap file. BMP RLE compression and colorspaces are not supported.

##### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`

##### `ImportBMP(file, dib)`

**Returns:** `return`

##### `ImportBMP(std::istream &file, bool dib = false)`

**Returns:** `bool`

Imports a given bitmap file. BMP RLE compression and colorspaces are not supported.

##### `if(!dib)`

**Returns:** ``

##### `ReadUInt16(file)`

**Returns:** ``

##### `ReadUInt16(file)`

**Returns:** ``

##### `while(v)`

**Returns:** ``

##### `if(headersize == 12)`

**Returns:** ``

##### `ReadUInt16(file)`

**Returns:** ``

##### `if(headersize >= 40)`

**Returns:** ``

##### `ReadUInt16(file)`

**Returns:** ``

##### `ReadUInt32(file)`

**Returns:** ``

##### `ReadInt32(file)`

**Returns:** ``

##### `ReadInt32(file)`

**Returns:** ``

##### `ReadUInt32(file)`

**Returns:** ``

##### `if(bitcompress && headersize == 40)`

**Returns:** ``

##### `if(bpp == 16)`

**Returns:** `else`

##### `if(bpp == 32)`

**Returns:** `else`

##### `if(headersize >= 108)`

**Returns:** ``

##### `if(redmask)`

**Returns:** ``

##### `if(greenmask)`

**Returns:** ``

##### `if(bluemask)`

**Returns:** ``

##### `if(alphamask)`

**Returns:** ``

##### `if(headersize > 108)`

**Returns:** ``

##### `if(bpp <= 8)`

**Returns:** ``

##### `for(int i=0; i<colorsused; i++)`

**Returns:** ``

##### `if(headersize > 12)`

**Returns:** ``

##### `for(int i=0; i<colorsused; i++)`

**Returns:** ``

##### `if(palette[i].A)`

**Returns:** ``

##### `Resize({width, height}, Graphics::ColorMode::RGBA)`

**Returns:** ``

##### `if(bpp <= 8 && grayscalepalette)`

**Returns:** `else`

##### `Resize({width, height}, Graphics::ColorMode::Grayscale_Alpha)`

**Returns:** ``

##### `Resize({width, height}, Graphics::ColorMode::Grayscale)`

**Returns:** ``

##### `if(alpha)`

**Returns:** `else`

##### `if(redmask == 0 && greenmask == 0 && bluemask == 0)`

**Returns:** ``

##### `Resize({width, height}, Graphics::ColorMode::Alpha)`

**Returns:** ``

##### `Resize({width, height}, Graphics::ColorMode::RGBA)`

**Returns:** ``

##### `Resize({width, height}, Graphics::ColorMode::RGB)`

**Returns:** ``

##### `if(upsidedown)`

**Returns:** ``

##### `if(bpp == 24)`

**Returns:** ``

##### `for(int y = ys; y!=ye; y += yc)`

**Returns:** ``

##### `for(int x=0; x<width; x++)`

**Returns:** ``

##### `if(bytes%4)`

**Returns:** ``

##### `if(bpp == 16 || bpp == 32)`

**Returns:** `else`

##### `for(int y = ys; y!=ye; y += yc)`

**Returns:** ``

##### `for(int x=0; x<width; x++)`

**Returns:** ``

##### `if(redmask != 0 || greenmask != 0 || bluemask != 0)`

**Returns:** ``

##### `if(alpha)`

**Returns:** ``

##### `if(redmask != 0 || greenmask != 0 || bluemask != 0)`

**Returns:** ``

##### `if(bytes%4)`

**Returns:** ``

##### `if(bpp < 8)`

**Returns:** `else`

##### `for(int y = ys; y!=ye; y += yc)`

**Returns:** ``

##### `for(int x=0; x<width; x++)`

**Returns:** ``

##### `if(bits == 0)`

**Returns:** ``

##### `if(grayscalepalette)`

**Returns:** ``

##### `if(alpha)`

**Returns:** ``

##### `if(bytes%4)`

**Returns:** ``

##### `ExportBMP(const std::string &filename, bool usev4 = false, bool dib = false)`

**Returns:** `bool`

Exports the image as a bitmap. RGB is exported as 24-bit, RGBA, BGR, BGRA is exported as 32-bit, Grayscale exported as 8-bit, Grayscale alpha, alpha only is exported as 16-bit

##### `file(filename, std::ios::binary)`

**Returns:** `std::ofstream`

##### `ExportBMP(file, usev4, dib)`

**Returns:** `return`

##### `ExportBMP(std::ostream &file, bool usev4 = false, bool dib = false)`

**Returns:** `bool`

Exports the image as a bitmap. RGB is exported as 24-bit, RGBA, BGR, BGRA is exported as 32-bit, Grayscale exported as 8-bit, Grayscale alpha, alpha only is exported as 16-bit

##### `switch(mode)`

**Returns:** ``

##### `if(!dib)`

**Returns:** ``

##### `WriteString(file, "BM")`

**Returns:** ``

##### `WriteUInt32(file, 14 + headersize + extraspace + datasize)`

**Returns:** ``

##### `WriteUInt16(file, 0)`

**Returns:** ``

##### `WriteUInt16(file, 0)`

**Returns:** ``

##### `WriteUInt32(file, 14 + headersize + extraspace)`

**Returns:** ``

##### `WriteUInt32(file, headersize)`

**Returns:** ``

##### `WriteInt32(file, size.Width)`

**Returns:** ``

##### `WriteInt32(file, size.Height)`

**Returns:** ``

##### `WriteUInt16(file, 1)`

**Returns:** ``

##### `WriteUInt16(file, bpp)`

**Returns:** ``

##### `WriteUInt32(file, compression)`

**Returns:** ``

##### `WriteUInt32(file, datasize)`

**Returns:** ``

##### `WriteInt32(file, 2834)`

**Returns:** ``

##### `WriteInt32(file, 2834)`

**Returns:** ``

##### `WriteInt32(file, 0)`

**Returns:** ``

##### `WriteInt32(file, 0)`

**Returns:** ``

##### `if(compression == 3)`

**Returns:** ``

##### `if(mode == ColorMode::Alpha)`

**Returns:** ``

##### `WriteUInt32(file, 0x00000001)`

**Returns:** ``

##### `WriteUInt32(file, 0x00000002)`

**Returns:** ``

##### `WriteUInt32(file, 0x00000004)`

**Returns:** ``

##### `if(mode == ColorMode::BGRA)`

**Returns:** `else`

##### `WriteUInt32(file, 0x00ff0000)`

**Returns:** ``

##### `WriteUInt32(file, 0x0000ff00)`

**Returns:** ``

##### `WriteUInt32(file, 0x000000ff)`

**Returns:** ``

##### `WriteUInt32(file, 0x000000ff)`

**Returns:** ``

##### `WriteUInt32(file, 0x0000ff00)`

**Returns:** ``

##### `WriteUInt32(file, 0x00ff0000)`

**Returns:** ``

##### `if(headersize == 108 || usev4)`

**Returns:** ``

##### `if(compression != 3)`

**Returns:** ``

##### `WriteUInt32(file, 0x00000001)`

**Returns:** ``

##### `WriteUInt32(file, 0x00000002)`

**Returns:** ``

##### `WriteUInt32(file, 0x00000004)`

**Returns:** ``

##### `if(mode == ColorMode::Alpha)`

**Returns:** ``

##### `WriteUInt32(file, 0x0000ff00)`

**Returns:** ``

##### `WriteUInt32(file, 0xff000000)`

**Returns:** ``

##### `WriteUInt32(file, 1)`

**Returns:** ``

##### `WriteUInt32(file, 0)`

**Returns:** ``

##### `switch(mode)`

**Returns:** ``

##### `for(int y=size.Height-1; y>=0; y--)`

**Returns:** ``

##### `WriteArray(file, data+y*ostride, ostride)`

**Returns:** ``

##### `WriteUInt8(file, 0)`

**Returns:** ``

##### `for(int y=size.Height-1; y>=0; y--)`

**Returns:** ``

##### `WriteArray(file, data+y*ostride, ostride)`

**Returns:** ``

##### `WriteUInt8(file, 0)`

**Returns:** ``

##### `for(int y=size.Height-1; y>=0; y--)`

**Returns:** ``

##### `WriteArray(file, data+y*ostride, ostride)`

**Returns:** ``

##### `for(int i=0; i<256; i++)`

**Returns:** ``

##### `WriteUInt8(file, 0)`

**Returns:** ``

##### `for(int y=size.Height-1; y>=0; y--)`

**Returns:** ``

##### `WriteArray(file, data+y*ostride, ostride)`

**Returns:** ``

##### `WriteUInt8(file, 0)`

**Returns:** ``

##### `for(int y=size.Height-1; y>=0; y--)`

**Returns:** ``

##### `for(int x=0; x<size.Width; x++)`

**Returns:** ``

##### `WriteUInt8(file, data[y*ostride+x*2])`

**Returns:** ``

##### `WriteUInt8(file, data[y*ostride+x*2])`

**Returns:** ``

##### `WriteUInt8(file, data[y*ostride+x*2])`

**Returns:** ``

##### `WriteUInt8(file, data[y*ostride+x*2+1])`

**Returns:** ``

##### `for(int y=size.Height-1; y>=0; y--)`

**Returns:** ``

##### `for(int x=0; x<size.Width; x++)`

**Returns:** ``

##### `WriteUInt8(file, 0xff)`

**Returns:** ``

##### `WriteUInt8(file, data[y*ostride+x])`

**Returns:** ``

##### `WriteUInt8(file, 0)`

**Returns:** ``

##### `if(p.X<0 || p.Y<0 || p.X>=size.Width || p.Y>=size.Height || component>=cpp)`

**Returns:** ``

Provides access to the given component in x and y coordinates. This function performs bounds checking only on debug mode.

##### `if(p.X<0 || p.Y<0 || p.X>=size.Width || p.Y>=size.Height || component>=cpp)`

**Returns:** ``

Provides access to the given component in x and y coordinates. This function performs bounds checking only on debug mode.

##### `Get(const Geometry::Point &p, unsigned component = 0)`

**Returns:** `Byte`

Provides access to the given component in x and y coordinates. This function returns 0 if the given coordinates are out of bounds. This function works slower than the () operator.

##### `if(p.X < 0 || p.Y < 0 || p.X >= size.Width || p.Y >= size.Height || component >= cpp)`

**Returns:** ``

##### `Get(const Geometry::Point &p, Byte def, unsigned component = 0)`

**Returns:** `Byte`

Provides access to the given component in x and y coordinates. This function returns 0 if the given coordinates are out of bounds. This function works slower than the () operator.

##### `if(p.X < 0 || p.Y < 0 || p.X >= size.Width || p.Y >= size.Height || component >= cpp)`

**Returns:** ``

##### `if(x<0 || y<0 || x>=size.Width || y>=size.Height || component>=cpp)`

**Returns:** ``

Provides access to the given component in x and y coordinates. This function performs bounds checking only on debug mode.

##### `if(x<0 || y<0 || x>=size.Width || y>=size.Height || component>=cpp)`

**Returns:** ``

Provides access to the given component in x and y coordinates. This function performs bounds checking only on debug mode.

##### `Get(int x, int y, unsigned component=0)`

**Returns:** `Byte`

Provides access to the given component in x and y coordinates. This function returns 0 if the given coordinates are out of bounds. This function works slower than the () operator.

##### `if(x<0 || y<0 || x>=size.Width || y>=size.Height || component>=cpp)`

**Returns:** ``

##### `GetAlphaAt(int x, int y)`

**Returns:** `Byte`

Returns the alpha at the given location. If the given location does not exits this function will return 0. If there is no alpha channel, image is assumed to be opaque.

##### `if(x<0 || y<0 || x>=size.Width || y>=size.Height)`

**Returns:** ``

##### `GetRGBAAt(int x, int y)`

**Returns:** `Graphics::RGBA`

Returns the alpha at the given location. If the given location does not exits this function will return 0. If there is no alpha channel, image is assumed to be opaque.

##### `if(x<0 || y<0 || x>=size.Width || y>=size.Height)`

**Returns:** ``

##### `switch(mode)`

**Returns:** ``

##### `GetRGBAAt(Geometry::Point p)`

**Returns:** `Graphics::RGBA`

Returns the alpha at the given location. If the given location does not exits this function will return 0. If there is no alpha channel, image is assumed to be opaque.

##### `GetRGBAAt(p.X, p.Y)`

**Returns:** `return`

##### `SetRGBAAt(int x, int y, Graphics::RGBA color)`

**Returns:** `void`

Sets the color at the given location to the specified RGBA value. If pixel does not exists, the call will be ignored.

##### `if(x<0 || y<0 || x>=size.Width || y>=size.Height)`

**Returns:** ``

##### `switch(mode)`

**Returns:** ``

##### `SetRGBAAt(Geometry::Point p, Graphics::RGBA color)`

**Returns:** `void`

Sets the color at the given location to the specified RGBA value. If pixel does not exists, the call will be ignored.

##### `SetRGBAAt(p.X, p.Y, color)`

**Returns:** ``

##### `GetSize(—)`

**Returns:** `Geometry::Size`

Returns the size of the image

##### `GetWidth(—)`

**Returns:** `int`

Returns the width of the image

##### `GetHeight(—)`

**Returns:** `int`

Returns the height of the image

##### `GetTotalSize(—)`

**Returns:** `unsigned long`

Total size of this image in number units

##### `GetMode(—)`

**Returns:** `Graphics::ColorMode`

Returns the color mode of the image

##### `ChangeMode(Graphics::ColorMode value)`

**Returns:** `void`

Changes the color mode of the image. Only works if the bits/pixel of the target mode is the same as the original

##### `GetChannelsPerPixel(—)`

**Returns:** `unsigned`

Returns the number units occupied by a single pixel of this image

##### `HasAlpha(—)`

**Returns:** `bool`

Returns if this image has alpha channel

##### `GetAlphaIndex(—)`

**Returns:** `int`

Returns the index of alpha channel. Value of -1 denotes no alpha channel


---

## Enums

### `InterpolationMethod`

**Namespace:** `Containers`


---

## Functions

### `Fix(float val)`

**Returns:** `static T_`



### `Fix(float val)`

**Returns:** `static float`



### `swap(basic_Image<T_> &l, basic_Image<T_> &r)`

**Returns:** `inline void`


Data that stores pixels of the image Width of the image Color mode of the image Channels per pixel information Location of the alpha channel, -1 means it does not exits Compares two images. Images are equal if their size, mode and contents are the same Compares two images. Images are equal if their size, mode and contents are not the same Swaps two images. Should be used unqualified for ADL.


### `if(reader)`

**Returns:** ``



### `if(ret && isloaded)`

**Returns:** ``



### `loaded()`

**Returns:** ``



### `while(!target)`

**Returns:** ``



### `if(gid==GID::Image_Props)`

**Returns:** ``



### `if(!load)`

**Returns:** ``



### `if(gid==GID::Image_Data)`

**Returns:** `else`



### `if(load)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `if(gid==GID::Image_Cmp_Data)`

**Returns:** `else`



### `if(load)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `if(compression==GID::PNG)`

**Returns:** ``



### `LoadError(LoadError::Unknown, "Unknown compression type.")`

**Returns:** `throw`



### `if(gid==GID::Image_Cmp_Props)`

**Returns:** `else`



### `if(size>4)`

**Returns:** ``



### `LoadError(LoadError::VersionMismatch, "Old version image compression")`

**Returns:** `throw`



### `ASSERT(data, "Image data does not exists")`

**Returns:** ``



### `if(compression==GID::None)`

**Returns:** ``



### `if(compression==GID::PNG)`

**Returns:** `else`



### `if(img)`

**Returns:** ``



### `if(compress)`

**Returns:** ``



### `Image(Graphics::Bitmap &&source)`

**Returns:** ``


This resource contains images. It allows draw, load, import, export functionality. An image resource may work without its data buffer. In order to be drawn, an image object should be prepared. Both data and texture might be released from the image resource. This allows safe destruction of the file tree without destroying the necessary information. Assumes the given bitmap and converts it to a resource.


### `Swap(source)`

**Returns:** ``



### `SetCompression(GID::Type compression)`

**Returns:** `void`


Changes the compression mode. It only works if this image is saved along with a file. Currently only GID::None and GID::PNG works.


### `GetCompression()`

**Returns:** `GID::Type`


Returns the compression mode of this image resource


### `MoveOutAsBitmap()`

**Returns:** `Graphics::Bitmap`


Moves the data out of resource system. Use Prepare and Discard before moving to avoid data duplication


### `Load()`

**Returns:** `bool`


Loads the image from the disk. This function requires image to be tied to a resource file.


### `IsLoaded()`

**Returns:** `bool`


Returns whether the image data is loaded. Data loading is a valid information in only resource context. If this image is created manually, it is always considered loaded even if no data is set for it.


### `SaveThis(Writer &writer, const Graphics::Bitmap &bmp, GID::Type type = GID::Image)`

**Returns:** `static void`


This function loads a image resource from the given file This function can be used to save a bitmap as image resource without modifying it. If given bitmap is a resource save function of that resource is used instead. If the area of the bitmap is greater than 400 pixel it will be saved as PNG.


### `load(std::shared_ptr<Reader> reader, unsigned long size, bool forceload)`

**Returns:** `bool`


Loads the image from the data stream


### `loaded()`

**Returns:** `void`


