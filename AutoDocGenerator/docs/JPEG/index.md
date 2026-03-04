# JPEG

> Auto-generated documentation for the **JPEG** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `myerror`

**Namespace:** `Gorgon`


### `SourceManager`

**Namespace:** `jpg`


### `DestManager`

**Namespace:** `jpg`


### `Reader`

**Namespace:** `jpg`

#### Methods

##### `Reader(—)`

**Returns:** ``

##### `virtual` `Attach(jpeg_decompress_struct &cinfo)`

**Returns:** `virtual void`

##### `virtual` `init_source(jpeg_decompress_struct &cinfo)`

**Returns:** `virtual void`

##### `virtual` `fill_input_buffer(jpeg_decompress_struct &cinfo)`

**Returns:** `virtual bool`

##### `virtual` `skip_input_data(jpeg_decompress_struct &cinfo, long size)`

**Returns:** `virtual void`

##### `virtual` `resync_to_restart(jpeg_decompress_struct &cinfo, int desired)`

**Returns:** `virtual bool`

##### `virtual` `term_source(jpeg_decompress_struct &cinfo)`

**Returns:** `virtual void`


### `StreamReader`

**Namespace:** `jpg`

#### Methods

##### `virtual` `init_source(jpeg_decompress_struct &cinfo)`

**Returns:** `virtual void`

##### `virtual` `fill_input_buffer(jpeg_decompress_struct &cinfo)`

**Returns:** `virtual bool`

##### `virtual` `skip_input_data(jpeg_decompress_struct &cinfo, long size)`

**Returns:** `virtual void`


### `VectorReader`

**Namespace:** `jpg`

#### Methods

##### `virtual` `init_source(jpeg_decompress_struct &cinfo)`

**Returns:** `virtual void`

##### `virtual` `fill_input_buffer(jpeg_decompress_struct &cinfo)`

**Returns:** `virtual bool`


### `ArrayReader`

**Namespace:** `jpg`

#### Methods

##### `virtual` `init_source(jpeg_decompress_struct &cinfo)`

**Returns:** `virtual void`

##### `virtual` `fill_input_buffer(jpeg_decompress_struct &cinfo)`

**Returns:** `virtual bool`


### `Writer`

**Namespace:** `jpg`

#### Methods

##### `Writer(—)`

**Returns:** ``

##### `virtual` `Attach(jpeg_compress_struct &cinfo)`

**Returns:** `virtual void`

##### `virtual` `init_destination(jpeg_compress_struct &cinfo)`

**Returns:** `virtual void`

##### `virtual` `empty_output_buffer(jpeg_compress_struct &cinfo)`

**Returns:** `virtual bool`

##### `virtual` `term_destination(jpeg_compress_struct &cinfo)`

**Returns:** `virtual void`


### `StreamWriter`

**Namespace:** `jpg`

#### Methods

##### `virtual` `init_destination(jpeg_compress_struct &cinfo)`

**Returns:** `virtual void`

##### `virtual` `empty_output_buffer(jpeg_compress_struct &cinfo)`

**Returns:** `virtual bool`

##### `virtual` `term_destination(jpeg_compress_struct &cinfo)`

**Returns:** `virtual void`


### `VectorWriter`

**Namespace:** `jpg`

#### Methods

##### `virtual` `init_destination(jpeg_compress_struct &cinfo)`

**Returns:** `virtual void`

##### `virtual` `empty_output_buffer(jpeg_compress_struct &cinfo)`

**Returns:** `virtual bool`

##### `virtual` `term_destination(jpeg_compress_struct &cinfo)`

**Returns:** `virtual void`


### `JPEG`

**Namespace:** `jpg`

#### Methods

##### `JPEG(—)`

**Returns:** ``

##### `Decode(std::istream &input, Containers::Image &output)`

**Returns:** `void`

Decodes given JPG data from the given input and creates the image. throws runtime error

##### `reader(input)`

**Returns:** `jpg::StreamReader`

##### `decode(reader, output)`

**Returns:** ``

##### `Decode(const std::string &input, Containers::Image &output)`

**Returns:** `void`

Decodes given JPG data from the given input and creates the image. throws runtime error

##### `file(input, std::ios::binary)`

**Returns:** `std::ifstream`

##### `Decode(file, output)`

**Returns:** ``

##### `Decode(std::vector<Byte> &input, Containers::Image &output)`

**Returns:** `void`

Decodes given JPG data from the given input and creates the image. throws runtime error

##### `reader(input)`

**Returns:** `jpg::VectorReader`

##### `decode(reader, output)`

**Returns:** ``

##### `Decode(Byte *input, std::size_t size, Containers::Image &output)`

**Returns:** `void`

Decodes given JPG data from the given input and creates the image. throws runtime error

##### `reader(input, size)`

**Returns:** `jpg::ArrayReader`

##### `decode(reader, output)`

**Returns:** ``

##### `Encode(Containers::Image &input, std::ostream &output, int quality = 90)`

**Returns:** `void`

Encode given image to JPG compressed data. Quality is in percents 100 means best. throws runtime error

##### `writer(output)`

**Returns:** `jpg::StreamWriter`

##### `encode(writer, input, quality)`

**Returns:** ``

##### `Encode(Containers::Image &input, const std::string &output, int quality = 90)`

**Returns:** `void`

Encode given image to JPG compressed data. Quality is in percents 100 means best. throws runtime error

##### `file(output, std::ios::binary)`

**Returns:** `std::ofstream`

##### `Encode(input, file, quality)`

**Returns:** ``

##### `Encode(Containers::Image &input, std::vector<Byte> &output, int quality = 90)`

**Returns:** `void`

Encode given image to JPG compressed data. Quality is in percents 100 means best. throws runtime error

##### `writer(output)`

**Returns:** `jpg::VectorWriter`

##### `encode(writer, input, quality)`

**Returns:** ``

##### `encode(jpg::Writer &writer, Containers::Image &input, int quality)`

**Returns:** `void`

##### `decode(jpg::Reader &reader, Containers::Image &output)`

**Returns:** `void`


---

## Functions

### `my_error_exit(j_common_ptr cinfo)`

**Returns:** `void`



### `my_output_message(j_common_ptr cinfo)`

**Returns:** `void`



### `jpgtocolormode(const struct jpeg_decompress_struct &cinfo)`

**Returns:** `Graphics::ColorMode`



### `if(cinfo.out_color_space == JCS_RGB)`

**Returns:** ``



### `if(cinfo.out_color_components==3)`

**Returns:** ``



### `if(cinfo.out_color_components==4)`

**Returns:** `else`



### `if(cinfo.out_color_space == JCS_GRAYSCALE)`

**Returns:** `else`



### `if(cinfo.out_color_components==1)`

**Returns:** ``



### `if(cinfo.out_color_components==2)`

**Returns:** `else`



### `jpeg_create_decompress(&cinfo)`

**Returns:** ``



### `jpeg_read_header(&cinfo, TRUE)`

**Returns:** ``



### `jpeg_start_decompress(&cinfo)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `jpeg_destroy_decompress(&cinfo)`

**Returns:** ``



### `jpeg_finish_decompress(&cinfo)`

**Returns:** ``



### `jpeg_destroy_decompress(&cinfo)`

**Returns:** ``



### `jpeg_create_compress(&cinfo)`

**Returns:** ``



### `jpeg_set_defaults(&cinfo)`

**Returns:** ``



### `jpeg_set_quality(&cinfo, quality, TRUE)`

**Returns:** ``



### `jpeg_start_compress(&cinfo, TRUE)`

**Returns:** ``



### `while(cinfo.next_scanline < cinfo.image_height)`

**Returns:** ``



### `jpeg_write_scanlines(&cinfo, &data, 1)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `jpeg_destroy_compress(&cinfo)`

**Returns:** ``



### `jpeg_finish_compress(&cinfo)`

**Returns:** ``



### `jpeg_destroy_compress(&cinfo)`

**Returns:** ``



### `fill_input_buffer(cinfo)`

**Returns:** ``



### `init_source(jpeg_decompress_struct *cinfo)`

**Returns:** `void`



### `fill_input_buffer(jpeg_decompress_struct *cinfo)`

**Returns:** `boolean`



### `skip_input_data(jpeg_decompress_struct *cinfo, long size)`

**Returns:** `void`



### `resync_to_restart(jpeg_decompress_struct *cinfo, int desired)`

**Returns:** `boolean`



### `term_source(jpeg_decompress_struct *cinfo)`

**Returns:** `void`



### `init_destination(jpeg_compress_struct *cinfo)`

**Returns:** `void`



### `empty_output_buffer(jpeg_compress_struct *cinfo)`

**Returns:** `boolean`



### `term_destination(jpeg_compress_struct *cinfo)`

**Returns:** `void`


