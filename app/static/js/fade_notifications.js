function fadeNotification(id) {
    setTimeout(
      function() {
        notification = document.getElementById(id);
        notification.classList.add('transition-opacity', 'duration-1000', 'ease-out');
        notification.classList.add('opacity-0', 'hidden');
      }, 10000);
  }