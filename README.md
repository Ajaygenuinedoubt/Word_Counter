

# 📄 README.md

```markdown
# 🎯 Word Counter & Visualizer

Welcome to the **Word Counter & Visualizer** project built using **Flask**! 🚀  
This web app allows users to **analyze text**, **count unique words**, and **visualize** word frequencies through beautiful **Pie, Bar, and Doughnut charts**.  
👉 **Login is required** to access the functionalities for added security.

---

## ✨ Features

- 🔐 **Login Authentication** (User must log in to use the app)
- 🖋️ **Paste or Write Text** for analysis
- 📊 **Generate Word Frequency Charts**:
  - Pie Chart
  - Bar Chart
  - Doughnut Chart
- 📥 **Download Word Counts as CSV**
- 🔄 **Logout Functionality**

---

## 🖼️ Screenshots

### 🔒 Login Page


![Image](https://github.com/user-attachments/assets/fdefd26a-fe2b-4248-93f6-808c10771954)



### 🏠 Home / Text Analysis Page
![image](https://github.com/user-attachments/assets/8d30aa54-4f82-4616-a468-509152c4605b)



> 📢 **Tip**: Place your screenshots in a folder called `static/images/` in your project directory.

---

## 🛠️ Tech Stack

- **Frontend**:  
  - HTML5
  - CSS3
  - Chart.js (for charts)
  
- **Backend**:  
  - Python 3
  - Flask

- **Other Tools**:  
  - Session Management
  - CSV File Handling (to download results)

---

## ⚙️ Project Structure

```

your-project/
│
├── app.py
├── templates/
│   ├── login.html
│   ├── home.html
│
├── static/
│   ├── style.css
│   ├── images/
│       ├── login\_page.png
│       ├── home\_page.png
│
├── README.md
└── requirements.txt

````

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/word-counter-visualizer.git
cd word-counter-visualizer
````

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install Flask Flask-Session Werkzeug
```

Or, create a **`requirements.txt`** file and install:

```bash
pip install -r requirements.txt
```

> **requirements.txt** content:
>
> ```
> Flask
> Flask-Session
> Werkzeug
> ```

### 4. Run the Application

```bash
python app.py
```

App will be running on:

```
http://127.0.0.1:5000/
```

---

## 🔑 Default Login Credentials

| Username | Password |
| :------: | :------: |
|   admin  | password |

> ✨ You can change these credentials directly in the `app.py` file.

---

## 📂 Folder Explanations

* `templates/` → Contains HTML templates.
* `static/` → Contains CSS files, JavaScript libraries (via CDN) and images.
* `app.py` → Main Python Flask backend.
* `README.md` → Complete project documentation.

---

## ❓ How It Works

1. **Login** with credentials.
2. **Paste** any text into the text area.
3. **Submit** to see:

   * Word counts.
   * Pie chart, bar chart, and doughnut chart.
4. **Download** the analysis result in CSV format.
5. **Logout** when finished.

---

## 📝 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project for personal or commercial purposes.

---

## 🙋‍♂️ Author

Made with ❤️ by **Ajay Jha**

Connect with me on:


* [LinkedIn](https://www.linkedin.com/in/ajay-kumar-jha-30b612261/)
* [GitHub](https://github.com/Ajaygenuinedoubt)

---

```

---


