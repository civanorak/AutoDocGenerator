# PulseAudio

&gt; Auto-generated documentation for the **PulseAudio** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `AudioLoop()`

**Returns:** `void`



### `pa_wait_connection(pa_mainloop *pam, unsigned long timeout = 1000)`

**Returns:** `bool`



### `while(pa_state == pa_waiting)`

**Returns:** ``



### `pa_mainloop_iterate(pam, 0, NULL)`

**Returns:** ``



### `pa_wait_stream_connection(pa_mainloop *pam, pa_stream *pa_stream, unsigned long timeout = 1000)`

**Returns:** `bool`



### `pa_mainloop_iterate(pam, 0, NULL)`

**Returns:** ``



### `wait_pa_op(pa_operation* pa_op, int timeout = 1000)`

**Returns:** `bool`



### `if(pa_op == nullptr)`

**Returns:** ``



### `pa_mainloop_iterate(pa_main, 0, NULL)`

**Returns:** ``



### `pa_state_cb(pa_context *ctx, void *userdata)`

**Returns:** `void`



### `switch(state)`

**Returns:** ``



### `convertopa(Channel ch)`

**Returns:** `pa_channel_position`



### `switch(ch)`

**Returns:** ``



### `convertpachannel(pa_channel_position channel)`

**Returns:** `Channel`



### `switch(channel)`

**Returns:** ``



### `Initialize()`

**Returns:** `void`



### `if(!pa_main)`

**Returns:** ``



### `if(!pa_ctx)`

**Returns:** ``



### `pa_context_set_state_callback(pa_ctx, pa_state_cb, nullptr)`

**Returns:** ``



### `pa_context_connect(pa_ctx, nullptr, PA_CONTEXT_NOFLAGS, nullptr)`

**Returns:** ``



### `if(pa_state == pa_failed)`

**Returns:** ``



### `if(pa_state == pa_timeout)`

**Returns:** ``



### `for(int i=0; i<chmap.channels; i++)`

**Returns:** ``



### `if(!pa_strm)`

**Returns:** ``



### `if(result != 0)`

**Returns:** ``



### `if(!result)`

**Returns:** ``



### `if(devname==nullptr)`

**Returns:** ``



### `for(int i=0; i<newchmap->channels; i++)`

**Returns:** ``



### `if(result!=0)`

**Returns:** ``



### `if(errno == EPERM)`

**Returns:** ``



### `pa_sinklist_cb(pa_context *c, const pa_sink_info *l, int eol, void *userdata)`

**Returns:** `void`



### `if(eol > 0)`

**Returns:** ``



### `switch(l->sample_spec.format)`

**Returns:** ``



### `for(int i = 0; i<l->channel_map.channels; i++)`

**Returns:** ``



### `if(l->active_port)`

**Returns:** ``



### `server_info_cb(pa_context* context, const pa_server_info* info, void *nm)`

**Returns:** `void`



### `if(!pa_op)`

**Returns:** ``



### `pa_operation_unref(pa_op)`

**Returns:** ``



### `swap(tempdevices, devices)`

**Returns:** ``



### `if(def_sinkname!="")`

**Returns:** ``



### `catch(const std::runtime_error &err)`

**Returns:** ``



### `if(!finished)`

**Returns:** ``



### `IsAvailable()`

**Returns:** `bool`


