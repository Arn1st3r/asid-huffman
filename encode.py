import collections

class Queue:
    def __init__(self):
        self.heap = []

    def left(self, k):
        return 2 * k + 1

    def right(self, k):
        return 2 * k + 2

    def parent(self, k):
        return (k - 1) // 2

    def minHeapify(self, k):
        l = self.left(k)
        r = self.right(k)
        smallest = k

        if l < len(self.heap) and self.heap[l][0] < self.heap[k][0]:
            smallest = l
        if r < len(self.heap) and self.heap[r][0] < self.heap[smallest][0]:
            smallest = r
        if smallest != k:
            self.heap[k], self.heap[smallest] = self.heap[smallest], self.heap[k]
            self.minHeapify(smallest)
            
    def heapifyUp(self, k):
        while k > 0 and self.heap[self.parent(k)][0] > self.heap[k][0]:
            self.heap[k], self.heap[self.parent(k)] = self.heap[self.parent(k)], self.heap[k]
            k = self.parent(k)

    def EQ(self, value):
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)

    def DQ(self):
        if len(self.heap) == 0:
            print("Kopiec jest pusty")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.minHeapify(0)
        return root

    def __len__(self):
        return len(self.heap)

def huffman(data):
    queue = Queue()
    for c, freq in data.items():
        queue.EQ((freq, c))

    while len(queue) > 1:
        x_left = queue.DQ()
        y_right = queue.DQ()
        z = (x_left[0] + y_right[0], x_left, y_right)
        queue.EQ(z)

    return queue.DQ()

def huffmanBinary(tree, prefix=''):
    if type(tree[1]) is str:
        return {tree[1]: prefix}
    left = huffmanBinary(tree[1], prefix + "0")
    right = huffmanBinary(tree[2], prefix + "1")
    return dict(list(left.items()) + list(right.items()))

def encode(file, huffmanBinaryString):
    try:
        with open(file, 'r', encoding='utf-8') as fileOutput:
            data = fileOutput.read()
    except Exception as error:
        print(f"Bład: {error}")

    encodedString = ""
    for c in data:
        if c in huffmanBinaryString:
            encodedString += huffmanBinaryString[c]

    sortedLetters = {}
    for c in data:
        if c in huffmanBinaryString:
            if c not in sortedLetters:
                sortedLetters[c] = huffmanBinaryString[c]
    
    try:
        with open("zaszyfr.txt", "w", encoding="utf-8") as outputFile:
            outputFile.write(f"Słownik: {sortedLetters}\n") 
            outputFile.write(f"Skompresowany tekst: {encodedString}\n")
    except Exception as error:
        print(f"Błąd: {error}")
        

file = input("Podaj plik txt: ")
try:
    with open(file, 'r', encoding='utf-8') as fileInput:
        data = fileInput.read()
    
    letters = collections.OrderedDict()
    for c in data:
        if c.isalpha() or c.isspace():
            if c not in letters:
                letters[c] = 0
            letters[c] += 1
    
    huffmanTree = huffman(letters)
    huffmanBinaryString = huffmanBinary(huffmanTree)
    encode(file, huffmanBinaryString)

except Exception as error:
    print(f"Wystąpił błąd: {error}")
