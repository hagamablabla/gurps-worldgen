import json
import math
import random

def main():
    print('GURPS Infinite Worlds Generator')
    print('v0.0.5\n')
    print('1 - Generate new world automatically')
    print('2 - Generate new world step-by-step')
    print('3 - Change settings (TO-DO)')
    
    results = {}
    while True:
        entry = input()
        try:
            entry = int(entry)
        except ValueError:
            continue

        if (entry == 1):
            print('How many worlds do you want to generate?')
            while True:
                numWorlds = input()
                try:
                    numWorlds = int(numWorlds)
                    break
                except ValueError:
                    continue

            for x in range(numWorlds):
                selectQuantum(True, results)
                print()
            break
        elif (entry == 2):
            input('A note before we begin: for any set of options, you may press enter without inputing anything to have the program automatically choose that step for you.')
            selectQuantum(False, results)
            break
        elif (entry == 3):
            retrieveSettings()
        continue

    if(results):
        print()
    
def retrieveJson(fileName):
    file = open(fileName)
    data = json.load(file)
    file.close()

    return data

def retrieveSettings():
    retrieveJson('')

def selectQuantum(automatic, results):
    # Homeline or Centrum world
    if (not automatic):
        print('\nHomeworld')
        print('1 - Homeline')
        print('2 - Centrum')

        while True:
            option = input()
            try:
                option = int(option)
            except ValueError:
                continue

            if (option in range(1, 2)):
                break
            elif (option == ''):
                option = random.randint(1, 2)
                break
            else:
                continue
    else:
        option = random.randint(1, 2)
    
    centerWorld = ['Homeline', 'Centrum'][option - 1]
    
    print('Homeworld: ' + centerWorld)
    results['centerWorld'] = centerWorld

    # Quantum
    if (not automatic):
        print('\nQuantum')
        if (centerWorld == 'Homeline'):
            print('1 - Quantum 3')
            print('2 - Quantum 4')
            print('3 - Quantum 5')
        elif (centerWorld == 'Centrum'):
            print('1 - Quantum 8')
            print('2 - Quantum 9')
            print('3 - Quantum 10')
        print('4 - Quantum 6')
        print('5 - Quantum 7')

        while True:
            option = input()
            try:
                option = int(option)
            except ValueError:
                continue

            if (option in range(1, 5)):
                break
            elif (option == 5):
                option = 6
                break
            elif (option == ''):
                option = random.randint(1, 6)
                break
            else:
                continue
    else:
        option = random.randint(1, 6)

    if (centerWorld == 'Homeline'):
        quantum = [3, 4, 5, 6, 6, 7][option - 1]
    elif (centerWorld == 'Centrum'):
        quantum = [8, 9, 10, 6, 6, 7][option - 1]
    
    print('Quantum: Q' + str(quantum))
    results['quantum'] = quantum

    selectWorldType(automatic, results)

def selectWorldType(automatic, results):
    # World Type
    if (not automatic):
        print('\nWorld Type')
        print('1 - Empty')
        print('2 - Echo/Parallel')
        print('3 - Echo')
        print('4 - Parallel')
        print('5 - Challenge')

        while True:
            option = input()
            try:
                option = int(option)
            except ValueError:
                continue

            if (option in range(1, 3)):
                break
            elif (option == '3'):
                worldType = 'Echo'
                break
            elif (option == '4'):
                worldType = 'Parallel'
                break
            elif (option == '5'):
                option = 6
                break
            elif (option == ''):
                option = random.randint(1, 6)
                break
            else:
                continue
    else:
        option = random.randint(1, 6)
    
    if (not ('worldType' in locals())):
        worldType = ['Empty', 'Echo/Parallel', 'Echo/Parallel', 'Echo/Parallel', 'Echo/Parallel', 'Challenge'][option - 1]
    
    if (worldType == 'Echo/Parallel'):
        option = random.randint(1, 6)
        if (results['quantum'] == 6):
            worldType = ['Echo', 'Echo', 'Parallel', 'Parallel', 'Parallel', 'Parallel'][option - 1]
        else:
            worldType = ['Echo', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel'][option - 1]
    
    print('World Type: ' + worldType)
    results['worldType'] = worldType

    if (worldType == 'Empty'):
        emptyWorldGen(automatic, results)


def emptyWorldGen(automatic, results):
    # Empty World Type
    if (not automatic):
        print('\nEmpty Worlds')
        print('1 - Resource exploitation')
        print('2 - Homeline colony or colonies')
        print('3 - Disaster world')

        while True:
            option = input()
            try:
                option = int(option)
            except ValueError:
                continue

            if (option == 1):
                break
            elif (option == 2):
                emptyType = 'Homeline colony or colonies'
                break
            elif (option == 3):
                emptyType = 'Disaster world'
                break
            elif (option == ''):
                option = random.randint(1, 6)
                break
            else:
                continue
    else:
        option = random.randint(1, 6)

    if (not ('emptyType' in locals())):
        emptyType = ['Resource exploitation', 'Resource exploitation', 'Resource exploitation', 'Resource exploitation', 'Homeline colony or colonies', 'Disaster world'][option - 1]
    
    print('Empty World Type: ' + emptyType)
    results['emptyType'] = emptyType

    if (emptyType == 'Resource exploitation'):
        resourceWorldGen(automatic, results)

def resourceWorldGen(automatic, results):
    resourcePrice = {'Bauxite':20, 'Beryllium':600000, 'Chromium':500, 'Cobalt':50000, 'Gold':8800000, 'Platinum':12800000, 'Silver':440000, 'Titanium':8000, 'Uranium':14000}
    resourceProbability = [10, 1, 4, 2, 15, 25, 40, 50, 10]

    # Resources
    if (not automatic):
        print('\nWealth')
        print('Generated automatically')
    
    numMines = math.ceil(random.lognormvariate(2, 1) * random.lognormvariate(2, 1))
    resourceMines = random.choices(list(resourcePrice.keys()), resourceProbability, k = numMines)
    mineCount = {}
    for resource in list(resourcePrice.keys()):
        mineCount[resource] = resourceMines.count(resource)
        print(resource, ': ', mineCount[resource], end = ' ')
    
    print(mineCount)
    results['mines'] = mineCount

if __name__ == '__main__':
    main()