stripe.onclick = function() {
    let sec = new Date().getSeconds() % 10;
    stripe.style.transitionDelay = '-' + sec + 's';
    stripe.classList.add('animate');
  };

  window.addEventListener('DOMContentLoaded', function()
{
    let sec = new Date().getSeconds() % 10;
    stripe.style.transitionDelay = '-' + sec + 's';
    stripe.classList.add('animate');
  });