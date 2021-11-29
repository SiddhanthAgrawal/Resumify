//et para = document.getElementById("body");
let compStyles = window.getComputedStyle("body");
para.textContent = compStyles.getPropertyValue('color');
console.log(para.textContent);
console.log("Hi");