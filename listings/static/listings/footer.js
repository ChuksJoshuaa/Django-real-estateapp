

const okayEl = document.querySelector(".okay");
now = new Date().getFullYear()
okayEl.innerHTML = now;

const topLinks = document.querySelector(".top-link");

window.addEventListener('scroll', function() {
  const scrollHeight = window.pageYOffset;

  if(scrollHeight > 600) {
       topLinks.classList.add("show-link")
  }
  else {
      topLinks.classList.remove("show-link")
  }

})