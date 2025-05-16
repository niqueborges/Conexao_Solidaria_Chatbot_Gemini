document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const chatLog = document.getElementById('chat-log');
    const typingIndicator = document.querySelector('.typing-indicator');

    const BACKEND_URL = 'http://127.0.0.1:5000/chat'; // Atualize para o domínio real se necessário

    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    const resetButton = document.getElementById('reset-button');
resetButton.addEventListener('click', async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/reset', {
            method: 'POST'
        });
        const data = await response.json();
        if (data.status === 'ok') {
            // Limpa o chat log
            chatLog.innerHTML = '';
            appendMessage('bot-message', 'Conversa reiniciada. Olá! Como posso ajudar hoje?');
        }
    } catch (error) {
        console.error('Erro ao reiniciar o chat:', error);
        appendMessage('bot-message', 'Ocorreu um erro ao reiniciar a conversa.');
    }
});


    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            appendMessage('user-message', message);
            userInput.value = '';
            sendToBackend(message);
        }
    }

    function appendMessage(className, message, isOption = false) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(className);

        if (isOption) {
            const optionButton = document.createElement('button');
            optionButton.textContent = message;
            optionButton.classList.add('option-button');
            optionButton.addEventListener('click', () => {
                appendMessage('user-message', optionButton.textContent);
                sendToBackend(optionButton.textContent);
                const optionsContainer = chatLog.querySelector('.bot-message .options');
                if (optionsContainer) optionsContainer.innerHTML = '';
            });
            messageDiv.appendChild(optionButton);
        } else {
            messageDiv.textContent = message;
        }

        chatLog.appendChild(messageDiv);
        chatLog.scrollTop = chatLog.scrollHeight;
    }

    function showTypingIndicator(show) {
        typingIndicator.style.display = show ? 'block' : 'none';
    }

    async function sendToBackend(message) {
        showTypingIndicator(true);
        try {
            const response = await fetch(BACKEND_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });

            const data = await response.json();
            displayBotResponse(data.text, data.options);
        } catch (error) {
            console.error('Erro:', error);
            appendMessage('bot-message', 'Erro ao obter resposta do servidor.');
        } finally {
            showTypingIndicator(false);
        }
    }

    function displayBotResponse(text, options = []) {
        const botMessageDiv = document.createElement('div');
        botMessageDiv.classList.add('bot-message');
        botMessageDiv.textContent = text;

        const optionsContainer = document.createElement('div');
        optionsContainer.classList.add('options');

        options.forEach(optionText => {
            const optionButton = document.createElement('button');
            optionButton.textContent = optionText;
            optionButton.classList.add('option-button');
            optionButton.addEventListener('click', () => {
                appendMessage('user-message', optionText);
                sendToBackend(optionText);
                optionsContainer.innerHTML = '';
            });
            optionsContainer.appendChild(optionButton);
        });

        botMessageDiv.appendChild(optionsContainer);
        chatLog.appendChild(botMessageDiv);
        chatLog.scrollTop = chatLog.scrollHeight;
    }
});
