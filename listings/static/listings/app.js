const menu = [
   {
   id: 1,
   name: "Banana Island, Lagos",
   },
   {
   id: 2,
   name: "Ikoyi, Lagos",
   },
   {
   id: 3,
   name: "Dobi, Abuja(F.C.T)",
   },
   {
   id: 4,
   name: "Lekki, Lagos",
   },
   {
   id: 5,
   name: "Asokoro, Abuja(F.C.T)",
   },
]

const toggleBtn = document.querySelector(".sidebar-toggle");
const closeBtn = document.querySelector(".close-btn");
const sidebar = document.querySelector(".sidebar");
const navBar = document.getElementById("nav")
dateEl = document.querySelector(".date")

window.addEventListener('DOMContentLoaded', function () {
   dateEl.innerHTML = menu[rand()].name
})

function rand() {
  return Math.floor(Math.random() * menu.length)
}




toggleBtn.addEventListener("click", function () {
  sidebar.classList.toggle("show-sidebar");
});

closeBtn.addEventListener("click", function () {
  sidebar.classList.remove("show-sidebar");
});


window.addEventListener('scroll', function() {
  const scrollHeight = window.pageYOffset;
  const navHeight = navBar.getBoundingClientRect().height;

  if(scrollHeight > navHeight) {
     navBar.classList.add("fixed-nav")
  }
  else {
    navBar.classList.remove("fixed-nav")
  }
})


