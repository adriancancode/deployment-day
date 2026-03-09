# 🚀 Website Deployment Workshop

Welcome to the **Website Deployment Workshop Repo!**  
This repository contains a **simple static website** that you will deploy using modern hosting platforms such as **Netlify** or **Vercel**.

By the end of this workshop, you will learn how to:

- Fork a GitHub repository
- Clone a project locally
- Make a simple change to a website
- Push updates to GitHub
- Deploy your site to the internet using **Netlify or Vercel**

---

# 🌐 Live Deployment Goal

During this workshop, you will deploy your own version of this website so that it is accessible through a **public URL on the internet**.

Example:

```
https://your-project-name.vercel.app
```

or

```
https://your-project-name.netlify.app
```

---

# 📂 Project Structure

```
deployment-workshop/
│
├── index.html
├── style.css
├── script.js
└── README.md
```

This is a **simple static website** consisting of:

- **HTML** → structure of the webpage
- **CSS** → styling
- **JavaScript** → optional interactive behavior

No frameworks or build tools are required.

---

# 1️⃣ Fork This Repository

First, create your own copy of this project.

1. Click the **Fork** button at the top right of this page.
2. Select your GitHub account.

You should now have a copy of the repository under:

```
https://github.com/YOUR_USERNAME/deployment-workshop
```

---

# 2️⃣ Clone the Repository

Next, download the project to your computer.

```bash
git clone https://github.com/YOUR_USERNAME/deployment-workshop.git
```

Move into the project directory:

```bash
cd deployment-workshop
```

---

# 3️⃣ Open the Project

Open the project in your preferred editor.

Example using **VS Code**:

```bash
code .
```

---

# 4️⃣ Run the Website Locally

Since this is a static site, you can simply open the file:

```
index.html
```

Or use a local server.

Example with VS Code **Live Server extension**:

Right click:

```
index.html → Open with Live Server
```

---

# 5️⃣ Make a Small Change

Edit the website so your deployment is unique.

Example:

Open **index.html** and change the title or text.

```html
<h1>Hello from Adrian's Workshop 🚀</h1>
```

Save your changes.

---

# 6️⃣ Commit and Push Your Changes

Stage your changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Updated website for deployment workshop"
```

Push to GitHub:

```bash
git push origin main
```

---

# 7️⃣ Deploy Your Website

You will now deploy your project using one of the following platforms.

## Option A — Deploy with Vercel

1. Go to  
https://vercel.com

2. Sign in using **GitHub**
3. Click **Add New Project**
4. Import your forked repository
5. Click **Deploy**

Vercel will automatically detect that this is a static site.

Your site will be live in about **30 seconds**.

---

## Option B — Deploy with Netlify

1. Go to  
https://netlify.com

2. Sign in with **GitHub**
3. Click **Add New Site**
4. Select **Import from Git**
5. Choose your forked repository
6. Click **Deploy Site**

Your site will be live shortly.

---

# 🎉 Congratulations!

You have successfully deployed a website to the internet!

Your project will automatically **redeploy whenever you push new commits to GitHub**.

Try updating the site again and pushing another commit to see automatic deployment in action.

---

# 📚 Useful Resources

### Netlify Docs
https://docs.netlify.com/

### Vercel Docs
https://vercel.com/docs

### GitHub Guides
https://guides.github.com/

### Git Cheat Sheet
https://education.github.com/git-cheat-sheet-education.pdf

---

# 💻 Workshop Information

This repository is used for deployment workshops such as:

- **ACM CSUF Workshops**
- Intro to Web Deployment
- GitHub + Hosting Basics
