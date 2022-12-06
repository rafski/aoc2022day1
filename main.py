import numpy
with open('input.txt') as f:
    lines = f.read().splitlines()
    list_array = numpy.array(lines)
    list_array[list_array == ''] = 0
    #print(list_array[5])
    int_array = list_array.astype(numpy.int_)
    #print(int_array)
    cal = 0
    elves = []
    for num in int_array:
        if num != 0:
            cal += num
        else:
            elves.append(cal)
            cal = 0

    superElfCal = numpy.amax(elves)
    superElf = numpy.where(elves == superElfCal)
    topElvesIndex = numpy.argpartition(elves, -3)[-3:]
    bigCal = 0
    for elf in topElvesIndex:
        bigCal += elves[elf]

    print('Elf number:', superElf,' had ', superElfCal, ' calories')
    print('Elves with most food :' , topElvesIndex , 'had ' , bigCal , ' calories' )