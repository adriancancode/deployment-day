# 🚀 Website Deployment Workshop

Welcome to the **Website Deployment Workshop Repo!**  
This repository contains a **simple static website** that you will deploy using modern hosting platforms such as **Netlify** or **Vercel**.

By the end of this workshop, you will learn how to:

- Fork a GitHub repository
- Clone a project locally
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

## 1️ Fork This Repository

First, create your own copy of this project.

1. Click the **Fork** button at the top right of this page.
2. Select your GitHub account.

You should now have a copy of the repository under:

```
https://github.com/YOUR_USERNAME/deployment-workshop
```

---

## 2️ Clone the forked Repository

Next, download the project to your computer.

```bash
git clone https://github.com/YOUR_USERNAME/deployment-workshop.git
```

Move into the project directory:

```bash
cd deployment-workshop
```

---

## 3️ Open the Project and install dependencies

Open the project in your preferred editor.

Example using **VS Code**:

```bash
code .
npm install
```

---

## 4️ Run the Website Locally

```
npm run dev
```

## 5 Deploy Your Website

You will now deploy your project using one of the following platforms.

## Option A — Deploy with Vercel

1. Go to  
[https://vercel.com/new](https://vercel.com/new)
2. Sign in using **GitHub**
3. Click **Add New Project**
4. Import your forked repository
5. Click **Deploy**

Vercel will automatically detect that this is a static site.

Your site will be live in about **30 seconds to a minute**.

---

## Option B — Deploy with Netlify

1. Go to  
https://netlify.com

2. Sign in/up with **GitHub**
3. Select **Import from Git**
4. Under **Let’s deploy your project with…**, select **Github**
5. Choose your forked repository
6. Click **Deploy Site**

Your site will be live shortly.

---

# 🎉 Congratulations!

You have successfully deployed a website to the internet!

---

## The Extra Mile(Optional): Make some changes to your site

Your project will automatically **redeploy whenever you push new commits to GitHub**.

Try updating the site and pushing another commit to see automatic deployment in action.

Example:

Open **App.tsx** and change the title or text.

```
<h1>Hello from ACM's Workshop 🚀</h1>
```
Save your changes, then commit and push them to Github.
```bash
git add -A/-a
git commit -m "Made changes to website for deployment workshop"
git push
```
And... voila!  Your new changes are reflected on the deployment!

# 📚 Useful Resources

### Netlify Docs
[https://docs.netlify.com/](https://docs.netlify.com/)

### Vercel Docs
[https://vercel.com/docs](https://vercel.com/docs)

### GitHub Guides
[https://guides.github.com/](https://guides.github.com/)

### Git Cheat Sheet
[https://education.github.com/git-cheat-sheet-education.pdf](https://education.github.com/git-cheat-sheet-education.pdf)

---
