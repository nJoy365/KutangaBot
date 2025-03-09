# KutangaBot 🎵 🤖

KutangaBot is a feature-rich Discord bot built with `discord.py`. It includes music streaming capabilities using **Lavalink**, MongoDB-powered persistence, and various utilities to enhance the Discord experience.

---

## 🚀 Features

- 🎶 **Music Playback**: Uses Lavalink for high-quality audio streaming.
- 📊 **Statistics Tracking**: Keeps track of user activity and commands.
- 🎲 **Fun Commands**: Dice rolls, RPS, reminders, and more!
- 🛠 **Modular Cog System**: Easy-to-expand with custom commands.
- 🗄 **MongoDB Storage**: Stores persistent data efficiently.

---

## 🔧 Configuration

### **Set Up `.env` File**

Rename `.env-example` to `.env` and update the values:

```
TOKEN=Fjdif3jflksjefsldjf834jf.434.tgm4j3tkl3j4tg
APPLICATION_ID=112233445566778899
DB_NAME=VeryNiceDatabaseName
MONGO_USER=VeryNiceUser
MONGO_PASSWORD=VeryNicePassword123
MONGO_PORT=80085
MONGO_HOST=192.168.1.991
LLURL=http://lavalink:80085
LLPASS=VeryNicePassword2
LLM_API_URL=http://llm_api.com/api/generate

```

---

## 🛠 Tech Stack

- **Python 3.10** (`discord.py`)
- **MongoDB** (Data storage)
- **Lavalink** (Music streaming)
- **Docker** (Containerized deployment)

---

## 🌎 Deployment

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/nJoy365/KutangaBot.git
cd KutangaBot
```

### **2️⃣ Run with Docker Compose**

Ensure you have **Docker & Docker Compose** installed, then start all services:

```sh
docker-compose up -d --build
```

To stop the bot:

```sh
docker-compose down
```

---

## ❓ Troubleshooting

### **Bot Can't Connect to MongoDB**

- Ensure the bot is using `mongodb://mongodb:27017` inside Docker (not `localhost`).
- Run `docker-compose logs -f mongodb` to check logs.

### **Bot Can't Connect to Lavalink**

- Check `docker-compose logs -f lavalink`.
- Make sure Lavalink's `application.yml` binds to `0.0.0.0`.

---

## 🤝 Contributing

Contributions are welcome! 🎉  
If you'd like to contribute:

1. **Fork** this repository.
2. Create a **new branch** (`git checkout -b feature-branch`).
3. **Commit your changes** (`git commit -m "Added new feature"`).
4. **Push to your branch** (`git push origin feature-branch`).
5. Open a **Pull Request**.

---

🚀 **Happy Coding!** 🎵🤖

