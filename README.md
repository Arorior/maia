maia
======================
1. Tips
 + [About maia](#a-nameabouta-about-maia)
   
2. Versions
 + [Version 1.1](#a-namev11a-version-11)
 + [Version 1.0](#a-namev10a-version-10)

3. Functions
 + [AutoInstaller](#a-nameautoinsta-autoinstaller)

## <a name="about"></a> About "maia"
This python module was created to make code clear and easy.<br/>
This page will be updated quite often, like the project itself, so I recommend checking for updates often</br>
You can install this package by using a simple command:
> pip install py-maia

And import this package using
> import maia

## <a name="v1.1"></a> Version 1.1
### <a name="autoinst"></a> AutoInstaller
That function will help you install packages without using a console command "pip install ..."<br/>
***Example:***

    from maia import AutoInstaller
    try:
        import colorama
    except ImportError:
       AutoInstaller()
    print("Hello, AutoInstaller" + colorama.Fore.GREEN)

## <a name="v1.0"></a> Version 1.0
Just crashed package, so you can just skip it