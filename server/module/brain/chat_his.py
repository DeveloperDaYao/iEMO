class ChatHis:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ChatHis, cls).__new__(cls, *args, **kwargs)
            cls._instance.variable = []  # 初始化变量
        return cls._instance

    def add(self,text):
        self.variable.append(text)

    def text(self, reverse: bool = False) -> str:
        msg = ""
        if reverse:
            list = reversed(self.variable)
        else:
            list = self.variable
        for m in list:
            msg += m + "\n"
        return msg

# 获取实例
output_history = ChatHis()