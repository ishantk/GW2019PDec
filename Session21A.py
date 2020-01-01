# WhatsAppUser : name, phone, status
# WhatsAppGroup : title, users

class WhatsAppUser:

    def __init__(self, name, phone, status):
        self.name = name
        self.phone = phone
        self.status = status

    def showWhatsAppUser(self):
        print("{} | {} | {}".format(self.name, self.phone, self.status))


class WhatsAppGroup:

    title = "NA"

    def __init__(self, title, users):
        WhatsAppGroup.title = title
        self.users = users

    def showWhatsAppGroup(self):

        print("=={}==".format(WhatsAppGroup.title))
        print("==Users {}==".format(len(self.users)))

        for user in self.users:
            user.showWhatsAppUser()

    def changeGroupTitle(self):
        pass




u1 = WhatsAppUser("John", "+91 99999 88888", "HNY2020 !!")
u2 = WhatsAppUser("Fionna", "+91 99977 11888", "Kuch Bhi !!")
u3 = WhatsAppUser("Sia", "+91 98977 12388", "Work Hard, Get Luckier !!")

users = [u1, u2, u3]

wg1 = WhatsAppGroup("Auribises", users)
wg1.showWhatsAppGroup()


