def dataMessage(message, lang, f_arcane=False, f_num=False, f_color=False):
    return {
        "id": message.chat.id,
        "username": message.chat.username,
        "lang": lang,
        "f_arcane": f_arcane,
        "f_num": f_num,
        "f_color": f_color
    }

class Session():
    def __init__(self):
        self.session_pool = dict()
    
    def addUser(self, id, username, lang, profile = {}, f_arcane=False, f_num=False, f_color=False):
        if not self.userInPool(id):
            self.session_pool[id] = dict()
            self.session_pool[id]["username"] = username
            self.session_pool[id]["lang"] = lang
            self.session_pool[id]["profile"] = profile
            self.session_pool[id]["f_arcane"] =  f_arcane
            self.session_pool[id]["f_num"] = f_num
            self.session_pool[id]["f_color"] = f_color

    def addUserFromMessage(self, value):
        if not self.userInPool(id):
            self.session_pool[value["id"]] = dict()
            self.session_pool[value["id"]]["username"] = value["username"]
            self.session_pool[value["id"]]["lang"] = value["lang"]
            self.session_pool[value["id"]]["profile"] = dict()
            self.session_pool[value["id"]]["f_arcane"] =  value["f_arcane"]
            self.session_pool[value["id"]]["f_num"] = value["f_num"]
            self.session_pool[value["id"]]["f_color"] = value["f_color"]

    def trySetProfile(self, id, name, male, birth_date, birth_time, birth_city):
        if (self.userInPool(id)):
            self.session_pool[id]["profile"]["name"] = name
            self.session_pool[id]["profile"]["male"] = male
            self.session_pool[id]["profile"]["birth_date"] = birth_date
            self.session_pool[id]["profile"]["birth_time"] = birth_time
            self.session_pool[id]["profile"]["birth_city"] = birth_city
            
        else:
            return None

    def userInPool(self, id):
        return True if id in self.session_pool.keys() else False

    def getUser(self, id):
        return self.session_pool[id] if self.userInPool(id) else None
    
    def getPool(self):
        return self.session_pool
    
    def getProfile(self,id):
        return self.session_pool[id]["profile"]
    
    def clearPool(self):
        self.session_pool.clear()

    def eraseUser(self, id):
        self.session_pool.pop(id)

    def setFArcane(self, id):
        self.session_pool[id]["f_arcane"] = True
    
    def getFarcane(self,id):
        return self.session_pool[id]["f_arcane"]
    
    def setFNum(self, id):
        self.session_pool[id]["f_num"] = True
    
    def getFNum(self,id):
        return self.session_pool[id]["f_num"]
    
    def setFColor(self, id):
        self.session_pool[id]["f_color"] = True
    
    def getFColor(self,id):
        return self.session_pool[id]["f_color"]
    
    def getLang(self, id):
        return self.session_pool[id]["lang"]
    
    def setLang(self, id, lang):
        self.session_pool[id]["lang"] = lang
    
    def setPostState(self, id, status):
        self.session_pool[id]["post_status"] = status
    
    def getPostState(self, id):
        return self.session_pool[id]["post_status"]