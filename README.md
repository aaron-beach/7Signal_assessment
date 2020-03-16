<h1 align="center">Welcome to Sample project 👋</h1>

<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/aaron-beach/SampleWork/blob/master/README.md" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
</p>

This project is an assessment completed in Python. The assessment includes TDD principles(writing test cases prior to coding). Please contact me directly with any questions.

## Table of contents

* [Prerequisites](#prerequisites)
* [Technologies](#technologies)
* [Using Sample](#using-sample)
* [Author](#author)
* [License](#license)
* [Assignment](#assignment)

## Prerequisites

>Before you begin, ensure you have met the following requirements:

## Technologies

>Project is created with:

- Pre-commit Hooks ([pre-commit](https://pre-commit.com/))
- Testing ([Pytest](https://docs.pytest.org/en/latest/))
- Code formatting ([Black](https://github.com/python/black) and [flake8](http://flake8.pycqa.org/en/latest/))
- Type checking ([mypy](http://mypy-lang.org/))

## Using Sample

>To use this project, follow these steps:

This project assumes you are using [pipenv](https://github.com/pypa/pipenv) to manage
virtual environments and project dependencies.

#### 1. Install project dependencies:

```
pipenv install --dev
```

#### 2. Setup project to use **pre-commit**:

```
pipenv run pre-commit install
```

#### 3. Install additional project dependencies:

```
pipenv install [package]
```

Use the **--dev** flag if needed.

#### 4. Run tests:

```
make test
```

Tests will be automatically run prior to every commit.


## Author


👤 **Aaron Beach**

* Website: aaronbeach.dev
* Github: [@aaron-beach](https://github.com/aaron-beach)
* LinkedIn: [@arbeach/](https://linkedin.com/in/arbeach/)

## License


This project uses the following license: MIT License

Copyright (c) 2020 Aaron Beach

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Additional Notes

In addition to autoformatting the code via **Black** and **flake8** for each commit,
it does the following:

- Runs the unit tests
- Runs mypy for type checking

If you would like to disable this, edit this [file](.pre-commit-config.yaml).
# Assignment
# TDD Kata 1 - String Calculator
http://osherove.com/kata
## Before you start:

- Try not to read ahead.
- Do one task at a time. The trick is to learn to work incrementally.
- Make sure you only test for correct inputs. there is no need to test for invalid inputs for this kata
- Test First!

## String Calculator

1. In a **test-first manner**, create a simple class `class StringCalculator`
   with a method `public int Add(string numbers)`

   - [x] The method can take **0, 1 or 2 numbers**, and will **return their sum**
   (for an **empty string** it will return **0**)
   for example
   `“” == 0 , “1” == 1 , “1,2” == 3`
   - [x] Start with the **simplest** test case of an **empty string** and move to **one & two numbers**
   - [x] Remember to solve things as **simply as possible** so that you force yourself to
   write tests you did not think about
   * Remember to **refactor** after each passing test


2. Allow the **Add** method to handle an unknown amount of numbers
   - [x] accept unknown number of numbers

3. Allow the **Add** method to handle **new lines** between numbers (instead of **commas**).
   - [x] the following input is ok: `“1\n2,3” == 6`

   - [x] the following is **INVALID input** so do not expect it : **`“1,\n”`** (not need to write a test for it)

4. Support different delimiters:
   to change a delimiter, the beginning of the string will contain a separate line
   - [x] accept multiple delimiters
   that looks like this:
   `“//[delimiter]\n[numbers…]”`

   for example
   `“//;\n1;2” == 3`

   since the default delimiter is `‘;’` .

   **Note:** All existing scenarios and tests should still be supported

5. Calling **Add** with a **negative number** will throw an **exception** “negatives not allowed” -
   and the **negative that was passed**.
   - [x] throw exception
   - [x] display msg and err

6. If there are **multiple negatives**, show all of them in the **exception message**
   - [x] throw exception
   - [x] display msg with multi negatives

7. Using **TDD**, Add a method to `StringCalculator`
   called `public int GetCalledCount()`
   that returns how many times `Add()` was invoked.
   **Remember** - Start with a **failing (or even non compiling**) test.
   - [x] add method `public int GetCalledCount()`
   - [x] return count of `add()`

8. (.NET Only) Using TDD, Add an **event** to the `StringCalculator` class named
   `public event Action<string, int> AddOccured` ,
   that is triggered after every `Add()` call.

   ***Hint**:
   Create the **event** declaration first:
   then write a failing test that listens to the event
   and proves it should have been triggered when calling **Add()**.
   ***Hint 2**:
   Example:

```
   string giveninput = null;
   sc.AddOccured += delegate(string input, int result)
   {
      giveninput = input;
   };
```

9. Numbers bigger than **1000** should be **ignored**, for example:
   `2 + 1001 == 2`
   - [x] ignore numbers above 1000

10. Delimiters can be of any length with the following format:
    `“//[delimiter]\n”`
    - [x] passed delimiter of any length
    for example:
    `“//[***]\n1***2***3” == 6`

11. Allow multiple delimiters like this:
    `“//[delim1][delim2]\n”`
    - [x] passed multiple delimiters
    for example
    `“//[*][%]\n1*2%3” == 6.`

12. make sure you can also handle multiple delimiters with **length longer than one char**
    for example
    `“//[**][%%]\n1**2%%3” == 6.`
    - [x] passed multiple delimiters of any length

For more info visit https://osherove.com or email roy@osherove.com
