# Polygon

> Auto-generated documentation for the **Polygon** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `ScanLineDrawOrder`

**Namespace:** `internal`

This structure is sent to ScanLine drawing functions.


### `edge`

**Namespace:** `internal`


### `activeline`

**Namespace:** `internal`


---

## Enums

### `polygonstrictmode`

**Namespace:** `internal`

Start painting from this point Continue painting until this point Path index


---

## Functions

### `findpolylinestofill(const PL_ &pointlist, int ymin, int ymax, F_ fn, Float cover = 1, Float scale = 1)`

**Returns:** `void`


ymin, ymax should be prescaled, pointlist will be scaled on the fly. W_ is winding, 0 is non zero, 1 is odd, 2 is non-zero on same path, odd on different path.


### `for(const auto &points : pointlist)`

**Returns:** ``



### `if(N <= 2)`

**Returns:** ``



### `for(int i=0; i<N; i++)`

**Returns:** ``



### `for(int y = ymin; y<ymax; y++)`

**Returns:** ``



### `while(it != end)`

**Returns:** ``



### `if(!winding)`

**Returns:** ``



### `if(W_ == 0)`

**Returns:** ``



### `if(W_ == 1)`

**Returns:** `else`



### `if(W_ == 2)`

**Returns:** `else`



### `if(it->index != index)`

**Returns:** ``



### `if(winding == 0 && start < nx)`

**Returns:** ``



### `for(auto &a : activelines)`

**Returns:** ``



### `fn(y, drawlist)`

**Returns:** ``



### `Polyfill(Containers::Image &target, const Containers::Collection<const Geometry::PointList<P_>> &points, F_ fill = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`


@endcond


### `for(const auto &p : points)`

**Returns:** ``



### `if(S_ >= 1)`

**Returns:** ``



### `cnts(ew)`

**Returns:** `std::vector<int>`



### `for(const auto &d : drawlist)`

**Returns:** ``



### `FitInto(s, xmin*S_, xmax*S_+S_)`

**Returns:** ``



### `FitInto(e, xmin*S_, xmax*S_+S_)`

**Returns:** ``



### `for(int x=s; x<e; x++)`

**Returns:** ``



### `if(y%S_ == S_-1 || y == targety-1)`

**Returns:** ``



### `for(int x=0; x<ew; x++)`

**Returns:** ``



### `if(cnts[x])`

**Returns:** ``



### `for(const auto &d : drawlist)`

**Returns:** ``



### `for(int x=s; x<e; x++)`

**Returns:** ``



### `Polyfill(Containers::Image &target, const std::vector<Geometry::PointList<P_>> &points, F_ fill = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`



### `for(const auto &pl : points)`

**Returns:** ``



### `Polyfill(Graphics::Bitmap &target, const std::vector<Geometry::PointList<P_>> &points, F_ fill = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`



### `Polyfill(Containers::Image &target, const Geometry::PointList<P_> &points, F_ fill = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`



### `Polyfill(Graphics::Bitmap &target, const Geometry::PointList<P_> &points, F_ fill = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`



### `Rectangle(Containers::Image &target, const Geometry::basic_Rectangle<typename P_::BaseType> &rect, F_ fill = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`



### `Rectangle(Graphics::Bitmap &target, const Geometry::basic_Rectangle<typename P_::BaseType> &rect, F_ fill = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`


