# PNG

> Auto-generated documentation for the **PNG** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Reader`

**Namespace:** `png`


### `Writer`

**Namespace:** `png`


### `VectorReader`

**Namespace:** `png`


### `VectorWriter`

**Namespace:** `png`


### `ArrayWrapper`

**Namespace:** `png`


### `ArrayReader`

**Namespace:** `png`


### `FileReader`

**Namespace:** `png`


### `FileWriter`

**Namespace:** `png`


### `PNG`

**Namespace:** `png`

@endcond Encodes or decodes PNG compression.

#### Methods

##### `Encode(const Containers::Image &input, std::ostream &output, bool replace_colormode = false)`

**Returns:** `void`

Encodes a given input. This variant writes to a stream @warning Array write buffer should either be a nullptr of type Byte or an array allocated with malloc. This system uses realloc or malloc to resize raw arrays. @throws runtime_error in case of an encoding error

##### `Encode(const Containers::Image &input, const std::string &output, bool replace_colormode = false)`

**Returns:** `void`

Encodes a given input. This variant opens the given file and writes on that file @throws runtime_error in case of an encoding error

##### `file(output, std::ios::binary)`

**Returns:** `std::ofstream`

##### `Encode(const Containers::Image &input, std::vector<Byte> &output, bool replace_colormode = false)`

**Returns:** `void`

Encodes a given input. This variant writes data to a vector. Vector is resized automatically. @warning Array write buffer should either be a nullptr of type Byte or an array allocated with malloc. This system uses realloc or malloc to resize raw arrays. @throws runtime_error in case of an encoding error

##### `Decode(std::istream &input, Containers::Image &output)`

**Returns:** `void`

Decodes the given PNG data. This function may produce an image with the following color modes: Grayscale, Grayscale_Alpha, RGB, RGBA. This variant reads data from the file. @throws runtime_error in case of a read error

##### `Decode(const std::string &input, Containers::Image &output)`

**Returns:** `void`

Decodes the given PNG data. This function may produce an image with the following color modes: Grayscale, Grayscale_Alpha, RGB, RGBA. This variant opens and reads data from a file. @throws runtime_error in case of a read error

##### `file(input, std::ios::binary)`

**Returns:** `std::ifstream`

##### `Decode(std::vector<Byte> &input, Containers::Image &output)`

**Returns:** `void`

Decodes the given PNG data. This function may produce an image with the following color modes: Grayscale, Grayscale_Alpha, RGB, RGBA. This variant reads data from the vector. @throws runtime_error in case of a read error

##### `Decode(const Byte *input, std::size_t size, Containers::Image &output)`

**Returns:** `void`

Decodes the given PNG data. This function may produce an image with the following color modes: Grayscale, Grayscale_Alpha, RGB, RGBA. In this variant data is read from an array. @throws runtime_error in case of a read error

##### `encode(const Containers::Image &input, png::Writer *write, bool replace_colormode)`

**Returns:** `void`

Performs actual encoding

##### `decode(png::Reader *reader, Containers::Image &output)`

**Returns:** `void`

Performs actual decoding


---

## Functions

### `ReadFile(png_struct_def *p, unsigned char *buf, size_t size)`

**Returns:** `void`



### `WriteFile(png_struct *p, unsigned char *buf, size_t size)`

**Returns:** `void`



### `ReadArray(png_struct *p, unsigned char *buf, size_t size)`

**Returns:** `void`



### `if(size + reader->BufPos > reader->Buf.size)`

**Returns:** ``



### `ReadVector(png_struct *p, unsigned char *buf, size_t size)`

**Returns:** `void`



### `WriteVector(png_struct *p, unsigned char *buf, size_t size)`

**Returns:** `void`



### `r(reader)`

**Returns:** `std::unique_ptr<png::Reader>`



### `if(!info_ptr)`

**Returns:** ``



### `png_destroy_read_struct(&png_ptr, NULL, NULL)`

**Returns:** ``



### `png_destroy_read_struct(&png_ptr, &info_ptr, NULL)`

**Returns:** ``



### `png_set_sig_bytes(png_ptr, 8)`

**Returns:** ``



### `png_read_info(png_ptr, info_ptr)`

**Returns:** ``



### `if(color_type == PNG_COLOR_TYPE_PALETTE)`

**Returns:** ``



### `png_set_palette_to_rgb(png_ptr)`

**Returns:** ``



### `png_set_expand_gray_1_2_4_to_8(png_ptr)`

**Returns:** ``



### `png_set_tRNS_to_alpha(png_ptr)`

**Returns:** ``



### `png_set_strip_16(png_ptr)`

**Returns:** ``



### `png_set_gamma(png_ptr, 2.2, gamma)`

**Returns:** ``



### `png_read_update_info(png_ptr, info_ptr)`

**Returns:** ``



### `if(color_type == PNG_COLOR_TYPE_GRAY || color_type == PNG_COLOR_TYPE_GRAY_ALPHA)`

**Returns:** ``



### `if(pChannels>1)`

**Returns:** ``



### `if(color_type == PNG_COLOR_TYPE_RGB || color_type == PNG_COLOR_TYPE_RGB_ALPHA)`

**Returns:** `else`



### `if(pChannels>3)`

**Returns:** ``



### `for(i = 0; i < height; ++i)`

**Returns:** ``



### `for(i = 0; i < height-1; ++i)`

**Returns:** ``



### `for(i = 0; i < height; ++i)`

**Returns:** ``



### `for(i = 0; i < height; ++i)`

**Returns:** ``



### `png_read_end(png_ptr, NULL)`

**Returns:** ``



### `png_destroy_read_struct(&png_ptr, &info_ptr, NULL)`

**Returns:** ``



### `if(!info_ptr)`

**Returns:** ``



### `if(replace_colormode)`

**Returns:** ``



### `png_write_info(png_ptr, info_ptr)`

**Returns:** ``



### `for(unsigned long i=0; i<total; i++)`

**Returns:** ``



### `png_write_row(png_ptr, &p[i*stride])`

**Returns:** ``



### `png_write_end(png_ptr, NULL)`

**Returns:** ``



### `png_destroy_write_struct(&png_ptr, &info_ptr)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `ReadVector(png_struct_def *p, unsigned char *buf, size_t size)`

**Returns:** `void`



### `VectorReader(vec)`

**Returns:** `return new`



### `GetReadSize(const std::vector<Byte> &vec)`

**Returns:** `inline unsigned long long`



### `VectorSeek(Reader *r, long long addr)`

**Returns:** `inline void`



### `WriteVector(png_struct_def *p, unsigned char *buf, size_t size)`

**Returns:** `void`



### `VectorWriter(vec)`

**Returns:** `return new`



### `ReadArray(png_struct_def *p, unsigned char *buf, size_t size)`

**Returns:** `void`



### `ArrayReader(f)`

**Returns:** `return new`



### `GetReadSize(const ArrayWrapper &vec)`

**Returns:** `inline unsigned long long`



### `ArraySeek(Reader *r, long long addr)`

**Returns:** `inline void`



### `ReadFile(png_struct_def *p, unsigned char *buf, size_t size)`

**Returns:** `void`



### `GetReadSize(std::istream &f)`

**Returns:** `unsigned long long`



### `FileReader(f)`

**Returns:** `return new`



### `GetReadSize(std::istream &f)`

**Returns:** `inline unsigned long long`



### `FileSeek(Reader *r, long long addr)`

**Returns:** `inline void`



### `WriteFile(png_struct_def *p, unsigned char *buf, size_t size)`

**Returns:** `void`



### `FileWriter(f)`

**Returns:** `return new`


