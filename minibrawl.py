# ===============================
# MINIBRAWL - SERVEUR + JEU MOBILE
# ===============================

import socket, threading, json, random, time, sys

MODE = "client"   # <-- METS "server" SUR PC, "client" SUR TELEPHONE
SERVER_IP = "192.168.1.25"  # <-- IP DU PC
PORT = 5555

# =====================================================
# ==================== SERVEUR =========================
# =====================================================

if MODE == "server":

    clients = []
    players = {}
    score = {"red":0,"blue":0}

    def broadcast():
        while True:
            data=json.dumps({"players":players,"score":score})
            for c in clients:
                try:
                    c.send((data+"\n").encode())
                except:
                    pass
            time.sleep(0.05)

    def choose_team():
        r=len([p for p in players.values() if p["team"]=="red"])
        b=len([p for p in players.values() if p["team"]=="blue"])
        return "red" if r<=b else "blue"

    def handle_client(conn):
        pid=str(random.randint(1000,9999))
        team=choose_team()

        players[pid]={
            "x":random.randint(100,700),
            "y":random.randint(100,500),
            "hp":100,
            "team":team
        }

        clients.append(conn)
        print("Player connected:",pid)

        try:
            while True:
                msg=conn.recv(1024).decode()
                if not msg: break
                data=json.loads(msg)

                if data["type"]=="move":
                    players[pid]["x"]=data["x"]
                    players[pid]["y"]=data["y"]

                if data["type"]=="shoot":
                    for id,p in players.items():
                        if id!=pid:
                            dx=p["x"]-data["x"]
                            dy=p["y"]-data["y"]
                            if abs(dx)<40 and abs(dy)<40:
                                p["hp"]-=20
                                if p["hp"]<=0:
                                    score[players[pid]["team"]]+=1
                                    p["x"]=random.randint(100,700)
                                    p["y"]=random.randint(100,500)
                                    p["hp"]=100

        except:
            pass

        clients.remove(conn)
        del players[pid]
        conn.close()

    def start_server():
        s=socket.socket()
        s.bind(("0.0.0.0",PORT))
        s.listen()
        print("SERVER RUNNING")
        threading.Thread(target=broadcast,daemon=True).start()

        while True:
            conn,_=s.accept()
            threading.Thread(target=handle_client,args=(conn,),daemon=True).start()

    start_server()

# =====================================================
# ==================== JEU MOBILE ======================
# =====================================================

if MODE == "client":

    from kivy.app import App
    from kivy.uix.widget import Widget
    from kivy.clock import Clock
    from kivy.graphics import Color, Ellipse, Rectangle

    sock = socket.socket()
    sock.connect((SERVER_IP,PORT))

    players={}
    score={"red":0,"blue":0}

    def listen_server():
        global players,score
        while True:
            data=sock.recv(4096).decode()
            if not data: break
            data=json.loads(data)
            players=data["players"]
            score=data["score"]

    threading.Thread(target=listen_server,daemon=True).start()

    class Game(Widget):
        def __init__(self,**kw):
            super().__init__(**kw)
            self.x=400
            self.y=300
            Clock.schedule_interval(self.update,1/60)

        def on_touch_move(self,touch):
            self.x=touch.x
            self.y=touch.y
            sock.send(json.dumps({"type":"move","x":self.x,"y":self.y}).encode())

        def on_touch_down(self,touch):
            sock.send(json.dumps({"type":"shoot","x":self.x,"y":self.y}).encode())

        def update(self,dt):
            self.canvas.clear()
            with self.canvas:
                for p in players.values():
                    if p["team"]=="red":
                        Color(1,0,0)
                    else:
                        Color(0,0,1)
                    Ellipse(pos=(p["x"],p["y"]),size=(30,30))

                Color(1,1,1)
                Rectangle(pos=(10,560),size=(250,30))

    class GameApp(App):
        def build(self):
            return Game()

    GameApp().run()
