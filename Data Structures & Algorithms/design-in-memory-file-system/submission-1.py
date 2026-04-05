from abc import ABC, abstractmethod

class FileSystemNode(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def is_file(self) -> bool:
        pass

class File(FileSystemNode):

    def __init__(self, name, content=""):
        super().__init__(name)
        self.content = content
    
    def is_file(self) -> bool:
        return True

class Directory(FileSystemNode):

    def __init__(self, name):
        super().__init__(name)
        self.children = {}
    
    def is_file(self) -> bool:
        return False

class FileSystem:

    def __init__(self):
        self.root = Directory("/")

    def _traverse(self, path: str) -> FileSystemNode:
        if path == "/":
            return self.root
        parts = path.split("/")[1:]
        node = self.root
        for part in parts:
            node = node.children[part]
        return node

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)
        if node.is_file():
            return [node.name]
        return sorted(node.children.keys())
        
    def mkdir(self, path: str) -> None:
        parts = path.split("/")[1:]
        node = self.root
        for part in parts:
            if part not in node.children:
                node.children[part] = Directory(part)
            node = node.children[part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = filePath.split("/")[1:]
        node = self.root
        for part in parts[:-1]:
            if part not in node.children:
                node.children[part] = Directory(part)
            node = node.children[part]
        fname = parts[-1]
        if fname not in node.children:
            node.children[fname] = File(fname)
        node.children[fname].content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        return self._traverse(filePath).content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
