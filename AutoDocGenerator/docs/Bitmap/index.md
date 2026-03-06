# Bitmap

&gt; Auto-generated documentation for the **Bitmap** module of the Gorgon C++ Game Engine.


## Contents

- [Enums](#enums)
- [Functions](#functions)

---

## Enums

### `AtlasMargin`

**Namespace:** `Gorgon`


### `GrayscaleConversionMethod`

**Namespace:** `Gorgon`

Atlas will be tight packed If there is transparency, transparent, otherwise black borders Repeats the last pixel Wraps to the other side


---

## Functions

### `if(data)`

**Returns:** ``



### `if(dotpos!=-1)`

**Returns:** ``



### `ImportPNG(filename)`

**Returns:** `return`



### `ImportJPEG(filename)`

**Returns:** `return`



### `ImportBMP(filename)`

**Returns:** `return`



### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `if(sig == pngsig)`

**Returns:** ``



### `ImportPNG(filename)`

**Returns:** `return`



### `if(sig == jpgsig1 || sig == jpgsig2)`

**Returns:** `else`



### `ImportJPEG(filename)`

**Returns:** `return`



### `ImportBMP(filename)`

**Returns:** `return`



### `if(sig == pngsig)`

**Returns:** ``



### `ImportPNG(file)`

**Returns:** `return`



### `if(sig == jpgsig1 || sig == jpgsig2)`

**Returns:** `else`



### `ImportJPEG(file)`

**Returns:** `return`



### `ImportBMP(file)`

**Returns:** `return`



### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `Destroy()`

**Returns:** ``



### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `Destroy()`

**Returns:** ``



### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `Destroy()`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `if(dotpos!=-1)`

**Returns:** ``



### `ExportPNG(filename)`

**Returns:** `return`



### `ExportJPEG(filename)`

**Returns:** `return`



### `ExportBMP(filename)`

**Returns:** `return`



### `ASSERT(data, "Image data does not exists")`

**Returns:** ``



### `file(filename, std::ios::binary)`

**Returns:** `std::ofstream`



### `ASSERT(data, "Image data does not exists")`

**Returns:** ``



### `ASSERT(data, "Image data does not exists")`

**Returns:** ``



### `ASSERT(data, "Image data does not exists")`

**Returns:** ``



### `ASSERT(data, "Image data does not exists")`

**Returns:** ``



### `file(filename, std::ios::binary)`

**Returns:** `std::ofstream`



### `ASSERT(data, "Image data does not exists")`

**Returns:** ``



### `for(int y=0; y<data.GetHeight()`

**Returns:** ``



### `for(int x=0; x<data.GetWidth()`

**Returns:** ``



### `for(int y=0; y<data.GetHeight()`

**Returns:** ``



### `for(int x=0; x<data.GetWidth()`

**Returns:** ``



### `if(c!=alpha)`

**Returns:** ``



### `if(ratio == 1)`

**Returns:** ``



### `if(mode == ColorMode::RGBA || mode == ColorMode::BGRA)`

**Returns:** ``



### `if(mode == ColorMode::RGB || mode == ColorMode::BGR)`

**Returns:** `else`



### `if(mode == ColorMode::Grayscale || mode == ColorMode::Grayscale_Alpha)`

**Returns:** `else`



### `if(mode == ColorMode::Alpha)`

**Returns:** `else`



### `if(mode == ColorMode::RGB || mode == ColorMode::RGBA)`

**Returns:** ``



### `if(method == Luminance)`

**Returns:** ``



### `for(int y=0; y<data.GetHeight()`

**Returns:** ``



### `for(int x=0; x<data.GetWidth()`

**Returns:** ``



### `if(ratio == 1)`

**Returns:** ``



### `setcolor(x, y, c)`

**Returns:** ``



### `if(margins == Zero)`

**Returns:** ``



### `for(auto &bmp : list)`

**Returns:** ``



### `if(margins == Zero)`

**Returns:** ``



### `for(int i=0; i<N; i++)`

**Returns:** ``



### `if(w - x > minw)`

**Returns:** ``



### `for(auto it = list.Last()`

**Returns:** ``



### `if(size.Width <= maxw)`

**Returns:** ``



### `if(!found)`

**Returns:** ``



### `if(x)`

**Returns:** ``



### `Resize({maxx, y + marginwidth}, mode)`

**Returns:** ``



### `if(margins == Zero)`

**Returns:** ``



### `for(auto p : mapping)`

**Returns:** ``



### `for(int y=0; y<b.Height()`

**Returns:** ``



### `for(int x=0; x<b.Width()`

**Returns:** ``



### `for(int c=0; c<C; c++)`

**Returns:** ``



### `for(int i=0; i<N; i++)`

**Returns:** ``



### `for(int y{ outer_margin.Y }; y <= H - size.Height - outer_margin.Y; y += size.Height + margin.Y)`

**Returns:** ``



### `for(int x{ outer_margin.X }; x <= W - size.Width - outer_margin.X; x += size.Width + margin.X)`

**Returns:** ``



### `GenerateAtlasBounds(Geometry::Size{size, size}, Geometry::Point {margin, margin}, Geometry::Point{outer_margin, outer_margin})`

**Returns:** `return`



### `GenerateAtlasBounds(size, Geometry::Point {margin, margin}, Geometry::Point{outer_margin, outer_margin})`

**Returns:** `return`



### `GenerateAtlasBounds(Geometry::Size{size, size}, margin, outer_margin)`

**Returns:** `return`



### `for(auto b : boundaries)`

**Returns:** ``



### `ASSERT(data, "Image data does not exists")`

**Returns:** ``



### `ASSERT(data, "Image data does not exists")`

**Returns:** ``



### `ret(0, 0, 0, 0)`

**Returns:** `Geometry::Margin`



### `if(left)`

**Returns:** ``



### `for(int x=bounds.Left; x<bounds.Right; x++)`

**Returns:** ``



### `for(int y=bounds.Top; y<bounds.Bottom; y++)`

**Returns:** ``



### `if(empty)`

**Returns:** ``



### `if(top)`

**Returns:** ``



### `for(int y=bounds.Top; y<bounds.Bottom; y++)`

**Returns:** ``



### `for(int x=bounds.Left; x<bounds.Right; x++)`

**Returns:** ``



### `if(empty)`

**Returns:** ``



### `if(right)`

**Returns:** ``



### `for(int x=bounds.Right-1; x>=bounds.Left; x--)`

**Returns:** ``



### `for(int y=bounds.Top; y<bounds.Bottom; y++)`

**Returns:** ``



### `if(empty)`

**Returns:** ``



### `if(bottom)`

**Returns:** ``



### `for(int y=bounds.Bottom-1; y>=bounds.Top; y--)`

**Returns:** ``



### `for(int x=bounds.Left; x<bounds.Right; x++)`

**Returns:** ``



### `if(empty)`

**Returns:** ``



### `if(data==nullptr)`

**Returns:** ``



### `ASSERT_DUMP(false, "No data to release")`

**Returns:** ``



### `for(int y=bounds.Top; y<bounds.Bottom; y++)`

**Returns:** ``



### `for(int x=bounds.Left; x<bounds.Right; x++)`

**Returns:** ``



### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `ForAllPixels([&](int x, int y, int c)`

**Returns:** ``



### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `ForAllPixels([&](int x, int y, int c)`

**Returns:** ``



### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `ForAllPixels([&](int x, int y, int c)`

**Returns:** ``



### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `Bitmap()`

**Returns:** ``


Default constructor will create an empty bitmap


### `data(new Containers::Image{size, mode})`

**Returns:** ``


Creates an uninitialized image of the given size and color mode. Prepare function should be called to be able to draw this image.


### `if(size.Width<0 || size.Height<0)`

**Returns:** ``



### `Bitmap(Bitmap &&other)`

**Returns:** ``


Copy constructor is disabled. Move constructor


### `Swap(other)`

**Returns:** ``



### `Swap(Bitmap &other)`

**Returns:** `virtual void`


Move constructor Swaps two images, mostly used for move constructor,


### `swap(data, other.data)`

**Returns:** ``



### `Discard()`

**Returns:** ``


Copy assignment is disabled Move assignment


### `Swap(other)`

**Returns:** ``



### `Duplicate()`

**Returns:** `Bitmap`


Duplicates this image. Only the data portion is duplicated. No other information is transferred to the image. Omitted information includes resource related data and texture related data. Therefore, before drawing the newly duplicated image, it should be prepared for drawing to work.


### `Destroy()`

**Returns:** `void`


Destroys the contained data, including the texture


### `ReleaseData()`

**Returns:** `Containers::Image`


Destroys image data if used as animation, this object will not be deleted Bitmap cannot be controlled Releases the image data. The image data returned by this function is moved out. Data is passed by value, thus if it is not moved into a Containers::Image, it will be destroyed.


### `ReleaseTexture()`

**Returns:** `Graphics::TextureImage`


Releases the texture held by this image. Texture is passed by value, thus if it is not moved into a Graphics::TextureImage, it will be destroyed.


### `HasData()`

**Returns:** `bool`


Checks if this image resource has a data attached to it


### `HasTexture()`

**Returns:** `bool`


Returns the data attached to this bitmap. If no data is present, this function throws Checks if this image resource has a texture attached to it.


### `Assign(const Containers::Image &image)`

**Returns:** `void`


Assigns the given image as the data of this image resource. Notice that changing data does not prepare the data to be drawn, a separate call to Prepare function is necessary


### `if(!data)`

**Returns:** ``



### `Assign(Byte *newdata, const Geometry::Size &size, Graphics::ColorMode mode)`

**Returns:** `void`


Assigns the image to the copy of the given data. Ownership of the given data is not transferred. If the given data is not required elsewhere, consider using Assume function. This variant performs resize and copy at the same time. The given data should have the size of width*height*Graphics::GetBytesPerPixel(mode)*sizeof(Byte). This function does not perform any checks for the data size while copying it. If width or height is 0, the newdata is not accessed and this method effectively Destroys the current image. In this case, both width and height should be specified as 0. Notice that changing data does not prepare the data to be drawn, a separate call to Prepare function is necessary.


### `if(!data)`

**Returns:** ``



### `Assign(Byte *newdata)`

**Returns:** `void`


Assigns the image to the copy of the given data. Ownership of the given data is not transferred. If the given data is not required elsewhere, consider using Assume function. The size and color mode of the image stays the same. The given data should have the size of width*height*Graphics::GetBytesPerPixel(mode)*sizeof(Byte). This function does not perform any checks for the data size while copying it. Notice that changing data does not prepare the data to be drawn, a separate call to Prepare function is necessary.


### `if(!data)`

**Returns:** ``



### `Assume(Containers::Image &image)`

**Returns:** `void`


Assumes the contents of the given image as image data. Notice that assuming data does not prepare the data to be drawn, a separate call to Prepare function is necessary.


### `Assume(Containers::Image &&image)`

**Returns:** `void`


Assumes the contents of the given image as image data by moving it into the bitmap buffer. Notice that assuming data does not prepare the data to be drawn, a separate call to Prepare function is necessary.


### `if(!data)`

**Returns:** ``



### `Assume(Byte *newdata, const Geometry::Size &size, Graphics::ColorMode mode)`

**Returns:** `void`


Assumes the ownership of the given data. This variant changes the size and color mode of the image. The given data should have the size of width*height*Graphics::GetBytesPerPixel(mode)*sizeof(Byte). This function does not perform any checks for the data size while assuming it. newdata could be nullptr however, in this case width, height should be 0. mode is not assumed to be ColorMode::Invalid while the image is empty, therefore it could be specified as any value. Notice that assuming data does not prepare the data to be drawn, a separate call to Prepare function is necessary.


### `if(!data)`

**Returns:** ``



### `Assume(Byte *newdata)`

**Returns:** `void`


Assumes the ownership of the given data. The size and color mode of the image stays the same. The given data should have the size of width*height*Graphics::GetBytesPerPixel(mode)*sizeof(Byte). This function does not perform any checks for the data size while assuming it. Notice that assuming data does not prepare the data to be drawn, a separate call to Prepare function is necessary.


### `if(!data)`

**Returns:** ``



### `Resize(const Geometry::Size &size, Graphics::ColorMode mode=Graphics::ColorMode::RGBA)`

**Returns:** `void`


Resizes the image to the given size and color mode. This function discards the contents of the image and does not perform any initialization.


### `if(!data)`

**Returns:** ``



### `Resize(int w, int h, Graphics::ColorMode mode=Graphics::ColorMode::RGBA)`

**Returns:** `void`


Resizes the image to the given size and color mode. This function discards the contents of the image and does not perform any initialization.


### `Resize({w, h}, mode)`

**Returns:** ``



### `ASSERT(data, "Data is not set")`

**Returns:** ``


Provides access to the given component in x and y coordinates. This function performs bounds checking only on debug mode. Notice that changing a pixel does not prepare the new data to be drawn, a separate call to Prepare function is necessary.


### `ASSERT(data, "Data is not set")`

**Returns:** ``


Provides access to the given component in x and y coordinates. This function performs bounds checking only on debug mode.


### `ASSERT(data, "Data is not set")`

**Returns:** ``


Provides access to the given component in x and y coordinates. This function performs bounds checking only on debug mode. Notice that changing a pixel does not prepare the new data to be drawn, a separate call to Prepare function is necessary.


### `ASSERT(data, "Data is not set")`

**Returns:** ``


Provides access to the given component in x and y coordinates. This function performs bounds checking only on debug mode.


### `Get(const Geometry::Point &p, unsigned component = 0)`

**Returns:** `Byte`


Provides access to the given component in x and y coordinates. This function returns 0 if the given coordinates are out of bounds. This function works slower than the () operator.


### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `Get(const Geometry::Point &p, Byte def, unsigned component)`

**Returns:** `Byte`


Provides access to the given component in x and y coordinates. This function returns 0 if the given coordinates are out of bounds. This function works slower than the () operator.


### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `GetAlphaAt(int x, int y)`

**Returns:** `Byte`


Returns the alpha at the given location. If the given location does not exits this function will return 0. If there is no alpha channel, image is assumed to be opaque.


### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `GetAlphaAt(Geometry::Point p)`

**Returns:** `Byte`


Returns the alpha at the given location. If the given location does not exits this function will return 0. If there is no alpha channel, image is assumed to be opaque.


### `GetAlphaAt(p.X, p.Y)`

**Returns:** `return`



### `GetRGBAAt(int x, int y)`

**Returns:** `RGBA`


Returns the alpha at the given location. If the given location does not exits this function will return 0. If there is no alpha channel, image is assumed to be opaque.


### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `GetRGBAAt(Geometry::Point p)`

**Returns:** `RGBA`


Returns the alpha at the given location. If the given location does not exits this function will return 0. If there is no alpha channel, image is assumed to be opaque.


### `GetRGBAAt(p.X, p.Y)`

**Returns:** `return`



### `SetRGBAAt(int x, int y, RGBA color)`

**Returns:** `void`


Sets the color at the given location to the specified RGBA value. If pixel does not exists, the call will be ignored.


### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `SetRGBAAt(Geometry::Point p, RGBA color)`

**Returns:** `void`


Sets the color at the given location to the specified RGBA value. If pixel does not exists, the call will be ignored.


### `SetRGBAAt(p.X, p.Y, color)`

**Returns:** ``



### `GetChannelsPerPixel()`

**Returns:** `int`


Returns the bytes occupied by a single pixel of this image


### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `if(Graphics::Texture::id!=0)`

**Returns:** ``


Returns the color mode of the image


### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `if(Graphics::Texture::id!=0)`

**Returns:** ``


Returns the size of this image resource. It is possible for an image to become unsynchronized due to a modification to the image data. Image texture size takes precedence if this happens.


### `if(data)`

**Returns:** `else`



### `HasAlpha()`

**Returns:** `bool`


Returns if this image has alpha channel


### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `GetAlphaIndex()`

**Returns:** `int`


Returns the index of alpha channel. Value of -1 denotes no alpha channel


### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `GetWidth()`

**Returns:** `int`


Returns the width of the bitmap. If texture is prepared, the width of the texture is returned otherwise width of the bitmap is returned


### `GetHeight()`

**Returns:** `int`


Returns the height of the bitmap. If texture is prepared, the height of the texture is returned otherwise height of the bitmap is returned


### `Prepare()`

**Returns:** `virtual void`


This function prepares image for drawing


### `Discard()`

**Returns:** `virtual void`


This function discards image data


### `ImportPNG(const std::string &filename)`

**Returns:** `bool`


Imports a PNG file to become the new data of this image resource. Notice that importing does not prepare the data to be drawn, a separate call to Prepare function is necessary. Returns true on success. False if file is not found. In other cases (eg. corrupt file), it will throw.


### `ImportJPEG(const std::string &filename)`

**Returns:** `bool`


Imports a JPEG file to become the new data of this image resource. Notice that importing does not prepare the data to be drawn, a separate call to Prepare function is necessary


### `ImportBMP(const std::string &filename)`

**Returns:** `bool`


Imports a BMP file to become the new data of this image resource. Notice that importing does not prepare the data to be drawn, a separate call to Prepare function is necessary


### `ImportPNG(std::istream &file)`

**Returns:** `bool`


Imports a PNG file to become the new data of this image resource. Notice that importing does not prepare the data to be drawn, a separate call to Prepare function is necessary. Returns true on success. False if file is not found. In other cases (eg. corrupt file), it will throw.


### `ImportJPEG(std::istream &file)`

**Returns:** `bool`


Imports a JPEG file to become the new data of this image resource. Notice that importing does not prepare the data to be drawn, a separate call to Prepare function is necessary


### `ImportBMP(std::istream &file)`

**Returns:** `bool`


Imports a BMP file to become the new data of this image resource. Notice that importing does not prepare the data to be drawn, a separate call to Prepare function is necessary


### `Import(const std::string &filename)`

**Returns:** `bool`


Imports an image file to become the new data of this image resource. Type of the image is determined from the extension or if extension is not present from file signature. Notice that importing does not prepare the data to be drawn, a separate call to Prepare function is necessary


### `Import(std::istream &file)`

**Returns:** `bool`


Imports an image file to become the new data of this image resource. Filetype is determined from file signature. Notice that importing does not prepare the data to be drawn, a separate call to Prepare function is necessary


### `Export(const std::string &filename)`

**Returns:** `bool`


Exports the data of the image resource to a PNG file. This function requires image data to be present. If image data is already discarded, there is no way to retrieve it. May throw if color mode is not supported by PNG encoding. PNG encoding allows: RGB, RGBA, Grayscale, Grayscale alpha. Additionally, Alpha only images are saved as grayscale alpha.


### `ExportPNG(const std::string &filename)`

**Returns:** `bool`


Exports the data of the image resource to a PNG file. This function requires image data to be present. If image data is already discarded, there is no way to retrieve it. May throw if color mode is not supported by PNG encoding. PNG encoding allows: RGB, RGBA, Grayscale, Grayscale alpha. Additionally, Alpha only images are saved as grayscale alpha.


### `ExportPNG(std::ostream &out)`

**Returns:** `bool`


Exports the data of the image resource to a PNG file. This function requires image data to be present. If image data is already discarded, there is no way to retrieve it. May throw if color mode is not supported by PNG encoding. PNG encoding allows: RGB, RGBA, Grayscale, Grayscale alpha. Additionally, Alpha only images are saved as grayscale alpha.


### `ExportBMP(const std::string &filename)`

**Returns:** `bool`


Exports the data of the image resource to a bitmap file. This function requires image data to be present. If image data is already discarded, there is no way to retrieve it. All color modes are supported in BMP, however, saving and loading the file may change the color mode. Regardless of this change when drawn, bitmap will appear the same on the screen.


### `ExportBMP(std::ostream &out)`

**Returns:** `bool`


Exports the data of the image resource to a bitmap file. This function requires image data to be present. If image data is already discarded, there is no way to retrieve it. All color modes are supported in BMP, however, saving and loading the file may change the color mode. Regardless of this change when drawn, bitmap will appear the same on the screen.


### `ExportJPEG(const std::string &filename, int quality = 90)`

**Returns:** `bool`


Exports the data of the image resource to a JPG file. This function requires image data to be present. If image data is already discarded, there is no way to retrieve it. May throw if color mode is not supported by PNG encoding. JPG encoding allows: RGB and Grayscale. Quality is between 0 and 100.


### `ExportJPG(std::ostream &out, int quality = 90)`

**Returns:** `bool`


Exports the data of the image resource to a JPG file. This function requires image data to be present. If image data is already discarded, there is no way to retrieve it. May throw if color mode is not supported by PNG encoding. JPG encoding allows: RGB and Grayscale. Quality is between 0 and 100.


### `Blur(float amount, int windowsize=-1)`

**Returns:** `Bitmap`


Creates the blurred version of this image as a new separate image. This function creates another image since it is not possible to apply blur in place. You may use move assignment to modify the original `img = img.Blur(1.2);` @param  amount is variance of the blur. This value is measured in pixels however, image will have blurred edges more than the given amount. @param  windowsize is the size of the effect window. If the value is -1, the window size is automatically determined. Reducing window size will speed up this function.


### `Shadow(float amount, int windowsize=-1)`

**Returns:** `Bitmap`


Creates a smooth drop shadow by using alpha channel of this image. Resultant image has Grayscale_Alpha color mode. This function creates another image. @param  amount is variance of the blur. This value is measured in pixels however, image will have blurred edges more than the given amount. @param  windowsize is the size of the effect window. If the value is -1, the window size is automatically determined. Reducing window size will speed up this function.


### `Grayscale(float ratio=1.0f, GrayscaleConversionMethod method = Luminance)`

**Returns:** `void`


Transforms this image to a grayscale image. This function has no effect if the image is already grayscale @param  ratio of the transformation. If ratio is 0, image is not modified. If the ratio is 1, image will be transformed into fully grayscale image. Values between 0 and 1 will desaturate the image depending on the given ratio. If the ratio is 1, color mode of the image will be modified to Grayscale or Grayscale_Alpha. @param  method to be used for transformation. Default is Luminance which mimic human vision


### `StripAlpha()`

**Returns:** `void`


This function removes transparency information from the image


### `StripRGB()`

**Returns:** `void`


This function removes color channels, leaving only alpha channel.


### `Trim(bool left, bool top, bool right, bool bottom)`

**Returns:** `Geometry::Margin`


Trims the empty parts of the image, alpha channel = 0 is used to determine empty portions. Parameters control which sides of the image would be trimmed. Trim operation will not be performed on empty images.


### `Trim()`

**Returns:** `Geometry::Margin`


Trims the empty parts of the image, alpha channel = 0 is used to determine empty portions. Trimming is performed to all sides of the image. Trim operation will not be performed on empty images.


### `Trim(true, true, true, true)`

**Returns:** `return`



### `Trim(bool horizontal, bool vertical)`

**Returns:** `Geometry::Margin`


Trims the empty parts of the image, alpha channel = 0 is used to determine empty portions. Parameters control which sides of the image would be trimmed. Trim operation will not be performed on empty images.


### `Trim(horizontal, vertical, horizontal, vertical)`

**Returns:** `return`



### `Trim(Geometry::Bounds bounds, bool left, bool top, bool right, bool bottom)`

**Returns:** `Geometry::Margin`


Trims the empty parts of the image, alpha channel = 0 is used to determine empty potions. This variant performs the check within the specified region and thus suitable for atlas images. This trim operation will not actually modify the image.


### `Trim(Geometry::Bounds bounds, bool horizontal, bool vertical)`

**Returns:** `Geometry::Margin`


Trims the empty parts of the image, alpha channel = 0 is used to determine empty potions. This variant performs the check within the specified region and thus suitable for atlas images. This trim operation will not actually modify the image.


### `Trim(bounds, horizontal, vertical, horizontal, vertical)`

**Returns:** `return`



### `Trim(Geometry::Bounds bounds)`

**Returns:** `Geometry::Margin`


Trims the empty parts of the image, alpha channel = 0 is used to determine empty potions. This variant performs the check within the specified region and thus suitable for atlas images. This trim operation will not actually modify the image.


### `Trim(bounds, true, true, true, true)`

**Returns:** `return`



### `for(int y=0; y<data->GetHeight()`

**Returns:** ``


Loops through all pixels of the image, giving coordinates to your function.


### `for(int x=0; x<data->GetWidth()`

**Returns:** ``



### `fn(x, y)`

**Returns:** ``



### `for(int y=0; y<data->GetHeight()`

**Returns:** ``


Loops through all pixels and channels of the image, giving coordinates to your function.


### `for(int x=0; x<data->GetWidth()`

**Returns:** ``



### `for(int c=0; c<GetChannelsPerPixel()`

**Returns:** ``



### `fn(x, y, c)`

**Returns:** ``



### `for(int y=0; y<data->GetHeight()`

**Returns:** ``


Loops through all pixels of the image, giving coordinates to your function. If you return false, looping will stop and the function will return false.


### `for(int x=0; x<data->GetWidth()`

**Returns:** ``



### `for(int y=0; y<data->GetHeight()`

**Returns:** ``


Loops through all pixels of the image, giving coordinates to your function. If you return false, looping will stop and the function will return false.


### `for(int x=0; x<data->GetWidth()`

**Returns:** ``



### `for(int c=0; c<GetChannelsPerPixel()`

**Returns:** ``



### `for(int y=0; y<data->GetHeight()`

**Returns:** ``


Loops through all pixels of the image, giving the specified channel value to your function.


### `for(int x=0; x<data->GetWidth()`

**Returns:** ``



### `for(int y=0; y<data->GetHeight()`

**Returns:** ``


Loops through all pixels of the image, giving the specified channel value to your function.


### `for(int x=0; x<data->GetWidth()`

**Returns:** ``



### `for(int y=0; y<data->GetHeight()`

**Returns:** ``


Loops through all channels of all pixels of the image


### `for(int x=0; x<data->GetWidth()`

**Returns:** ``



### `for(int c=0; c<GetChannelsPerPixel()`

**Returns:** ``



### `for(int y=0; y<data->GetHeight()`

**Returns:** ``


Loops through all channels of all pixels of the image


### `for(int x=0; x<data->GetWidth()`

**Returns:** ``



### `for(int c=0; c<GetChannelsPerPixel()`

**Returns:** ``



### `for(int y=0; y<data->GetHeight()`

**Returns:** ``


Loops through all pixels of the image, giving the specified channel value to your function. If you return false, looping will stop and the function will return false.


### `for(int x=0; x<data->GetWidth()`

**Returns:** ``



### `for(int y=0; y<data->GetHeight()`

**Returns:** ``


Loops through all pixels of the image, giving the specified channel value to your function. If you return false, looping will stop and the function will return false.


### `for(int x=0; x<data->GetWidth()`

**Returns:** ``



### `IsEmpty(Geometry::Bounds bounds)`

**Returns:** `bool`


Checks if the given region of this bitmap is completely transparent.


### `IsEmpty()`

**Returns:** `bool`


Checks if this bitmap is empty: either 0x0 in size or completely transparent.


### `Rotate90()`

**Returns:** `Graphics::Bitmap`


Rotates image data without any losses


### `Rotate180()`

**Returns:** `Graphics::Bitmap`


Rotates image data without any losses


### `Rotate270()`

**Returns:** `Graphics::Bitmap`


Rotates image data without any losses


### `ZoomMultiple(int factor)`

**Returns:** `Graphics::Bitmap`


Zooms the image while preserving the colors.


### `Clear()`

**Returns:** `void`


Cleans the contents of the buffer by setting every byte it contains to 0.


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `CreateLinearAtlas(Containers::Collection<const Bitmap> list, AtlasMargin margins = None)`

**Returns:** `std::vector<Geometry::Bounds>`


Assumes all image heights are similar and all images have same color mode. If there is colormode problem, this function will throw. You can either have duplicate or move your collection to this function as it needs to modify the collection on the run. Moving would be more efficient. Margin can be useful if the images would be drawn resized. Unless a margin correction method is selected, textures will bleed into each other. Currently only None and Empty modes are supported.


### `GenerateAtlasBounds(Geometry::Size size, Geometry::Point margin = {0, 0}, Geometry::Point outer_margin = {0, 0})`

**Returns:** `std::vector<Geometry::Bounds>`



### `GenerateAtlasBounds(int size, int margin = 0, int outer_margin = 0)`

**Returns:** `std::vector<Geometry::Bounds>`



### `GenerateAtlasBounds(Geometry::Size size, int margin = {}, int outer_margin = {})`

**Returns:** `std::vector<Geometry::Bounds>`



### `GenerateAtlasBounds(int size, Geometry::Point margin = {}, Geometry::Point outer_margin = {})`

**Returns:** `std::vector<Geometry::Bounds>`



### `CreateAtlasImages(std::vector<Geometry::Bounds> boundaries)`

**Returns:** `std::vector<TextureImage>`


Creates images from the given atlas image and map. Prepares every image as well. This requires image to be prepared. Texture images can be passed around as value, but it is best to avoid that.


### `Slice(Geometry::Bounds bounds)`

**Returns:** `Bitmap`


Returns a new bitmap containing a slice of this bitmap


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `Scale(int width, int height, Containers::InterpolationMethod method = Containers::InterpolationMethod::Cubic)`

**Returns:** `Bitmap`


Scales this bitmap as a new one using the supplied interpolation method. If the size is reduced more than twice, integer part of the size reduction is done using area interpolation.


### `Scale({width, height}, method)`

**Returns:** `return`



### `Scale(const Geometry::Size &newsize, Containers::InterpolationMethod method = Containers::InterpolationMethod::Cubic)`

**Returns:** `Bitmap`


Scales this bitmap as a new one using the supplied interpolation method. If the size is reduced more than twice, integer part of the size reduction is done using area interpolation.


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `Rotate(Float ang, const Geometry::Pointf &origin, Containers::InterpolationMethod method = Containers::InterpolationMethod::Cubic)`

**Returns:** `Bitmap`


Rotates this bitmap as a new one using the supplied interpolation method.


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `Rotate(Float ang, Containers::InterpolationMethod method = Containers::InterpolationMethod::Cubic)`

**Returns:** `Bitmap`


Rotates this bitmap as a new one using the supplied interpolation method.


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `ShrinkMultiple(const Geometry::Size& factor)`

**Returns:** `Bitmap`


Shrinks the bitmap size to integer multiples. This method uses Area interpolation


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `SkewX(Float perpixel, Containers::InterpolationMethod method = Containers::InterpolationMethod::Cubic)`

**Returns:** `Bitmap`


Skews this bitmap as a new one using the supplied interpolation method. Origin is assumed to be 0, 0


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `SkewX(Float perpixel, const Geometry::Pointf &origin, Containers::InterpolationMethod method = Containers::InterpolationMethod::Cubic)`

**Returns:** `Bitmap`


Skews this bitmap as a new one using the supplied interpolation method.


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `SkewY(Float perpixel, Containers::InterpolationMethod method = Containers::InterpolationMethod::Cubic)`

**Returns:** `Bitmap`


Skews this bitmap as a new one using the supplied interpolation method. Origin is assumed to be 0, 0


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `SkewY(Float perpixel, const Geometry::Pointf &origin, Containers::InterpolationMethod method = Containers::InterpolationMethod::Cubic)`

**Returns:** `Bitmap`


Skews this bitmap as a new one using the supplied interpolation method.


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `MirrorX()`

**Returns:** `Bitmap`


Mirrors this bitmap along X axis as a new one using the supplied interpolation method.


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `MirrorY()`

**Returns:** `Bitmap`


Mirrors this bitmap along Y axis as a new one using the supplied interpolation method.


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `FlipX()`

**Returns:** `Bitmap`


Flips this bitmap along X axis as a new one using the supplied interpolation method.


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `FlipY()`

**Returns:** `Bitmap`


Mirrors this bitmap along Y axis as a new one using the supplied interpolation method.


### `ASSERT(data, "Bitmap data is not set")`

**Returns:** ``



### `GetSize()`

**Returns:** `return`


When used as animation, an image is always persistent and it never finishes.

