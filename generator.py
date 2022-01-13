import json
import random

def main():
    print('GURPS Infinite Worlds Generator')
    print('v0.0.3\n')
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
    quantumOptions = retrieveJson('data/quantum.json')

    # Homeline or Centrum world
    if (not automatic):
        print('1 - Homeline')
        print('2 - Centrum')

        while True:
            option = input()
            if (option in [1, 2]):
                centerWorld = quantumOptions.keys()[int(option)]
            elif (option == ''):
                centerWorld = random.choice(list(quantumOptions.keys()))
            else:
                continue
    else:
        centerWorld = random.choice(list(quantumOptions.keys()))
    
    print('Homeworld: ' + centerWorld)
    results['centerWorld'] = centerWorld

    # Quantum
    if (not automatic):
        print('1 - Quantum ', quantumOptions[centerWorld]['1'])
        print('2 - Quantum ', quantumOptions[centerWorld]['2'])
        print('3 - Quantum ', quantumOptions[centerWorld]['3'])
        print('4 - Quantum ', quantumOptions[centerWorld]['4'])
        print('5 - Quantum ', quantumOptions[centerWorld]['6'])

        while True:
            option = input()

            if (option in ['1', '2', '3', '4']):
                quantum = quantumOptions[centerWorld][option]
            elif (option == '5'):
                quantum = quantumOptions[centerWorld]['6']
            elif (option == ''):
                quantum = random.choice(list(quantumOptions[centerWorld].values()))
            else:
                continue
    else:
        quantum = random.choice(list(quantumOptions[centerWorld].values()))
    
    print('Quantum: Q' + quantum)
    results['quantum'] = quantum

    selectWorldType(automatic, results)

def selectWorldType(automatic, results):
    worldOptions = retrieveJson('data/worldType.json')

    # World Type
    if (not automatic):
        print('1 - Empty')
        print('2 - Echo')
        print('3 - Parallel')
        # Add one more here
        print('4 - Challenge')

        while True:
            option = input()

            if (option == '1'):
                worldType = 'Empty'
            elif (option == '2'):
                worldType = 'Echo'
            elif (option == '3'):
                worldType = 'Parallel'
            elif (option == '4'):
                worldType = 'Challenge'
            elif (option == ''):
                worlds = list(worldOptions.values())
                specialOptions = worlds.pop()
                worldType = random.choice(worlds)
            else:
                continue
    else:
        worlds = list(worldOptions.values())
        specialOptions = worlds.pop().values()
        worldType = random.choice(worlds)

    if (worldType == 'Echo/Parallel'):
        if (results['quantum'] == '6'):
            worldType = random.choice(list(specialOptions))
        else:
            worldType = random.choice(['Echo', 'Parallel'])
    
    print('World Type: ' + worldType)
    results['worldType'] = worldType

if __name__ == '__main__':
    main()