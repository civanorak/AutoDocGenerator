# Kernel

&gt; Auto-generated documentation for the **Kernel** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Kernel`

**Namespace:** `Gorgon`

#### Methods

##### `Kernel(—)`

**Returns:** ``

Default constructor creates an empty kernel

##### `Kernel(const std::initializer_list<std::initializer_list<Float>> &values)`

**Returns:** ``

Creates a new kernel using the supplied values

##### `Resize(const Geometry::Size &size)`

**Returns:** `void`

Move constructor is supported Copy constructor is supported Assigns new values Move assignment is supported Copy assignment is supported Changes the size of the kernel. Values will not be preserved in a meaningful way.

##### `Resize(int width, int height)`

**Returns:** `void`

Changes the size of the kernel. Values will not be preserved in a meaningful way.

##### `Resize({width, height})`

**Returns:** ``

##### `Resize(int size)`

**Returns:** `void`

Changes the size of the kernel. Values will not be preserved in a meaningful way. This variant sets both dimensions to the value value.

##### `Resize({size, size})`

**Returns:** ``

##### `GetWidth(—)`

**Returns:** `int`

Returns the width of the filter

##### `GetHeight(—)`

**Returns:** `int`

Returns the height of the filter

##### `GetSize(—)`

**Returns:** `Geometry::Size`

Returns the size of the filter

##### `GetTotal(—)`

**Returns:** `Float`

Returns sum of all elements in the filter

##### `Get(int x, int y)`

**Returns:** `Float`

Returns a specific element. This value can be changed Returns a specific element.

##### `Get(const Geometry::Point &index)`

**Returns:** `Float`

Returns a specific element.

##### `Normalize(—)`

**Returns:** `void`

Returns a specific element. This value can be changed Returns a specific element. This value can be changed Returns a specific element. Returns a specific element. This value can be changed Returns the internal data that is stored Normalizes the kernel so the sum becomes 1

##### `static` `SobelFilter(Axis axis)`

**Returns:** `static Kernel`

Create a sobel filter for gradient calculation

##### `static` `Sharpen(—)`

**Returns:** `static Kernel`

Creates a simple sharpen filter.

##### `static` `BoxFilter(int kernelsize)`

**Returns:** `static Kernel`

Creates a box kernel for blur filter. It is better to use gaussian filter for this purpose.

##### `static` `CircularFilter(float kernelsize)`

**Returns:** `static Kernel`

Creates a Circular filter, it can be used by the openning/closing

##### `static` `EdgeDetection(int kernelsize)`

**Returns:** `static Kernel`

A kernel that can be used for edge detection.

##### `static` `GaussianFilter(float sigma, Axis axis, float quality = 2.0f)`

**Returns:** `static Kernel`

Creates kernel for Gaussian blur filter. This function creates filter for only one axis. Gaussian blur can be achived by applying two separate filters for axis instead of single two dimensional filter. By splitting the kernel filtering works at least sigma times faster. Larger quality values improve the result while reducing the processing speed. Qualities above 3 will not yield an improvement for 8-bit images.

##### `createboxfilter(float centervalue, float others)`

**Returns:** `void`

##### `createcircularfilter(float centervlaue, float others)`

**Returns:** `void`


---

## Functions

### `for(auto &list : values)`

**Returns:** ``



### `for(auto &list : values)`

**Returns:** ``



### `for(auto &val : kernel)`

**Returns:** ``



### `switch(axis)`

**Returns:** ``



### `for(int x = 0; x < size; x++)`

**Returns:** ``



### `for(int y = 0; y < size.Height; y++)`

**Returns:** ``



### `for(int x= 0; x < size.Width; x++)`

**Returns:** ``



### `for(int y = -size.Height/2; y < size.Height/2; y++)`

**Returns:** ``



### `for(int x= -size.Width/2; x < size.Width/2; x++)`

**Returns:** ``



### `oldState(nullptr)`

**Returns:** `std::ios`



### `for(int y=0; y<kernel.GetHeight()`

**Returns:** ``



### `for(int x=0; x<kernel.GetWidth()`

**Returns:** ``


