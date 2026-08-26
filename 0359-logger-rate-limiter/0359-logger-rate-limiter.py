class Logger:

    def __init__(self):
        self.lastMessages = {}
        
    

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.lastMessages:
            self.lastMessages[message] = timestamp + 10
            return True
        next_time = self.lastMessages[message]
        if timestamp < next_time :
            return False
        else:
            self.lastMessages[message] = timestamp + 10
            return True
        
        

        

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)