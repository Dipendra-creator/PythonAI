def printingFun(x):
    if x == str(x):
        commandLine = "print('"
        endCommand = "')"
        return commandLine + x + endCommand
    elif x == int(x):
        commandLine = "print("
        endCommand = ")"
        return commandLine + str(x) + endCommand


query = input().lower()
if 'hello world' in query:
    fh = open(query.replace(' ', '') + '.py', 'w')
    string = input("Enter the string: ")
    fh.write(printingFun(string))
    fh.close()
if 'addition' and 'sum' and 'add' in query:
    fh = open(query.replace(' ', '') + '.py', 'w')
    sum = 0
    string = list(map(int, input("Enter number separated with plus sign (+): ").split("+")))
    for i in range(len(string)):
        sum += string[i]
    fh.write(printingFun(sum))
    fh.close()