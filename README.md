maia
======================
1. Tips
 + [About maia](#about-maia)
   
2. Versions
 + [Version 1.5](#version-15)
 + [Version 1.1](#version-11)
 + [Version 1.0](#version-10)

3. Functions
 + [AutoInstaller](#autoinstaller)
 + [switch & case](#switch--case)
 + [Loadings & printr](#loadings--printr)
 + [Photo](#photo)

## About "maia"
This python module was created to make code clear and easy.<br/>
This page will be updated quite often, like the project itself, so I recommend checking for updates often</br>
You can install this package by using a simple command:
> pip install py-maia

And import this package using
> import maia

## Version 1.5
**19 February 2021**

### switch & case
That just popular method of iterating, which unfortunately was not added to this language
But in this function I tried to add this functionality in Python

    from maia import switch

    x = 10
    for case in switch(x):
        if case(0):
            print('num is 0')
            break
        elif case(10):
            print('num is 10')
            break
        else:
            print('num not in list')
            break

### Loadings & printr
Now you can use loadings in your project!

    from maia import Loading, printr
    import time

    for x in Loading.user_load(['x', 'b', 'c'], desc='Object: %'):
        printr(x)
        time.sleep(1)
    print('All objets done.')

Or you can load a usual one

    from maia import Loading, printr
    import time

    for x in Loading.usual(xrange=range(0, 100)):
        printr(x)
        time.sleep(0.01)

So, what about "printr()" func? This function allows you to edit
last line into new line. It can be helpful in many situations then you need
to work with a console, so use it :)

### Photo
Now you can load photo from wedsite using just a one simple line
> Photo(path).download(link)

I will add some more functions in this class later 

## Version 1.1
### AutoInstaller
That function will help you install packages without using a console command "pip install ..."<br/>
***Example:***

    from maia import AutoInstaller
    try:
        import colorama
    except ImportError:
       AutoInstaller()
    print("Hello, AutoInstaller" + colorama.Fore.GREEN)

## Version 1.0
Just crashed package, so you can just skip it