# 🤖 N8N-VOICE-CHATBOT
Chatbot automatizado en **Telegram** que **captura y entrega audio**.  
Transcribe y envía audios mediante una **API** en **Python con Flask**.

<div align=center>
  <img src="https://brandslogos.com/wp-content/uploads/images/large/python-logo.png" alt="Python" width=170 />
  <img src="https://cdn.raiolanetworks.com/blog/wp-content/uploads/n8n.png?width=599&height=599" alt="Python" width=170 />
</div>

---

## 📦 Instalación y Ejecución

Pasos para correr la API en tu máquina:

1. **Clona el repositorio**  
   ```bash
   git clone https://github.com/FranJMD0508/Voice-Chabot-n8n.git
   ```

2. **Entra a la carpeta del proyecto**  
   ```bash
   cd Voice-Chabot-n8n
   ```

3. **Instala las dependencias requeridas**
   ```bash
   pip install -r requirements.txt
   ```
4. **Inicia la API**
   ```bash
   python src/app.py
   ```
---

## ℹ️ Detalles sobre la API
> [!IMPORTANT]
> Es necesario descargar y añadir **FFmpeg** a las variables de entorno de tu sistema. Esto para las conversiones de formatos de audio.

> [!NOTE]
> No olvides crear un archivo **.env** y crear la variable **"N8N_API_KEY"**, la cual contiene la clave de tu API.

>[!NOTE]
> Al hacer un llamado a la API, coloca en los headers la key **"API-KEY"** con el valor de la clave mencionada anteriormente.
