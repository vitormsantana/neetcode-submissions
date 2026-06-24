class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key):
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        data = self.store[key]
        
        if len(data) == 1:
            if data[0][1] <= timestamp:
                return data[0][0]
            else:
                return ""

        maxx = -float('inf')
        returnn = ''

        l = 0
        r = len(data) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if data[mid][1] == timestamp:
                return data[mid][0]

            if data[mid][1] < timestamp:
                l = mid + 1
                maxx = max(maxx, data[mid][1])
                returnn = data[mid][0]
            else:
                r = mid - 1
        return returnn