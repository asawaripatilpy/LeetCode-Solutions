class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}      # userId -> [(time, tweetId)]
        self.following = {}   # userId -> set of followees
        

    def postTweet(self, userId: int, tweetId: int) -> None:
            if userId not in self.tweets:
                self.tweets[userId] = []

            self.tweets[userId].append((self.time, tweetId))
            self.time += 1
        

    def getNewsFeed(self, userId: int) -> list[int]:
        users = {userId}

        if userId in self.following:
            users.update(self.following[userId])

        heap = []

        for user in users:
            if user in self.tweets:
                tweets = self.tweets[user]
                index = len(tweets) - 1

                time, tweetId = tweets[index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        result = []

        while heap and len(result) < 10:
            neg_time, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            index -= 1

            if index >= 0:
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        return result
        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)


        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)