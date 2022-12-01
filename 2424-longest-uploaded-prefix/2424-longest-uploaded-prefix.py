class LUPrefix:

    def __init__(self, n: int):
        self.longest_prefix = 0
        self.videos = set()

    def upload(self, video: int) -> None:
        self.videos.add(video)

    def longest(self) -> int:
        while self.longest_prefix + 1 in self.videos:
            self.longest_prefix += 1
            
        return self.longest_prefix


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()