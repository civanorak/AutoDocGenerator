# Vorbis

> Auto-generated documentation for the **Vorbis** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `streamread`

**Namespace:** `vorbis`

#### Methods

##### `if(len == -1)`

**Returns:** ``


### `VorbisStream`

**Namespace:** `vorbis`

#### Methods

##### `VorbisStream(—)`

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

### `vorbischannels(int channelcount)`

**Returns:** `inline std::vector<Audio::Channel>`



### `switch(channelcount)`

**Returns:** ``



### `ogg_streamseek(void *vs, ogg_int64_t to, int type)`

**Returns:** `int`



### `if(v->stream)`

**Returns:** ``



### `switch(type)`

**Returns:** ``



### `ogg_streamtell(void *vs)`

**Returns:** `long`



### `ogg_streamread(void* dest, size_t size1, size_t size2, void* vs)`

**Returns:** `size_t`



### `if(v->stream)`

**Returns:** ``



### `ov_clear(ogg)`

**Returns:** ``


@endcond


### `ASSERT(streamer, "Stream decoding is not initialized")`

**Returns:** ``



### `bail("info")`

**Returns:** ``



### `if(samplerate != info->rate || channelcount != info->channels)`

**Returns:** ``



### `if(last != start)`

**Returns:** ``



### `if(err == OV_EOF && start < last)`

**Returns:** ``



### `DecodeStart(streamer->stream, streamer->len)`

**Returns:** ``



### `bail("seek")`

**Returns:** ``



### `bail("seek")`

**Returns:** ``



### `while(processed < target)`

**Returns:** ``



### `if(sz < 0)`

**Returns:** ``



### `bail("decoding")`

**Returns:** ``



### `if(sz == 0)`

**Returns:** `else`



### `for(long i=0; i<sz; i++)`

**Returns:** ``



### `for(int ch=0; ch<channelcount; ch++)`

**Returns:** ``



### `DecodeStart(*stream)`

**Returns:** `return`



### `if(!ogg)`

**Returns:** ``



### `ov_clear(ogg)`

**Returns:** ``



### `if(res != 0)`

**Returns:** ``



### `bail()`

**Returns:** ``



### `bail()`

**Returns:** ``



### `if(samples < 0)`

**Returns:** ``



### `bail()`

**Returns:** ``



### `ov_pcm_seek(ogg, 0)`

**Returns:** ``


