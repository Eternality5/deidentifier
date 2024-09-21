document.addEventListener('DOMContentLoaded', function () {
    var slideInBar = document.getElementById('slide-in-bar');
    var closeButton = document.getElementById('close-button');

    // Function to close the slide-in bar
    function closeSlideInBar() {
        slideInBar.style.display = 'none';
        helperDiv.style.display = 'none';
    }

    // Add event listener to the close button
    closeButton.addEventListener('click', closeSlideInBar);
});

console.log("dasdsad")