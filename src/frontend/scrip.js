const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const chatLog = document.getElementById('chat-log');

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const message = userInput.value.trim();
    if (message) {
        addUserMessage(message);
        userInput.value = '';
        // Aqui, em um sistema real, a mensagem seria enviada para o backend
        // Para a demonstração, vamos simular uma resposta do bot
        setTimeout(() => {
            simulateBotResponse(message);
        }, 500);
    }
}

function addUserMessage(message) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('user-message');
    messageDiv.textContent = message;
    chatLog.appendChild(messageDiv);
    chatLog.scrollTop = chatLog.scrollHeight; // Mantém a última mensagem visível
}

function simulateBotResponse(userMessage) {
    const responseDiv = document.createElement('div');
    responseDiv.classList.add('bot-message');
    // Lógica de resposta simulada (bem básica para a demonstração)
    if (userMessage.toLowerCase().includes('doar')) {
        responseDiv.textContent = 'Que ótimo! Para qual tipo de item você gostaria de doar?';
    } else if (userMessage.toLowerCase().includes('ajuda')) {
        responseDiv.textContent = 'Entendi. Qual tipo de ajuda sua instituição precisa?';
    } else {
        responseDiv.textContent = 'Obrigado pela sua mensagem!';
    }
    chatLog.appendChild(responseDiv);
    chatLog.scrollTop = chatLog.scrollHeight;
}