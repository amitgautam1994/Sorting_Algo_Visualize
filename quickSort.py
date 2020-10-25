import time

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep((timeTick))

    for i in range(head, tail):
        if data[i] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, i, True))
            time.sleep((timeTick))

            data[border], data[i] = data[i], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, i))
        time.sleep((timeTick))

    # swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep((timeTick))

    data[border], data[tail] = data[tail], data[border]

    return border


def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)

        # LEFT PARTITION
        quick_sort(data, head, partitionIdx - 1, drawData, timeTick)

        # RIGHT PARTITION
        quick_sort(data, partitionIdx + 1, tail, drawData, timeTick)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        # base coloring
        if i >= head and i <= tail:
            colorArray.append('grey')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray
