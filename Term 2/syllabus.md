# Data Types
- string
  - str(رشته)
  - `'`, `"`
  -
    | Operators | State |
    | --- | ----------- |
    | `+` | [x] |
    | `-` | [ ] |
    | `*` | [ ] |
    | `/` | [ ] |
  -

- integer
  - int(عدد صحیح)
  -
    | Operators | State |
    | --- | ----------- |
    | `+` | [x] |
    | `-` | [x] |
    | `*` | [x] |
    | `/` | [x] |

- float
  - عدد اعشاری 
  -
    | Operators | State |
    | --- | ----------- |
    | `+` | [x] |
    | `-` | [x] |
    | `*` | [x] |
    | `/` | [x] |

# Variable
- start with `a`~`z`, `A`~`Z`
- dont start with `0`~`9`
- dont contain ' '(space)
- dont contain `!`,`@`,`#`,`$`,`%`,`^`,`&`,`*`,`(`, `)`,` ...
- can contain `_`
- dont use this words as variable
`False`, `await`, `else`, `import`, `pass`, `None`, `break`, `except`, `in`, `raise`, `True`, `class`, `finally`, `is`, `return`,  `and`, `continue`, `for`, `lambda`, `try`,  `as`, `def`, `from`, `nonlocal`, `while`, `assert`, `del`, `global`, `not`, `with`, `async`, `elif`, `if`, `or`, `yield`

# Functions
- print()  
میتوان چندین مقدار رو با گذاشتین ویرگول بین آنها چاپ کند.
- type()   
نوع داده رو مشخص میکتد

# F-String
```
name = 'Sina'
f'My name is {name}'
```
# Function
- input(prompt)
  - یک ورودی از ما میگیرد 
  - prompt یک رشته است که هنگام دریافت ورودی به کاربر نمایش میهد
  - دستور INPUT اطلاعات را از نوع رشته ذخیره میکند

# Operator INT vs STR
در ضرب یک رشته با عدد ، رشته به تعداد عدد چاپ میشود.

# Functions
- int()  
  - یک رشته از اعداد دریافت میکند و رشته را تبدیل به عدد میکند
  ‍- از رشته(نباید اعشاری باشد) به عدد تبدیل میکند
  - از اعشاری به عدد تبدیل میکند
- str()  
  - تبدیل به رشته میکند  
  - از عدد یا عدد اعشاری تبدیل به رشته میشود
- float()  
  - تبدیل به عدداعشاری میکند  
  - از عدد یا رشته تبدیل به عدد اعشاری میشود

- range()
  - از این دستور برای ایجاد سری عددی استفاده میکنیم
  - range(7)
    - از صفر تا 6 را ایحاد میکند
  - range(2, 7)
    - از ۲ تا 6 را ایحاد میکند
  - range(2, 7, 3)
    - از ۲ تا 6 را ۳ واحد سه واحد ایحاد میکند


# Comment
اگر قصد دارید در کدتون پیغام بنویسید یا کدی مه نوشته اید اجرا نشود ابتدای خط # قرار دهید.

# Turtle
یک کتابخانه برای کشیدن تصویر است.

# Data Types
- boolean
  - bool( `True`, `False`)

# Comparison
عملگرهای مقایسه ای
- `>`
- `>=`
- `<`
- `<=`
- `==` برابر 
- `!=` نابرابر

# `if` Statement
دستور شرطی برای تصمیم گیری در حالتهای مختلف
- باید شرط داشته باشد
- اخر خط دونقطه قرارمیگیرد
- دستورات باید با فاصله نوشته شود(indent)

# Chained `if`
```
if condition:
    statements
elif condition
    statements
```

# Turtle Library
## import
1. import tkinter
2. import tkinter as tk
3. from tkinter import *

## Functions
- forward
- left

# `while` Loop
این حلقه مانند if است اما تا زمانیکه شرط درست هست آنرا اجرا میکند
- باید شرط داشته باشد
- اخر خط دونقطه قرارمیگیرد
- دستورات باید با فاصله نوشته شود(indent)

# String Methods
[String Methods](https://www.w3schools.com/python/python_ref_string.asp)  

| isdecimal() | isdigit() | isnumeric() |          Example    |
| :---        |  :----:   |     ---:    |      :----:         |
|    True     |    True   |    True     | "038", "０３８"      |
|  False      |  False    |  False      | "abc", "38.0", "-38"|


# String Index
رشته اطلاعات رو داخل پلاکهای مجزا ذخیره میکند.
مثال:
```
#    01234567
#    ^^^^^^^^   
a = "Poulstar"
  
```

# For
برای تکرار و ایتریت کردن استفاده میکنیم  
 
    for i in range(4):
        print(i)

