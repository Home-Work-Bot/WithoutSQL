#Имитация базы данных

USERS = {
(812335827, "Mikhail_161200"):
{
    "currentChat"   :(-1002101105264, "sdkfksadfkjdslakfjkdsjflkdsajfjl"),
    "allChats"      :[(-1002101105264, "sdkfksadfkjdslakfjkdsjflkdsajfjl")]
},
(None, None): 1
}
CHATS = {
(-1002101105264, "sdkfksadfkjdslakfjkdsjflkdsajfjl"):
{
    "inviter":  (812335827, "Mikhail_161200"),
    "admins":   [(812335827, "Mikhail_161200")],
    "subjects": ["matAnalisys", "linearAlgebra"],
    "pinned":   (None, 
                {"matAnalisys"              : None,
                "linearAlgebra"             : None,
                "Additional Information"    : None}

                
                ),    #(id, subject->lastMessageId)
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

def updatePin(chatId: int, pinId: int, name: str, newText):
    for c in CHATS:
        if c[0] == chatId:
            CHATS[c]["pinned"][name] = newText
            return True
    return False

def updateLast(chatId: int, subjectName: str, newLastId:int):
    for c in CHATS:
        if c[0] == chatId:
            CHATS[c]["pinned"][subjectName] = newLastId

if __name__ == "__main__":
    userExist(1)