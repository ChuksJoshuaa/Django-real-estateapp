
firstEl = document.querySelector("#first")
secondEl = document.querySelector(".second")
thirdEl = document.querySelector(".third")
fourEl = document.querySelector(".four")


const minutes = document.querySelector("#minutes")
    const seconds = document.querySelector("#seconds")
    let count = 0;

    const renderTimer = () => {
      count += 1;
      firstEl.innerHTML = (count % 150).toString().padStart(2);
      secondEl.innerHTML = (count % 200).toString().padStart(2);
      thirdEl.innerHTML = (count % 170).toString().padStart(2);
      fourEl.innerHTML = (count % 120).toString().padStart(2);
    }

    const timer = setInterval(renderTimer, 60)