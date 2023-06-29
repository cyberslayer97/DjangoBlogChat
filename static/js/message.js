var inputMessage = document.getElementById('message');

inputMessage.addEventListener('keyup', function myFunction(event)  {
  if (event.key === 'Enter') {
    event.preventDefault();
    var rowContainer = document.getElementById('row');

    var chatContainer = document.getElementById('chat').cloneNode(true);
    
    chatContainer.children[0].textContent = inputMessage.value;
    chatContainer.children[0].classList = 'm-2 border border-2 rounded-2 p-2'
    chatContainer.children[1].src = '';
    chatContainer.children[1].classList = 'img-thumbnail border border-2 rounded-2'
    chatContainer.children[1].style.height = '40px';
    chatContainer.children[1].style.width = '40px';


    rowContainer.appendChild(chatContainer);
    inputMessage.value = '';

  }
});