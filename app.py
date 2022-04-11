import cv2


class Graph:
    def __init__(self, visited = [], queue = [], graph = {}):
        self.visited = visited
        self.queue = queue
        self.graph = {
            '1': ['2', '3'],
            '2': ['4', '5'],
            '3': ['6'],
            '4': [],
            '5': ['7'],
            '6': [],
            '7': []

        }

    def openImg(self, img):
        img = cv2.imread(img, 1)
        cv2.imshow('Graph Representation ', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def bfsAlgorithms(self, startedNode):
        self.visited.append(startedNode)
        self.queue.append(startedNode)

        while self.queue:
            n = self.queue.pop(0)
            print(n, end=" ")

            for neighbour in self.graph[n]:
                if neighbour not in self.visited:
                    self.queue.append(neighbour)
                    self.visited.append(neighbour)

    def dfsAlgorithms(self, startedNode):
        self.visited = set()
        if startedNode not in self.visited:
            print(startedNode)
            self.visited.add(startedNode)
            for neighbour in self.graph[startedNode]:
                self.dfsAlgorithms(neighbour)


graph = Graph()
