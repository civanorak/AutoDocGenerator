# ColorSpaces

> Auto-generated documentation for the **ColorSpaces** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `XYZAf`

**Namespace:** `Gorgon`

#### Methods

##### `XYZAf(—)`

**Returns:** ``

Data type for each channel Default constructor zero initializes the color except for alpha which is set to 1.

##### `XYZAf(RGBAf other)`

**Returns:** ``

Fills all channels

##### `RGBAf(—)`

**Returns:** `operator`


### `LuvAf`

**Namespace:** `Gorgon`

X color channel Y color channel Z color channel Alpha color channel

#### Methods

##### `LuvAf(—)`

**Returns:** ``

Data type for each channel Default constructor zero initializes the color except for alpha which is set to 1.

##### `LuvAf(XYZAf other)`

**Returns:** ``

Fills all channels

##### `LuvAf(RGBAf other)`

**Returns:** ``

##### `XYZAf(—)`

**Returns:** `operator`

##### `RGBAf(—)`

**Returns:** `operator`


### `LabAf`

**Namespace:** `Gorgon`

Luminance channel u color channel v color channel Alpha color channel

#### Methods

##### `LabAf(—)`

**Returns:** ``

Data type for each channel Defaalt constractor zero initializes the color except for alpha which is set to 1.

##### `LabAf(XYZAf other)`

**Returns:** ``

Fills all channels

##### `LabAf(RGBAf other)`

**Returns:** ``

##### `XYZAf(—)`

**Returns:** `operator`

##### `RGBAf(—)`

**Returns:** `operator`


### `HCLAf`

**Namespace:** `Gorgon`

Luminance channel a color channel b color channel Alpha color channel

#### Methods

##### `HCLAf(—)`

**Returns:** ``

Data type for each channel Default constructor zero initializes the color except for alpha which is set to 1.

##### `HCLAf(LuvAf other)`

**Returns:** ``

Fills all channels

##### `HCLAf(XYZAf other)`

**Returns:** ``

##### `HCLAf(RGBAf other)`

**Returns:** ``

##### `LuvAf(—)`

**Returns:** `operator`

##### `XYZAf(—)`

**Returns:** `operator`

##### `RGBAf(—)`

**Returns:** `operator`


### `LChAf`

**Namespace:** `Gorgon`

hue channel Chromacity channel Luminance color channel Alpha color channel

#### Methods

##### `LChAf(—)`

**Returns:** ``

Data type for each channel Default constructor zero initializes the color except for alpha which is set to 1.

##### `LChAf(LabAf other)`

**Returns:** ``

Fills all channels

##### `LChAf(XYZAf other)`

**Returns:** ``

##### `LChAf(RGBAf other)`

**Returns:** ``

##### `LabAf(—)`

**Returns:** `operator`

##### `XYZAf(—)`

**Returns:** `operator`

##### `RGBAf(—)`

**Returns:** `operator`


---

## Functions

### `RGBToXYZ(RGBAf color)`

**Returns:** `XYZAf`



### `perform(color.R)`

**Returns:** ``



### `perform(color.G)`

**Returns:** ``



### `perform(color.B)`

**Returns:** ``



### `XYZToRGB(XYZAf color, bool unbounded)`

**Returns:** `RGBAf`



### `FitInto(c, 0.f, 1.f)`

**Returns:** ``



### `perform(c.R)`

**Returns:** ``



### `perform(c.G)`

**Returns:** ``



### `perform(c.B)`

**Returns:** ``



### `XYZToLuv(XYZAf color)`

**Returns:** `LuvAf`



### `LuvToXYZ(LuvAf color)`

**Returns:** `XYZAf`



### `XYZToLab(XYZAf color)`

**Returns:** `LabAf`



### `perform(color.X, 95.047f)`

**Returns:** ``



### `perform(color.Y, 100.f)`

**Returns:** ``



### `perform(color.Z, 108.883f)`

**Returns:** ``



### `LabToXYZ(LabAf color)`

**Returns:** `XYZAf`



### `perform(c.X, 95.047f)`

**Returns:** ``



### `perform(c.Y, 100.f)`

**Returns:** ``



### `perform(c.Z, 108.883f)`

**Returns:** ``



### `LuvToLCh(LuvAf color)`

**Returns:** `HCLAf`



### `LChToLuv(HCLAf color)`

**Returns:** `LuvAf`



### `LabToLCh(LabAf color)`

**Returns:** `LChAf`



### `LChToLab(LChAf color)`

**Returns:** `LabAf`



### `RGBAf()`

**Returns:** `XYZAf::operator`



### `XYZToRGB(*this)`

**Returns:** `return`



### `XYZAf()`

**Returns:** `LuvAf::operator`



### `LuvToXYZ(*this)`

**Returns:** `return`



### `RGBAf()`

**Returns:** `LuvAf::operator`



### `XYZToRGB(*this)`

**Returns:** `return`



### `LuvAf()`

**Returns:** `HCLAf::operator`



### `LChToLuv(*this)`

**Returns:** `return`



### `XYZAf()`

**Returns:** `HCLAf::operator`



### `LuvToXYZ(*this)`

**Returns:** `return`



### `RGBAf()`

**Returns:** `HCLAf::operator`



### `XYZToRGB(*this)`

**Returns:** `return`



### `XYZAf()`

**Returns:** `LabAf::operator`



### `LabToXYZ(*this)`

**Returns:** `return`



### `RGBAf()`

**Returns:** `LabAf::operator`



### `LabToXYZ(*this)`

**Returns:** `return`



### `LabAf()`

**Returns:** `LChAf::operator`



### `LChToLab(*this)`

**Returns:** `return`



### `XYZAf()`

**Returns:** `LChAf::operator`



### `LabToXYZ(*this)`

**Returns:** `return`



### `RGBAf()`

**Returns:** `LChAf::operator`



### `XYZToRGB(*this)`

**Returns:** `return`



### `RGBToXYZ(RGBAf color)`

**Returns:** `XYZAf`


Luminance color channel Chromacity channel hue channel Alpha color channel Converts a color in RGB color space to XYZ color space.


### `XYZToRGB(XYZAf color, bool unbounded = false)`

**Returns:** `RGBAf`


Converts a color in XYZ color space to RGB color space..


### `XYZToLuv(XYZAf color)`

**Returns:** `LuvAf`


Converts a color in XYZ color space to CIE Luv color space.


### `LuvToXYZ(LuvAf color)`

**Returns:** `XYZAf`


Converts a color in CIE Luv color space to XYZ color space.


### `XYZToLab(XYZAf color)`

**Returns:** `LabAf`


Converts a color in XYZ color space to CIE Lab color space.


### `LabToXYZ(LabAf color)`

**Returns:** `XYZAf`


Converts a color in CIE Lab color space to XYZ color space.


### `LuvToLCh(LuvAf color)`

**Returns:** `HCLAf`


Converts a color in CIE Luv color space to CIE LCh_uv color space.


### `LChToLuv(HCLAf color)`

**Returns:** `LuvAf`


Converts a color in CIE LCh_uv color space to CUE Luv color space.


### `LabToLCh(LabAf color)`

**Returns:** `LChAf`


Converts a color in CIE Lab color space to CIE LCh_ab color space.


### `LChToLab(LChAf color)`

**Returns:** `LabAf`


Converts a color in CIE LCh_ab color space to CUE Lab color space.

