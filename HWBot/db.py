#Имитация базы данных

USERS = {
(812335827, "Mikhail_161200"):
{
    "currentChat"   :(-1002101105264, "sdkfksadfkjdslakfjkdsjflkdsajfjl"),
    "allChats"      :[(-1002101105264, "sdkfksadfkjdslakfjkdsjflkdsajfjl")]
}
}
CHATS = {
(-1002101105264, "sdkfksadfkjdslakfjkdsjflkdsajfjl"):
{
    "inviter":  (812335827, "Mikhail_161200"),
    "admins":   [(812335827, "Mikhail_161200")],
    "subjects": ["matAnalisys", "linearAlgebra"],
    "pinned":   [None, 
                {"matAnalisys"              : None,
                "linearAlgebra"             : None,
                "Additional Information"    : None}

                
                ],    #(id, subject->lastMessageId)
                
    #"last":     {"matAnalisys"  : None,
    #            "linearAlgebra" : None}

}
}
#Куча функций доступа к БД

def userExist(id: int):
    for u in USERS:
        if u[0] == id:
            return True
    return False

def currentUserChatId(userId: int):
    for u in USERS:
        if u[0] == userId:
            return USERS[u]["currentChat"][0]
    return None

def getSubjects(chatId: int)->[str]:
    for c in CHATS:
        if c[0] == chatId:
            return CHATS[c]["subjects"]
    return None
def updatePinId(chatId: int, newId:int):
    for c in CHATS:
        if c[0] == chatId:
            CHATS[c]["pinned"][0] = newId
            return True
    return False
def updatePin(chatId: int, name: str, newText):
    for c in CHATS:
        if c[0] == chatId:
            CHATS[c]["pinned"][1][name] = newText
            return True
    return False

def createLink(chatName: int, msgId:int, name:str)->str:
    lnk = ""
    if msgId == None:
        lnk = name
    else:
        lnk = f"<a href = 'https://t.me/{chatName}/{msgId}'>{name}</a> "
    return lnk

def ParsePinned(chatId: int):
    res = "<b>Hometasks</b>\n\n"
    for c in CHATS:
        if c[0] == chatId:
            for s in getSubjects(chatId):
                res += createLink(chatName = c[1], 
                                  msgId = CHATS[c]["pinned"][1][s],
                                  name = s) + "\n"
    return res

def getPinId(chatId:int):
    for c in CHATS:
        if c[0] == chatId:
            return CHATS[c]["pinned"][0]
    return None

if __name__ == "__main__":
    userExist(1)