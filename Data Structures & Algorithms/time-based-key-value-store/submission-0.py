class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])
    
    def get(self, key: str, timestamp: int) -> str:
            if not key in self.map:
                return ""

            values = self.map[key]
            result = ""
            l, r = 0, len(values) - 1

            while l <= r:
                mid = (l + r) // 2
                if values[mid][1] <= timestamp:
                    result = values[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
            return result