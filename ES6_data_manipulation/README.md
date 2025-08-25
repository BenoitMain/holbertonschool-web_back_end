<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

---

# ⚡ ES6 Data Manipulation

**Level:** Amateur  
**Author:** Johann Kerbrat, Engineering Manager at Uber Works  
**Weight:** 1  

Your score will be updated as you progress through the project.

---

## 📖 Description
This project focuses on mastering ES6 data manipulation in JavaScript.  
You will learn to work with arrays, typed arrays, and ES6 data structures such as `Set`, `Map`, and `WeakMap`.  
By the end of the project, you should be able to confidently explain and implement these concepts without external help.

---

## 📚 Resources
You may find the following resources useful:

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)  
- [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)  
- [Set Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)  
- [Map Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)  
- [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)  

---

## 🎯 Learning Objectives
By the end of this project, you should be able to explain to anyone (without Google):

- How to use `map`, `filter`, and `reduce` on arrays.  
- How typed arrays work in JavaScript.  
- The differences and use cases of `Set`, `Map`, and `WeakMap`.  

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
