const menuToggle = document.getElementById("menuToggle");
const siteNav = document.querySelector(".site-nav");

menuToggle.addEventListener("click", function(){

    siteNav.classList.toggle("active");

    if(siteNav.classList.contains("active")){
        menuToggle.innerHTML='<i class="fa-solid fa-xmark"></i>';
    }else{
        menuToggle.innerHTML='<i class="fa-solid fa-bars"></i>';
    }

});
