from maia import AutoInstaller

try:
    import colorama
except ImportError:
    AutoInstaller()

print('Hello, AutoInstaller' + colorama.Fore.RED)
