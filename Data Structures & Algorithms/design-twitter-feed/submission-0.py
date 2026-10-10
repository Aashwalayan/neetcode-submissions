class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following.get(userId, set()) | {userId}

        for user in users:
            for time, tweetId in self.tweets.get(user, [])[-10:]:
                heapq.heappush(heap, (-time, tweetId))

        return [heapq.heappop(heap)[1] for _ in range(min(10, len(heap)))]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following.get(followerId, set()).discard(followeeId)
