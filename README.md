# PyAngle

> A simple package for angle calculation

## Use

```
pip install PyAngle
```

# class Angle

> Designed especially for angle in the form of DMS(Degree, Minute and Second)
>
> immutable object
>
> default: public, non-static

## APIs

### Creators

```python
>>> a1 = Angle.from_dms(deg=30, min=20, sec=10)
>>> a2 = Angle.from_degrees(degrees=60)
>>> a3 = Angle.from_rad(rad=1.23)
>>> a4 = Angle.from_atan2(x=0.7, y=0.8)
```

- [x] `from_dms(deg, min=0, sec=0) -> Angle`
- [x] `from_degrees(degrees) -> Angle`
- [x] `from_rad(rad) -> Angle`
- [x] `from_atan2(x, y) -> Angle`

### Operators

```python
>>> str(a1 + a2)
'90 20 10.00'
>>> str(a3 % a4)
'21 39 35.04'
>>> angle_list = [a1, a2, a3, a4]
>>> angle_list.sort(reverse=True)
>>> angle_list
[<PyAngle.Angle.Angle object at 0x0000020C195FD0F0>, <PyAngle.Angle.Angle object at 0x0000020C19521B38>, <PyAngle.Angle.Angle object at 0x0000020C195FD860>, <PyAngle.Angle.Angle object at 0x0000020C195D6EF0>]
>>> a3 > a4
True
```

- [x] `__add__(self, other)`: "+"
- [x] `__sub__(self, other)`: "-"
- [x] `__mul__(self, n)`: "\*"
- [x] `__truediv__(self, n)`: "/"
- [x] `__floordiv__(self, n)`: "//"
- [x] `__mod__(self, other)`: "%"
- [x] `__str__(self)`
- [x] `__cmp__(self, other)`
- [x] `__eq__(self, other)`: "=="
- [x] `__ne__(self, other)`: "!="
- [x] `__le__(self, other)`: "<="
- [x] `__lt__(self, other)`: "<"
- [x] `__ge__(self, other)`: ">="
- [x] `__gt__(self, other)`: ">"
- [x] `__hash__(self)`

### Calculators

```python
>>> a2.sin()
0.8660254037844386
```

- [x] `sin() -> float`
- [x] `cos() -> float`
- [x] `tan() -> float`

### Getters

```python
>>> a4.get_deg()
48
>>> a4.get_sec()
50.66940344529314
```

- [x] `get_deg() -> int`
- [x] `get_min() -> int`
- [x] `get_sec() -> float`

### Switchers

```python
>>> [x.to_degrees() for x in angle_list]
[70.47380880109125, 60.0, 48.81407483429036, 30.336111111111112]
>>> a1.to_atan2(x=1)
(1, 0.5851986012863108)
>>> a3.to_fmt_str()
'70°28′25.71″'
```

- [x] `to_degrees() -> float`
- [x] `to_rad() -> float`
- [x] `to_atan2(x=None, y=None) -> (float, float)`
- [x] `to_fmt_str(fmt="xxx°xxx′xxx″", decimal=2) -> str`

### Judges

```python
>>> a3.is_acute_angle()
True
```

- [x] `is_zero_angle() -> bool`: 零角
- [x] `is_acute_angle() -> bool`: 锐角
- [x] `is_right_angle() -> bool`: 直角
- [x] `is_obtuse_angle() -> bool`: 钝角
- [x] `is_straight_angle() -> bool`: 平角
- [x] `is_major_angle() -> bool`: 优角
- [x] `is_minor_angle() -> bool`: 劣角
- [x] `is_complementary_angle_with(other) -> bool`: 余角
- [x] `is_supplementary_angle_with(other) -> bool`: 补角

## Future Features

- [ ] `Angle[] toAnglesFromXYs((float, float)[] angles)`: 参数为(x, y)元组的列表
- [ ] `Angle[] toAnglesFromDegrees(float[] angles)`: 参数为 degree 元组的列表
- [ ] `Angle[] toAnglesFromRads(float[] angles)`: 参数为 rad 元组的列表
- [ ] `(float, float)[] toXYsFromAngles(Angle[] angles)`
- [ ] `float[] toDegreesFromAngles(Angle[] angles)`
- [ ] `float[] toRadsFromAngles(Angle[] angles)`
- [ ] `Angle getNearestAngle(Angle angle, Angle[] angles)`: 在`angles`中找到与`angle`最近的角
- [ ] `Angle getFurthestAngle(Angle angle, Angle[] angles)`: 在`angles`中找到与`angle`最远的角
