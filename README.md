# PyAngle

> A simple package for angle calculation

## use `pip install PyAngle`

# class Angle

> Designed especially for angle in the form of DMS(Degree, Minute and Second)
>
> immutable object
>
> default: public, non-static

## Member Variables

- `int degree`
- `int minute`
- `float second`

## Member Methods

### Override

- [x] `__init__(form, degree, minute, second, rad, x, y)`
- [x] `__add__(self, other)`: "+"
- [x] `__sub__(self, other)`: "-"
- [x] `__mul__(self, n)`: "\*"
- [x] `__truediv__(self, n)`: "/"
- [x] `__floordiv__(self, n)`: "//"
- [x] `__mod__(self, other)`: "%
- [x] `__str__(self)`
- [x] `__cmp__(self, other)`
- [x] `__eq__(self, other)`: "=="
- [x] `__ne__(self, other)`: "!="
- [x] `__le__(self, other)`: "<="
- [x] `__lt__(self, other)`: "<"
- [x] `__ge__(self, other)`: ">="
- [x] `__gt__(self, other)`: ">"

### Creator

- [x] `createByDMS(degree, minute, second)`
- [x] `createByDegree(degree)`
- [x] `createByRadian(rad)`
- [x] `createByXY(x, y)`

### Mutator

- [x] `void adjust()`: 调整格式

### Producer

#### Calculators

- [x] `float sin()`
- [x] `float cos()`
- [x] `float tan()`

### Observer

#### Getters

- [x] `int getDegree()`
- [x] `int getMinute()`
- [x] `float getSecond()`

#### Switchers

- [x] `float toDegrees()`
- [x] `float toRadians()`
- [x] `(float, float) toXY(x, y)`: 坐标，x、y 两者之一不为 0
- [x] `String toString(format)`: 指定格式输出字符串，默认`xxx°xxx′xxx″`

#### Judges

- [x] `bool isZeroAngle()`: 零角
- [x] `bool isAcuteAngle()`: 锐角
- [x] `bool isRightAngle()`: 直角
- [x] `bool isObtuseAngle()`: 钝角
- [x] `bool isStraightAngle()`: 平角
- [x] `bool isMajorAngle()`: 优角
- [x] `bool isMinorAngle()`: 劣角

### Static Methods

#### Producer

- [ ] `Angle[] toAnglesFromXYs((float, float)[] angles)`: 参数为(x, y)元组的列表
- [ ] `Angle[] toAnglesFromDegrees(float[] angles)`: 参数为 degree 元组的列表
- [ ] `Angle[] toAnglesFromRads(float[] angles)`: 参数为 rad 元组的列表
- [ ] `(float, float)[] toXYsFromAngles(Angle[] angles)`
- [ ] `float[] toDegreesFromAngles(Angle[] angles)`
- [ ] `float[] toRadsFromAngles(Angle[] angles)`
- [ ] `Angle[] sort(Angle[] angles, bool reverse)`

#### Chooser

- [ ] `Angle getBiggerAngle(angle1, angle2)`
- [ ] `Angle getSmallerAngle(angle1, angle2)`
- [ ] `Angle getNearestAngle(Angle angle, Angle[] angles)`: 在`angles`中找到与`angle`最近的角
- [ ] `Angle getFurthestAngle(Angle angle, Angle[] angles)`: 在`angles`中找到与`angle`最远的角
