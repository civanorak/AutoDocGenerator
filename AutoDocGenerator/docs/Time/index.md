# Time

&gt; Auto-generated documentation for the **Time** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Date`

**Namespace:** `Time`

This class represents a specific date including time information. Can be obtained using GetDateTime function. An Empty month marks the time as unset.

#### Methods

##### `Date(const std::string &isodate)`

**Returns:** ``

Default constructor, zero initializes the class, making it an unset time. Creates a new date object from the given ISO-8601 date string. @see Parse @throw std::runtime_error if the string is malformed or data is not valid

##### `Date(std::istream &source)`

**Returns:** `explicit`

Reads a new date object from a binary stream. @see Save for details. @throw std::runtime_error if checksum is wrong or data is not valid

##### `Date(time_t systemtime)`

**Returns:** ``

##### `Save(std::ostream &target)`

**Returns:** `bool`

Writes date object to a binary stream. Format is given below. numbers after names are number of bytes. @verbatim &lt;year:2&gt;&lt;month:1&gt;&lt;day:1&gt;&lt;hour:1&gt;&lt;minute:1&gt;&lt;millis:2&gt;&lt;timezone:2&gt;&lt;checksum:1&gt; @endverbatim checksum is the sum of all numbers in base 256. @return true if successful. An empty date will be saved correctly.

##### `Load(std::istream &source)`

**Returns:** `bool`

Loads date object from a binary stream. @see Save for details. @return true if successful.

##### `Parse(std::string isodate)`

**Returns:** `bool`

Creates a new date object from the given ISO-8601 date string. Requires full information. Following format is recognized: [YYYY]-[MM]-[DD]T[HH]:[mm]:[SS](+/-)[TT][tt] * YYYY: 4 digit year * MM  : 2 digit month * DD  : 2 digit day * HH  : 2 digit hour * mm  : 2 digit minute * SS  : 2 digit second * TT  : 2 digit timezone hour * tt  : 2 digit timezone minute Timezone is optional, if omitted default is system timezone. It can also be specified as Z meaning UTC. @return true if successful.

##### `ISODate(—)`

**Returns:** `std::string`

ISO compliant date format. Contains only date

##### `ISODateTime(bool timezone = true)`

**Returns:** `std::string`

ISO compliant date/time. This format should be used to serialize as text.

##### `Date_En(—)`

**Returns:** `std::string`

Returns currently stored month's name in English. Month 0 is valid and returns "". @throw std::logic_error (debug only) if month is invalid. Returns currently stored month's int name in English. Month 0 is valid and returns "". @throw std::logic_error (debug only) if month is invalid. Returns currently stored week day's name in English. @throw std::logic_error (debug only) if weekday is invalid. Returns currently stored week day's int name in English. @throw std::logic_error (debug only) if weekday is invalid. Returns stored date in `day monthname year, weekday` format with English names for month and weekday.

##### `ShortDate_En(—)`

**Returns:** `std::string`

Returns stored date in `day intmonthname year` format with English names for month.

##### `Time(—)`

**Returns:** `std::string`

Returns stored time in `hour:minute:second` format.

##### `ShortTime(—)`

**Returns:** `std::string`

Returns stored time in `hour:minute` format.

##### `Timezone_GMT(—)`

**Returns:** `std::string`

Returns stored timezone. Format depends on the actual timezone. If the timezone offset contains only hours, the format is `GMT+H` or `GMT-H`. If there is minute offset, timezone is returned in `GMT+H:MM` or `GMT-H:MM` format. H is the hour without any leading zeroes, MM is the minute in two digit format.

##### `SystemTime(—)`

**Returns:** `time_t`

##### `static` `LocalTimezone(—)`

**Returns:** `static int`

Returns the system timezone in minutes. Might be negative.

##### `AddYears(int years)`

**Returns:** `void`

Adds specified amount of years to the date

##### `AddMonths(int months)`

**Returns:** `void`

Adds specified amount of months to the date

##### `AddDays(int days)`

**Returns:** `void`

Adds specified amount of days to the date

##### `AddHours(int hours)`

**Returns:** `void`

Adds specified amount of hours to the date

##### `AddMinutes(int minutes)`

**Returns:** `void`

Adds specified amount of minutes to the date

##### `AddSeconds(int seconds)`

**Returns:** `void`

Adds specified amount of seconds to the date

##### `IsSet(—)`

**Returns:** `bool`

Checks whether the stored time is actually set.

##### `static` `Now(—)`

**Returns:** `static Date`

Returns current time

##### `GetDate(—)`

**Returns:** `return`

##### `Unset(—)`

**Returns:** `void`

Gives the difference between two dates. Compares 2 dates Unsets the stored time

##### `DetermineWeekday(—)`

**Returns:** `bool`

Determines the weekday from the stored date. @return true if successful


---

## Enums

### `WeekdayType`

**Namespace:** `Time`

Days of week. Starts from sunday


### `MonthType`

**Namespace:** `Time`

Months, january is 1.


---

## Functions

### `Initialize()`

**Returns:** `void`



### `totm(const Date &d)`

**Returns:** `tm`



### `fromtm(Date &ret, tm timeinfo)`

**Returns:** `void`



### `fromtm(*this, inf)`

**Returns:** ``



### `mktime(&t)`

**Returns:** `return`



### `if(isodate[19]=='Z')`

**Returns:** `else`



### `catch(...)`

**Returns:** ``



### `DetermineWeekday()`

**Returns:** `return`



### `if(csource!=c)`

**Returns:** ``



### `DetermineWeekday()`

**Returns:** `return`



### `if(timezone)`

**Returns:** ``



### `if(Month > Dec)`

**Returns:** ``



### `if(Month > Dec)`

**Returns:** ``



### `if(Timezone % 60 == 0)`

**Returns:** ``



### `time(&time_local)`

**Returns:** ``



### `difftime(x, y)`

**Returns:** `return`



### `mktime(&a)`

**Returns:** ``



### `fromtm(*this, a)`

**Returns:** ``



### `mktime(&a)`

**Returns:** ``



### `fromtm(*this, a)`

**Returns:** ``



### `mktime(&a)`

**Returns:** ``



### `fromtm(*this, a)`

**Returns:** ``



### `mktime(&a)`

**Returns:** ``



### `fromtm(*this, a)`

**Returns:** ``



### `mktime(&a)`

**Returns:** ``



### `fromtm(*this, a)`

**Returns:** ``



### `mktime(&a)`

**Returns:** ``



### `fromtm(*this, a)`

**Returns:** ``



### `Initialize()`

**Returns:** `void`


Initializes Time module.


### `GetDate()`

**Returns:** `Date`


Returns the current date. Should not be used for performance calculations, its not guaranteed to be precise.


### `GetTime()`

**Returns:** `unsigned long`


Full year Month starts from jan = 1 Day in month Hour in 24 hour format Minute Second This value is from the last second tick. Day of the week, starts from sunday = 0 Timezone in minutes, can be negative. Note that some time zones has minute offset. Output stream operator overload Returns current time in milliseconds. @warning FrameStart should be used unless exact time is required. This function works slower and changes during a frame, which may cause synchronization issues.


### `FrameStart()`

**Returns:** `inline unsigned long`


@endcond Returns start time of the current frame in milliseconds. This function should be used for animations and effects as it is constant throughout a frame.


### `DeltaTime()`

**Returns:** `inline unsigned long`


Returns the time passed since the last frame. This value is updated at the start of the frame.

