<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

---

# 🚀 ES6 Promises Project

## 📚 Resources
Read or watch:  
- [📘 Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)  
- [📘 JavaScript Promise: An introduction](https://developers.google.com/web/fundamentals/primers/promises)  
- [📘 Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)  
- [📘 Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)  
- [📘 Throw / Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)  

---

## 🎯 Learning Objectives
By the end of this project, you should be able to explain (without Google 🧠):

- ✨ **Promises** → how, why, and what they are.  
- 🔗 How to use the **`.then()`**, **`.resolve()`**, and **`.catch()`** methods.  
- 📦 How to use **every method of the Promise object**.  
- ⚡ **Throw / Try** → handling errors gracefully.  
- ⏳ The **`await`** operator.  
- ⚙️ How to use an **async function**.  

---

## ✅ Requirements
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Node.js 20.x.x** and **npm 9.x.x**.  
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`.  
- All files must end with a **new line**.  
- A `README.md` file at the root of the project folder is **mandatory**.  
- Code must use the `.js` extension.  
- Code will be tested using **Jest** with the command:
  ``` npm run test ```

## ⚙️ Installation and Setup

# 🟢 Install NodeJS 20.x.x
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v  # Should display v20.15.1
npm -v     # Should display 10.7.0

# 🧪 Install Jest, Babel, and ESLint
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint

## 📂 Required Configuration Files

package.json

babel.config.js

eslint.config.js (⚠️ ESLint v9 uses eslint.config.js, not .eslintrc.js)

⚠️ Don’t forget to run npm install inside the project folder to install all the required dependencies.

🚫 Do not push the node_modules folder to your repository.