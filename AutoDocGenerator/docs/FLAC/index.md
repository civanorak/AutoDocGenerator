# FLAC

> Auto-generated documentation for the **FLAC** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `vectorio`

**Namespace:** `flac`


### `streamdata`

**Namespace:** `flac`

#### Methods

##### `streamdata(—)`

**Returns:** ``

##### `free(data)`

**Returns:** ``

##### `allocateupto(std::size_t size)`

**Returns:** `void`

##### `free(data)`

**Returns:** ``

##### `allocate(std::size_t size)`

**Returns:** `void`

##### `free(data)`

**Returns:** ``


### `streamwrite`

**Namespace:** `flac`


### `streamread`

**Namespace:** `flac`

#### Methods

##### `if(len == -1)`

**Returns:** ``


### `vectorread`

**Namespace:** `flac`


### `FLAC`

**Namespace:** `flac`

#### Methods

##### `FLAC(int buffersize = 8*1024)`

**Returns:** ``

##### `Encode(const Containers::Wave &input, std::ostream &output, int bps = 16)`

**Returns:** `void`

Encodes the given wave data to %FLAC compressed data. bps is the bit/sample. It is best to use original bit/sample if re-saving a file. Lower values will save disk space while sacrificing quality. Current FLAC implementation supports 4 - 24 bit/sample. Channel layout is saved as is, and it is the responsibility of the caller to make it compatible with the standard layout. This function is not thread safe, you need one FLAC object per thread.

##### `Encode(const Containers::Wave &input, const std::string &filename, int bps = 16)`

**Returns:** `void`

Encodes the given wave data to %FLAC compressed data. bps is the bit/sample. It is best to use original bit/sample if re-saving a file. Lower values will save disk space while sacrificing quality. Current FLAC implementation supports 4 - 24 bit/sample. Channel layout is saved as is, and it is the responsibility of the caller to make it compatible with the standard layout. This function is not thread safe, you need one FLAC object per thread.

##### `stream(filename, std::ios::binary)`

**Returns:** `std::ofstream`

##### `Encode(input, stream, bps)`

**Returns:** ``

##### `Encode(const Containers::Wave &input, std::vector<Byte> &output, int bps = 16)`

**Returns:** `void`

Encodes the given wave data to %FLAC compressed data. bps is the bit/sample. It is best to use original bit/sample if re-saving a file. Lower values will save disk space while sacrificing quality. Current FLAC implementation supports 4 - 24 bit/sample. Channel layout is saved as is, and it is the responsibility of the caller to make it compatible with the standard layout.

##### `Decode(std::istream &input, Containers::Wave &wave, size_t len = -1)`

**Returns:** `void`

Decodes given %FLAC compressed data and fills a wave container.

##### `Decode(const std::vector<Byte> &input, Containers::Wave &wave)`

**Returns:** `void`

Decodes given %FLAC compressed data and fills a wave container.

##### `Decode(const std::string &filename, Containers::Wave &wave)`

**Returns:** `void`

Decodes given %FLAC compressed file and fills a wave container.

##### `stream(filename, std::ios::binary)`

**Returns:** `std::ifstream`

##### `Decode(stream, wave)`

**Returns:** ``

##### `encode(void *enc, const Containers::Wave &input, int bps)`

**Returns:** `void`


### `FLACStream`

**Namespace:** `flac`

#### Methods

##### `FLACStream(—)`

**Returns:** ``

##### `DecodeSome(Containers::Wave &container, unsigned long start)`

**Returns:** `unsigned long`

Decodes data from the requested location. Container must be initialized. This function will try to fill the container if there is enough data. If not it will leave additional samples empty.

##### `DecodeStart(std::istream &input, size_t len = -1)`

**Returns:** `Audio::AudioDataInfo`

Starts decoding the given %FLAC compressed data by obtaining metadata information. This function should require a new instance of Flac coder as it has to store some information to continue.

##### `DecodeStart(const std::string &filename)`

**Returns:** `Audio::AudioDataInfo`

Starts decoding the given %FLAC compressed file by obtaining metadata information. This function should require a new instance of Flac coder as it has to store some information to continue.


---

## Functions

### `memcpy(buffer, &input.input[input.readpos], bytestoread)`

**Returns:** ``



### `if(reader.channels == 0)`

**Returns:** ``



### `if(reader.channels != frame->header.channels)`

**Returns:** ``



### `if(reader.rate != frame->header.sample_rate)`

**Returns:** ``



### `for(int i=0; i<size; i++)`

**Returns:** ``



### `if(reader.currentpos >= reader.datasize)`

**Returns:** ``



### `decode_error(const FLAC__StreamDecoder * /*decoder*/, FLAC__StreamDecoderErrorStatus status, void * /*client_data*/)`

**Returns:** `void`



### `while(i < size)`

**Returns:** ``



### `for(int j=0; j<tobeenc; j++)`

**Returns:** ``



### `for(int c=0; c<channels; c++)`

**Returns:** ``



### `FLAC__stream_encoder_process_interleaved(encoder, &buffer[0], tobeenc)`

**Returns:** ``



### `FLAC__stream_encoder_finish(encoder)`

**Returns:** ``



### `FLAC__stream_decoder_new()`

**Returns:** `return`



### `enc_guard(enc, &FLAC__stream_encoder_delete)`

**Returns:** `std::shared_ptr<FLAC__StreamEncoder>`



### `encode(enc, input, bps)`

**Returns:** ``



### `enc_guard(enc, &FLAC__stream_encoder_delete)`

**Returns:** `std::shared_ptr<FLAC__StreamEncoder>`



### `encode(enc, input, bps)`

**Returns:** ``



### `dec_guard(dec, &FLAC__stream_decoder_delete)`

**Returns:** `std::shared_ptr<FLAC__StreamDecoder>`



### `stream(input, len)`

**Returns:** `flac::streamread`



### `FLAC__stream_decoder_process_until_end_of_metadata(dec)`

**Returns:** ``



### `FLAC__stream_decoder_process_single(dec)`

**Returns:** ``



### `if(total != 0)`

**Returns:** ``



### `FLAC__stream_decoder_process_until_end_of_stream(dec)`

**Returns:** ``



### `dec_guard(dec, &FLAC__stream_decoder_delete)`

**Returns:** `std::shared_ptr<FLAC__StreamDecoder>`



### `vector(input)`

**Returns:** `flac::vectorread`



### `FLAC__stream_decoder_process_until_end_of_metadata(dec)`

**Returns:** ``



### `FLAC__stream_decoder_process_single(dec)`

**Returns:** ``



### `if(total != 0)`

**Returns:** ``



### `FLAC__stream_decoder_process_until_end_of_stream(dec)`

**Returns:** ``



### `ASSERT(streamer, "Stream decoding is not initialized")`

**Returns:** ``



### `if(last != start)`

**Returns:** ``



### `bail("reset")`

**Returns:** ``



### `samplesdone()`

**Returns:** `return`



### `bail("seek")`

**Returns:** ``



### `samplesdone()`

**Returns:** `return`



### `bail("decoding")`

**Returns:** ``



### `samplesdone()`

**Returns:** `return`



### `samplesdone()`

**Returns:** `return`



### `DecodeStart(*stream)`

**Returns:** `return`



### `if(!dec)`

**Returns:** ``



### `if(res != FLAC__STREAM_DECODER_INIT_STATUS_OK)`

**Returns:** ``



### `FLAC__stream_decoder_process_until_end_of_metadata(dec)`

**Returns:** ``



### `FLAC__stream_decoder_process_single(dec)`

**Returns:** ``



### `FLAC__stream_decoder_reset(dec)`

**Returns:** ``


