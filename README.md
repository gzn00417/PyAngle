# PyAngle

![https://img.shields.io/badge/license-Apache%202.0-blue.svg?longCache=true&style=flat-square](https://img.shields.io/badge/license-Apache%202.0-blue.svg?longCache=true&style=flat-square)

> A simple package for angle calculation

# class Angle

> immutable object
> default: public, non-static

## Member Variables

- `int degree`
- `int minute`
- `float second`

## Member Methods

### Override

- [x] `__init__(form, degree, minute, second, rad, x, y)`
- [x] `__add__(self, other)`
- [x] `__sub__(self, other)`
- [x] `__mul__(self, n)`
- [x] `__truediv__(self, n)`: "/"
- [x] `__floordiv__(self, n)`: "//"
- [x] `__mod__(self, other)`
- [ ] `__str__(self)`
- [ ] `__cmp__(self, other)`

### Creator

- [x] `createByDMS(degree, minute, second)`
- [x] `createByDegree(degree)`
- [x] `createByRadian(rad)`
- [x] `createByXY(x, y)`

### Mutator

- [x] `void adjust()`: 调整格式

### Producer

#### Calculators

- [ ] `Angle add(anotherAngle)`: 加法
- [ ] `Angle sub(anotherAngle)`: 减法
- [ ] `Angle mul(n)`: 乘法
- [ ] `Angle div(n)`: 除法
- [ ] `float sin()`
- [ ] `float cos()`
- [ ] `float tan()`

### Observer

#### Getters

- [x] `int getDegree()`
- [x] `int getMinute()`
- [x] `float getSecond()`

#### Switchers

- [ ] `float toDegrees()`
- [ ] `float toRadians()`
- [ ] `(float, float) toCoorOfXY(x, y)`: 坐标，x、y 两者之一不为 0
- [ ] `String toString(format)`: 指定格式输出字符串，默认`xxx°xxx′xxx″`

#### Judges

- [ ] `bool isZeroAngle()`: 零角
- [ ] `bool isAcuteAngle()`: 锐角
- [ ] `bool isRightAngle()`: 直角
- [ ] `bool isObtuseAngle()`: 钝角
- [ ] `bool isStraightAngle()`: 平角
- [ ] `bool isMajorAngle()`: 优角
- [ ] `bool isMinorAngle()`: 劣角
- [ ] `bool isBiggerThan(anotherAngle)`
- [ ] `bool isSmallerThan(anotherAngle)`
- [ ] `bool isEqual(anotherAngle)`

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
