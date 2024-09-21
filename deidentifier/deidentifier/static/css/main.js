window.onload=function(){
  
  document.addEventListener('DOMContentLoaded', function () {
    var slideInBar = document.getElementById('slide-in-bar');
    var closeButton = document.getElementById('close-button');

    // Function to close the slide-in bar
    function closeSlideInBar() {
        slideInBar.style.display = 'none';
    }

    // Add event listener to the close button
    closeButton.addEventListener('click', closeSlideInBar);
});


const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar_menu');


// Display Mobile Menu
menu.addEventListener('click', function () {
  menu.classList.toggle('is-active');
  menuLinks.classList.toggle('active');
});


// expansions
document.addEventListener("DOMContentLoaded", function() {
  const sections = document.querySelectorAll(".exp-section");

  sections.forEach(section => {
    const header = section.querySelector("h2");
    const content = section.querySelector(".exp-content");

    header.addEventListener("click", function() {
      section.classList.toggle("active");
      content.style.display = section.classList.contains("active") ? "block" : "none";
    });
  });
});
}


