from code import InteractiveConsole
console = InteractiveConsole()

inp = True
while inp:
    inp = input('>>> ')
    console.runcode(inp)
