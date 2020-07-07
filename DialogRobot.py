from tkinter import *
import hashlib
import json
import time
from urllib import parse
import requests

app_id = '**********'
app_key = '****************'

class ApplicantionInfo:
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    # 获取签名用于申请
    def get_sign(self, params):
        uri_str = ''

        for key in sorted(params.keys()):
            uri_str += '{}={}&'.format(key, parse.quote_plus(str(params[key]), safe=''))
        sign_str = uri_str + 'app_key=' + self.app_key

        hash_str = hashlib.md5(sign_str.encode('utf-8'))
        return hash_str.hexdigest().upper()

    def call_api(self, params, api=None):
        if api is None:
            api = self.api

        return requests.post(api, data=parse.urlencode(params).encode("utf-8"), headers=self.headers)


class RobotChat(ApplicantionInfo):
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'

    def __init__(self, app_id, app_key):
        super().__init__(app_id, app_key)
        self.session = str(time.time())

    # 获取调用接口的参数
    def make_params(self, question):
        params = {
            'app_id': self.app_id,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'question': question,
            'session': self.session,
        }

        params['sign'] = self.get_sign(params)
        return params

    # 聊天功能
    def ask(self, question):
        params = self.make_params(question)
        response = self.call_api(params)
        result = json.loads(response.text)
        answer = result['data']['answer']
        return answer

robot = RobotChat(app_id, app_key)

def AIChat(sentense):
    answer = robot.ask(sentense)
    return answer

def main():
    def start():
          strMsg = 'BearChild:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n '
          txtget.insert(END, strMsg, 'redcolor')
          txtget.insert(END, '你好！请问有什么需要吗？')

    # 发送消息
    def sendMsg():
        t=txtMsg.get('0.0', END)
        txtMsg.delete('0.0', END)
        strMsg = '我:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n '

        for i in range(int(txtget.index(END).split(".")[0])-int(txtMsgList.index(END).split(".")[0])+1):
            txtMsgList.insert(END, '\n')
        # 处理间距

        txtMsgList.insert(END, strMsg, 'bluecolor')
        txtMsgList.insert(END, t)
        txtMsgList.see(END)

        for i in range(int(txtMsgList.index(END).split(".")[0])-int(txtget.index(END).split(".")[0])+1):
            txtget.insert(END, '\n')
            txtget.see(END)

        # 处理格式
        strMsg = 'BearChild:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n '
        for i in range(int(txtMsgList.index(END).split(".")[0])-int(txtget.index(END).split(".")[0])+1):
            txtget.insert(END, '\n')
        txtget.insert(END, strMsg, 'redcolor')

        # 获取输出文字
        txtget.insert(END, AIChat(t))
        txtget.see(END)

        for i in range(int(txtget.index(END).split(".")[0])-int(txtMsgList.index(END).split(".")[0])+1):
            txtMsgList.insert(END, '\n')
            txtMsgList.see(END)

    # 取消消息
    def cancelMsg():
        txtMsg.delete('0.0', END)

    # 发送消息事件
    def sendMsgEvent(event):
        sendMsg()

    # 更换图片编号
    global picID
    picID = 0
    def changePictureID():
        global picID
        picID = (picID + 1) % 14
        lblImage.configure(image = picList[picID])

    # 创建窗口
    t = Tk()
    t.title('BearChild')

    # 创建frame容器
    frmLT = Frame(width=500, height=320, bg='#FFFACD')
    frmLC = Frame(width=500, height=150, bg='#FFFACD')
    frmLB = Frame(width=500, height=45, bg='white')
    frmRT = Frame(width=324, height=500, bg='#FFFACD')

    # 创建控件
    txtMsgList = Text(frmLT, width=40, bd=0)
    txtMsgList.tag_config('bluecolor', foreground='#00BFFF')  # 创建tag
    txtMsg = Text(frmLC)
    txtget = Text(frmLT, width=40, bd=0)
    txtget.tag_config('redcolor', foreground='#DAA520')  # 创建tag
    start()


    txtMsg.bind('<Return>', sendMsgEvent)
    btnSend = Button(frmLB, text='发送', width=10, command=sendMsg, bg='#6495ED', bd=0)
    btnCancel = Button(frmLB, text='取消', width=10, command=cancelMsg, bg='#E6E6FA', bd=0)

    btnChange = Button(frmRT, text='更换', width=10, command=changePictureID, bg='#FFE4B5', bd=5)
    scollor = Scrollbar(bg='white')
    scollor.config(command=txtget.yview)
    scollor.config(command=txtMsgList.yview)
    txtget.config(yscrollcommand=scollor.set)
    txtMsgList.config(yscrollcommand=scollor.set)

    # 图片信息
    imgInfo01 = PhotoImage(file="pictures/picture01.png")
    imgInfo02 = PhotoImage(file="pictures/picture02.png")
    imgInfo03 = PhotoImage(file="pictures/picture03.png")
    imgInfo04 = PhotoImage(file="pictures/picture04.png")
    imgInfo05 = PhotoImage(file="pictures/picture05.png")
    imgInfo06 = PhotoImage(file="pictures/picture06.png")
    imgInfo07 = PhotoImage(file="pictures/picture07.png")
    imgInfo08 = PhotoImage(file="pictures/picture08.png")
    imgInfo09 = PhotoImage(file="pictures/picture09.png")
    imgInfo10 = PhotoImage(file="pictures/picture10.png")
    imgInfo11 = PhotoImage(file="pictures/picture11.png")
    imgInfo12 = PhotoImage(file="pictures/picture12.png")
    imgInfo13 = PhotoImage(file="pictures/picture13.png")
    imgInfo14 = PhotoImage(file="pictures/picture14.png")
    picList = [imgInfo01, imgInfo02, imgInfo03, imgInfo04, imgInfo05, imgInfo06, imgInfo07,
               imgInfo08, imgInfo09, imgInfo10, imgInfo11, imgInfo12, imgInfo13, imgInfo14]


    lblImage = Label(frmRT, image=picList[picID])
    lblImage.image = picList[picID]

    # 窗口布局
    frmLT.grid(row=0, column=0, columnspan=2, padx=0, pady=0)
    frmLC.grid(row=1, column=0, columnspan=2, padx=0, pady=0)
    frmLB.grid(row=2, column=0, columnspan=2, padx=0)
    scollor.grid(row=0, column=2, sticky=N + S)
    frmRT.grid(row=0, column=3, rowspan=3, padx=0, pady=0)

    # 固定大小
    frmLT.grid_propagate(0)
    frmLC.grid_propagate(0)
    frmLB.grid_propagate(0)
    frmRT.grid_propagate(0)

    # 方框大小
    btnSend.grid(row=2, column=0)
    btnCancel.grid(row=2, column=1)
    btnChange.grid(row=0, column=0)

    lblImage.grid()
    txtget.grid(row=0, column=0)

    txtMsgList.grid(row=0, column=1)

    txtMsg.grid()

    # 主事件循环
    t.mainloop()

if __name__ == '__main__':
    main()