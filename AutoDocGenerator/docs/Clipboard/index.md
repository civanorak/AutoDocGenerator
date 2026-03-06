# Clipboard

&gt; Auto-generated documentation for the **Clipboard** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `getclipboardformats()`

**Returns:** `std::vector<int>`



### `g(&CloseClipboard)`

**Returns:** `Utils::ScopeGuard`



### `while(true)`

**Returns:** ``



### `GetClipboardFormats()`

**Returns:** `std::vector<Resource::GID::Type>`



### `for(auto format : formats)`

**Returns:** ``



### `if(format == cf_html)`

**Returns:** `else`



### `if(format == CF_HDROP)`

**Returns:** `else`



### `if(format == cf_urilist)`

**Returns:** `else`



### `if(format == CF_TEXT || format == CF_UNICODETEXT)`

**Returns:** `else`



### `switch(format)`

**Returns:** ``



### `CloseClipboard()`

**Returns:** ``



### `SetClipboardText(const std::string &text, Resource::GID::Type type, bool unicode, bool append)`

**Returns:** `void`



### `g(&CloseClipboard)`

**Returns:** `Utils::ScopeGuard`



### `if(!append)`

**Returns:** ``



### `EmptyClipboard()`

**Returns:** ``



### `if(type == Resource::GID::Text)`

**Returns:** ``



### `GlobalUnlock(clipbuffer)`

**Returns:** ``



### `if(unicode)`

**Returns:** ``



### `GlobalUnlock(clipbuffer)`

**Returns:** ``



### `SetClipboardData(CF_UNICODETEXT, cbu)`

**Returns:** ``



### `SetClipboardData(CF_TEXT, clipbuffer)`

**Returns:** ``



### `if(type == Resource::GID::HTML)`

**Returns:** `else`



### `GlobalUnlock(clipbuffer)`

**Returns:** ``



### `SetClipboardData(cf_html, clipbuffer)`

**Returns:** ``



### `GetClipboardText(Resource::GID::Type type)`

**Returns:** `std::string`



### `g(&CloseClipboard)`

**Returns:** `Utils::ScopeGuard`



### `if(type == Resource::GID::Text)`

**Returns:** ``



### `if(clip == nullptr)`

**Returns:** ``



### `if(type == Resource::GID::HTML)`

**Returns:** `else`



### `if(unicode)`

**Returns:** ``



### `GetClipboardList(Resource::GID::Type type)`

**Returns:** `std::vector<std::string>`



### `g(&CloseClipboard)`

**Returns:** `Utils::ScopeGuard`



### `if(type == Resource::GID::FileList)`

**Returns:** ``



### `if(clip != nullptr)`

**Returns:** ``



### `while(widetext[0])`

**Returns:** ``



### `if(type == Resource::GID::URIList)`

**Returns:** `else`



### `if(clip != nullptr)`

**Returns:** ``



### `if(data[i] == '\n')`

**Returns:** ``



### `if(i-last > 0)`

**Returns:** ``



### `if(data[i] == '\r')`

**Returns:** `else`



### `if(clip != nullptr)`

**Returns:** ``



### `while(widetext[0])`

**Returns:** ``



### `SetClipboardList(std::vector<std::string> list, Resource::GID::Type type, bool append)`

**Returns:** `void`



### `g(&CloseClipboard)`

**Returns:** `Utils::ScopeGuard`



### `if(!append)`

**Returns:** ``



### `EmptyClipboard()`

**Returns:** ``



### `if(type == Resource::GID::FileList)`

**Returns:** ``



### `for(auto &e : list)`

**Returns:** ``



### `if(!first)`

**Returns:** ``



### `memcpy(str, "file://", 7)`

**Returns:** ``



### `GlobalUnlock(uri)`

**Returns:** ``



### `SetClipboardData(cf_urilist, uri)`

**Returns:** ``



### `for(auto &e : list)`

**Returns:** ``



### `GlobalUnlock(clipbuffer)`

**Returns:** ``



### `SetClipboardData(CF_HDROP, clipbuffer)`

**Returns:** ``



### `if(type == Resource::GID::URIList)`

**Returns:** `else`



### `for(auto &e : list)`

**Returns:** ``



### `if(!first)`

**Returns:** ``



### `GlobalUnlock(uri)`

**Returns:** ``



### `SetClipboardData(cf_urilist, uri)`

**Returns:** ``



### `GetClipboardBitmap()`

**Returns:** `Containers::Image`



### `for(const auto &w : Window::Windows)`

**Returns:** ``



### `if(d && d->handle == owner)`

**Returns:** ``



### `for(auto &e : clipboard_entries)`

**Returns:** ``



### `if(e.type == cf_png)`

**Returns:** ``



### `g(&CloseClipboard)`

**Returns:** `Utils::ScopeGuard`



### `if(clip)`

**Returns:** ``



### `GlobalUnlock(clip)`

**Returns:** ``



### `CloseClipboard()`

**Returns:** ``



### `if(clip)`

**Returns:** ``



### `GlobalUnlock(clip)`

**Returns:** ``



### `CloseClipboard()`

**Returns:** ``



### `if(clip)`

**Returns:** ``



### `ms(data, data+sz)`

**Returns:** `IO::MemoryInputStream`



### `GlobalUnlock(clip)`

**Returns:** ``



### `CloseClipboard()`

**Returns:** ``



### `if(clip)`

**Returns:** ``



### `ms(data, data+sz)`

**Returns:** `IO::MemoryInputStream`



### `GlobalUnlock(clip)`

**Returns:** ``



### `CloseClipboard()`

**Returns:** ``



### `SetClipboardBitmap(Containers::Image img, bool append)`

**Returns:** `void`



### `for(const auto &w : Window::Windows)`

**Returns:** ``



### `if(d && d->handle)`

**Returns:** ``



### `g(&CloseClipboard)`

**Returns:** `Utils::ScopeGuard`



### `if(!append)`

**Returns:** ``



### `EmptyClipboard()`

**Returns:** ``



### `SetClipboardData(cf_g_bmp, nullptr)`

**Returns:** ``



### `SetClipboardData(cf_png, nullptr)`

**Returns:** ``



### `SetClipboardData(CF_DIB, nullptr)`

**Returns:** ``



### `renderformat(unsigned type)`

**Returns:** `void`



### `for(auto &e : WindowManager::clipboard_entries)`

**Returns:** ``



### `if(e.type == type)`

**Returns:** ``



### `if(e.type == WindowManager::cf_png)`

**Returns:** ``



### `GlobalUnlock(clipbuffer)`

**Returns:** ``



### `SetClipboardData(type, clipbuffer)`

**Returns:** ``



### `if(e.type == CF_DIB)`

**Returns:** `else`



### `GlobalUnlock(clipbuffer)`

**Returns:** ``



### `SetClipboardData(type, clipbuffer)`

**Returns:** ``



### `if(e.type == WindowManager::cf_g_bmp)`

**Returns:** `else`



### `GlobalUnlock(clipbuffer)`

**Returns:** ``



### `SetClipboardData(type, clipbuffer)`

**Returns:** ``



### `make_clipboarddata(T_ data)`

**Returns:** `std::shared_ptr<CopyFreeAny>`


@cond internal


### `getclipboardformats()`

**Returns:** `std::vector<Atom>`



### `if(windowhandle==0)`

**Returns:** ``



### `for(auto &w : Window::Windows)`

**Returns:** ``



### `if(data && data->handle == owner)`

**Returns:** ``



### `for(auto &d : clipboard_entries)`

**Returns:** ``



### `XConvertSelection(display, XA_CLIPBOARD, XA_TARGETS, XA_CP_PROP, windowhandle, CurrentTime)`

**Returns:** ``



### `XFlush(display)`

**Returns:** ``



### `if(event.xselection.property == XA_CP_PROP)`

**Returns:** ``



### `XGetWindowProperty(display, windowhandle, XA_CP_PROP, 0, 0, 0, XA_ATOM, &type, &format, &len, &bytes, &data)`

**Returns:** ``



### `if(bytes)`

**Returns:** ``



### `for(int i=0;i<bytes/4;i++)`

**Returns:** ``



### `XFree(data)`

**Returns:** ``



### `XDeleteProperty(display, windowhandle, XA_CP_PROP)`

**Returns:** ``



### `handleselectionrequest(XEvent event)`

**Returns:** `void`



### `if(event.xselectionrequest.selection==WindowManager::XA_CLIPBOARD)`

**Returns:** ``



### `if(event.xselectionrequest.target==WindowManager::XA_TARGETS)`

**Returns:** ``



### `for(auto &d : WindowManager::clipboard_entries)`

**Returns:** ``



### `for(auto &d : WindowManager::clipboard_entries)`

**Returns:** ``



### `if(d.type == event.xselectionrequest.target)`

**Returns:** ``



### `if(entry)`

**Returns:** ``



### `if(entry->type == WindowManager::XA_PNG)`

**Returns:** `else`



### `if(entry->type == WindowManager::XA_JPG)`

**Returns:** `else`



### `if(entry->type == WindowManager::XA_BMP)`

**Returns:** `else`



### `XSendEvent(WindowManager::display, event.xselectionrequest.requestor, 0, 0, &respond)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `handleclipboardevent(XEvent event)`

**Returns:** `void`



### `switch(event.type)`

**Returns:** ``



### `handleselectionrequest(event)`

**Returns:** ``



### `GetClipboardFormats()`

**Returns:** `std::vector<Resource::GID::Type>`


@endcond


### `for(auto atom : list)`

**Returns:** ``



### `if(atom == XA_Filelist)`

**Returns:** `else`



### `GetClipboardText(Resource::GID::Type requesttype)`

**Returns:** `std::string`



### `if(windowhandle==0)`

**Returns:** ``



### `for(auto atom : list)`

**Returns:** ``



### `if(requesttype == Resource::GID::Text && atom == XA_UTF8_STRING)`

**Returns:** ``



### `if(requesttype == Resource::GID::Text && atom == XA_STRING)`

**Returns:** `else`



### `if(requesttype == Resource::GID::Text && atom == XA_TEXT && request != XA_STRING)`

**Returns:** `else`



### `if(requesttype == Resource::GID::HTML && atom == XA_TEXT_HTML)`

**Returns:** `else`



### `if(requesttype == Resource::GID::URL && atom == XA_URL)`

**Returns:** `else`



### `for(auto &w : Window::Windows)`

**Returns:** ``



### `if(data && data->handle == owner)`

**Returns:** ``



### `for(auto &d : clipboard_entries)`

**Returns:** ``



### `if(d.type == request)`

**Returns:** ``



### `XConvertSelection(display, XA_CLIPBOARD, request, XA_CP_PROP, windowhandle, CurrentTime)`

**Returns:** ``



### `XFlush(display)`

**Returns:** ``



### `if(event.xselection.property == XA_CP_PROP)`

**Returns:** ``



### `XGetWindowProperty(display, windowhandle, XA_CP_PROP, 0, 0, 0, AnyPropertyType, &type, &format, &len, &bytes, &data)`

**Returns:** ``



### `if(bytes)`

**Returns:** ``



### `XFree(data)`

**Returns:** ``



### `XDeleteProperty(display, windowhandle, XA_CP_PROP)`

**Returns:** ``



### `SetClipboardText(const std::string &text, Resource::GID::Type type, bool unicode, bool append)`

**Returns:** `void`



### `if(type == Resource::GID::Text)`

**Returns:** ``



### `if(unicode)`

**Returns:** ``



### `if(type == Resource::GID::HTML)`

**Returns:** `else`



### `if(type == Resource::GID::URL)`

**Returns:** `else`



### `XSetSelectionOwner(display, XA_CLIPBOARD, windowhandle, CurrentTime)`

**Returns:** ``



### `XFlush(display)`

**Returns:** ``



### `GetClipboardList(Resource::GID::Type requesttype)`

**Returns:** `std::vector<std::string>`



### `if(windowhandle==0)`

**Returns:** ``



### `for(auto atom : list)`

**Returns:** ``



### `for(auto &w : Window::Windows)`

**Returns:** ``



### `if(wdata && wdata->handle == owner)`

**Returns:** ``



### `for(auto &d : clipboard_entries)`

**Returns:** ``



### `if(d.type == request)`

**Returns:** ``



### `if(d.type == WindowManager::XA_Filelist)`

**Returns:** ``



### `if(!data)`

**Returns:** ``



### `XConvertSelection(display, XA_CLIPBOARD, request, XA_CP_PROP, windowhandle, CurrentTime)`

**Returns:** ``



### `XFlush(display)`

**Returns:** ``



### `if(data || event.xselection.property == XA_CP_PROP)`

**Returns:** ``



### `XGetWindowProperty(display, windowhandle, XA_CP_PROP, 0, 0, 0, AnyPropertyType, &type, &format, &len, &bytes, &data)`

**Returns:** ``



### `if(bytes)`

**Returns:** ``



### `if(data)`

**Returns:** ``



### `if(i-p>1)`

**Returns:** ``



### `if(requesttype == Resource::GID::FileList)`

**Returns:** ``



### `if(requesttype == Resource::GID::URIList)`

**Returns:** `else`



### `if(bytes)`

**Returns:** ``



### `XFree(data)`

**Returns:** ``



### `XDeleteProperty(display, windowhandle, XA_CP_PROP)`

**Returns:** ``



### `SetClipboardList(std::vector<std::string> list, Resource::GID::Type type, bool append)`

**Returns:** `void`



### `if(type == Resource::GID::FileList)`

**Returns:** ``



### `for(auto &e : list)`

**Returns:** ``



### `XSetSelectionOwner(display, XA_CLIPBOARD, windowhandle, CurrentTime)`

**Returns:** ``



### `XFlush(display)`

**Returns:** ``



### `if(type == Resource::GID::URIList)`

**Returns:** `else`



### `for(auto &e : list)`

**Returns:** ``



### `XSetSelectionOwner(display, XA_CLIPBOARD, windowhandle, CurrentTime)`

**Returns:** ``



### `XFlush(display)`

**Returns:** ``



### `GetClipboardBitmap()`

**Returns:** `Containers::Image`



### `if(windowhandle==0)`

**Returns:** ``



### `for(auto &w : Window::Windows)`

**Returns:** ``



### `if(wdata && wdata->handle == owner)`

**Returns:** ``



### `for(auto &d : clipboard_entries)`

**Returns:** ``



### `if(d.type == XA_PNG || d.type == XA_BMP || d.type == XA_JPG)`

**Returns:** ``



### `for(auto atom : list)`

**Returns:** ``



### `if(atom == XA_PNG)`

**Returns:** ``



### `if(atom == XA_BMP)`

**Returns:** `else`



### `if(request == 0 && atom == XA_JPG)`

**Returns:** `else`



### `XConvertSelection(display, XA_CLIPBOARD, request, XA_CP_PROP, windowhandle, CurrentTime)`

**Returns:** ``



### `XFlush(display)`

**Returns:** ``



### `if(event.xselection.property == XA_CP_PROP)`

**Returns:** ``



### `if(type == XA_INCR)`

**Returns:** ``



### `while(true)`

**Returns:** ``



### `XFlush(display)`

**Returns:** ``



### `XFlush(display)`

**Returns:** ``



### `if(!bytes)`

**Returns:** ``



### `memcpy(&imgdata[cur], data, bytes)`

**Returns:** ``



### `XFree(data)`

**Returns:** ``



### `if(request == XA_PNG)`

**Returns:** ``



### `if(request == XA_BMP)`

**Returns:** `else`



### `if(request == XA_JPG)`

**Returns:** `else`



### `if(bytes)`

**Returns:** `else`



### `if(request == XA_PNG)`

**Returns:** ``



### `if(request == XA_BMP)`

**Returns:** `else`



### `if(request == XA_JPG)`

**Returns:** `else`



### `XFree(data)`

**Returns:** ``



### `SetClipboardBitmap(Containers::Image img, bool append)`

**Returns:** `void`



### `XSetSelectionOwner(display, XA_CLIPBOARD, windowhandle, CurrentTime)`

**Returns:** ``



### `XFlush(display)`

**Returns:** ``


