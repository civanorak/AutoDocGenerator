# LZMA

&gt; Auto-generated documentation for the **LZMA** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `MyProgress`

**Namespace:** `Gorgon`

#### Methods

##### `static` `progress(void *p, UInt64 inSize, UInt64 outSize)`

**Returns:** `static SRes`


### `Reader`

**Namespace:** `lzma`


### `Writer`

**Namespace:** `lzma`


### `VectorReader`

**Namespace:** `lzma`


### `VectorWriter`

**Namespace:** `lzma`


### `ArrayReader`

**Namespace:** `lzma`


### `ArrayWriter`

**Namespace:** `lzma`


### `StringReader`

**Namespace:** `lzma`


### `StringWriter`

**Namespace:** `lzma`


### `FileReader`

**Namespace:** `lzma`


### `FileWriter`

**Namespace:** `lzma`


### `LZMA`

**Namespace:** `lzma`

@endcond This class allows encoding and decoding data using LZMA compression algorithm. @cond INTERNAL The main idea of this system is to reduce the amount of the code. There are reader structures that can read data from various sources. These sources are automatically created by encode/decode template functions. After creating these structures, internal encode/decode function is called. Creating an new read/write structure is enough to support that type of container @endcond

#### Methods

##### `Encode(I_ &input, O_ &output)`

**Returns:** `void`

Callback to notify progress. The value is reported between 0 and 1 Default constructor Encodes the given data to %LZMA compressed data. Supports vectors, arrays, strings and streams as data source and targets. @warning Using this system with arrays is extremely dangerous make sure your arrays are big enough @throws runtime_error

##### `Encode(I_ &input, O_ &output, ProgressNotification notifier)`

**Returns:** `void`

Encodes the given data to %LZMA compressed data. Supports vectors, arrays, strings and streams as data source and targets. This variant allows a notification function which is called during compression. @warning Using this system with arrays is extremely dangerous make sure your arrays are big enough @throws runtime_error

##### `PropertySize(—)`

**Returns:** `int`

Decodes %LZMA compressed data. Supports vectors, arrays, strings and streams as data source and targets. @param   input %Input data @param   output Output data @param   compressionproperties is the compression property data. Leaving this parameter with default nullptr, causes this function to read the actual compression properties from the main data source. @param   fsize size of the extracted data. This value is only used if UseUncompressedSize is false. Default value of -1 relies on LZMA to terminate extraction. @warning Using this system with arrays is extremely dangerous make sure your arrays are big enough @throws  runtime_error Decodes %LZMA compressed data. Supports vectors, arrays, strings and streams as data source and targets. This variant allows a notification function which is called during decompression. @param   input %Input data @param   output Output data @param   notifier is the callback to send notifications to @param   compressionproperties is the compression property data. Leaving this parameter with default nullptr, causes this function to read the actual compression properties from the main data source. @param   fsize size of the extracted data. This value is only used if UseUncompressedSize is false. Default value of -1 relies on LZMA to terminate extraction. Additionally, -1 will cause progress notification to report 0. @warning Using this system with arrays is extremely dangerous make sure your arrays are big enough @throws  runtime_error The size of the compression property data appended in front of the compressed data

##### `encode(lzma::Reader *reader, lzma::Writer *writer, unsigned long long size, ProgressNotification *notifier)`

**Returns:** `void`

Whether to encode uncompressed size with the compression properties. Default value for this variable is true. Performs actual compression, notifier can be nullptr


---

## Functions

### `AllocForLzma(void *p, size_t size)`

**Returns:** `static void *`



### `FreeForLzma(void *p, void *address)`

**Returns:** `static void`



### `reader_d(reader)`

**Returns:** `std::unique_ptr<lzma::Reader>`



### `writer_d(writer)`

**Returns:** `std::unique_ptr<lzma::Writer>`



### `if(!enc)`

**Returns:** ``



### `LzmaEncProps_Init(&props)`

**Returns:** ``



### `if(res != SZ_OK)`

**Returns:** ``



### `if(UseUncompressedSize)`

**Returns:** ``



### `if(res != SZ_OK || propsSize != LZMA_PROPS_SIZE)`

**Returns:** ``



### `if(res != SZ_OK)`

**Returns:** ``



### `LzmaEnc_Destroy(enc, &SzAllocForLzma, &SzAllocForLzma)`

**Returns:** ``



### `LzmaDec_Construct(&dec)`

**Returns:** ``



### `if(cprops==NULL)`

**Returns:** ``



### `if(UseUncompressedSize)`

**Returns:** ``



### `if(res != SZ_OK)`

**Returns:** ``



### `if(res != SZ_OK)`

**Returns:** ``



### `LzmaDec_Init(&dec)`

**Returns:** ``



### `while(outPos < fullsize)`

**Returns:** ``



### `if(res != SZ_OK)`

**Returns:** ``



### `if(status==LZMA_STATUS_NEEDS_MORE_INPUT && destLen==0)`

**Returns:** ``



### `LzmaDec_Free(&dec, &SzAllocForLzma)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `ReadVector(void *p, void *buf, size_t *size)`

**Returns:** `int`



### `VectorReader(vec)`

**Returns:** `return new`



### `GetReadSize(const std::vector<Byte> &vec)`

**Returns:** `inline unsigned long long`



### `VectorSeek(Reader *r, long long addr)`

**Returns:** `inline void`



### `ReadVector(void *p, void *buf, size_t *size)`

**Returns:** `inline int`



### `WriteVector(void *p, const void *buf, size_t size)`

**Returns:** `std::size_t`



### `VectorWriter(vec)`

**Returns:** `return new`



### `WriteVector(void *p, const void *buf, size_t size)`

**Returns:** `inline std::size_t`



### `ReadArray(void *p, void *buf, size_t *size)`

**Returns:** `int`



### `ArrayReader(vec)`

**Returns:** `return new`



### `GetReadSize(const Byte *vec)`

**Returns:** `inline unsigned long long`



### `ArraySeek(Reader *r, long long addr)`

**Returns:** `inline void`



### `ReadArray(void *p, void *buf, size_t *size)`

**Returns:** `inline int`



### `WriteArray(void *p, const void *buf, size_t size)`

**Returns:** `std::size_t`



### `ArrayWriter(vec)`

**Returns:** `return new`



### `WriteArray(void *p, const void *buf, size_t size)`

**Returns:** `inline std::size_t`



### `ReadString(void *p, void *buf, size_t *size)`

**Returns:** `int`



### `StringReader(vec)`

**Returns:** `return new`



### `GetReadSize(const std::string &vec)`

**Returns:** `inline unsigned long long`



### `StringSeek(Reader *r, long long addr)`

**Returns:** `inline void`



### `ReadString(void *p, void *buf, size_t *size)`

**Returns:** `inline int`



### `WriteString(void *p, const void *buf, size_t size)`

**Returns:** `std::size_t`



### `StringWriter(vec)`

**Returns:** `return new`



### `WriteString(void *p, const void *buf, size_t size)`

**Returns:** `inline std::size_t`



### `ReadFile(void *p, void *buf, size_t *size)`

**Returns:** `int`



### `GetReadSize(std::istream &f)`

**Returns:** `unsigned long long`



### `FileReader(f)`

**Returns:** `return new`



### `GetReadSize(std::istream &f)`

**Returns:** `inline unsigned long long`



### `FileSeek(Reader *r, long long addr)`

**Returns:** `inline void`



### `ReadFile(void *p, void *buf, size_t *size)`

**Returns:** `inline int`



### `WriteFile(void *p, const void *buf, size_t size)`

**Returns:** `std::size_t`



### `FileWriter(f)`

**Returns:** `return new`



### `WriteFile(void *p, const void *buf, size_t size)`

**Returns:** `inline std::size_t`


