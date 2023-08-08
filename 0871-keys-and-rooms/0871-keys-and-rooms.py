class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque

        q = deque([0])
        unlocked = set([0])

        while q:
            cur_room = q.popleft()
            unlocked.add(cur_room)
            keys = rooms[cur_room]

            for key in keys:
                if key not in unlocked:
                    q.append(key)

        return len(unlocked) == len(rooms)
