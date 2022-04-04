const details = document.querySelectorAll("details");

details.forEach((targetDetail) => {
    targetDetail.addEventListener("click", () => {
        // Close all the details that are not targetDetail.
        details.forEach((detail) => {
            if (detail !== targetDetail) {
                detail.removeAttribute("open");
            }
        });
    });
});

function menuOpen() {
    var menuBLock = document.querySelector('.menu-block');
    var menu = document.querySelectorAll(".side-menu");
    var btn = document.querySelector(".menu-open-button");
    menuBLock.classList.toggle('block-opened');
    for (i = 0; i <= menu.length; i++) {
        menu[i].classList.toggle("open");
    }
}
