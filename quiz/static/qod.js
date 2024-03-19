 $(document).ready(function () {
            var timer;

            // Funkcja do losowania pytania
            function getRandomQuestion() {
                $.ajax({
                    url: '/QOD/',
                    type: 'GET',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    success: function (data) {
                        $('#questionCard').css('transform', 'rotateY(180deg)');
                        setTimeout(function () {
                            $('#questionCard').html('<i class="fas fa-angry top-left"></i>' + data.question + '<i class="fas fa-angry bottom-right"></i>').css('transform', 'rotateY(0deg)');
                        }, 300);
                    },
                    error: function (error) {
                        console.log('Error:', error);
                    }
                });
            }

            // Funkcja do obsługi przycisku "Piję" lub "Odpowiadam"
            function handleButtonClick() {
                $('#timer').show(); // Pokaż timer

                var seconds = 10;
                $('#timer').text(seconds);

                // Rozpocznij odliczanie
                timer = setInterval(function () {
                    seconds--;
                    $('#timer').text(seconds);

                    // Jeśli upłynął czas, zatrzymaj timer, ukryj go i wylosuj nowe pytanie
                    if (seconds === 0) {
                        clearInterval(timer);
                        $('#timer').hide();
                        getRandomQuestion();
                    }
                }, 1000);
            }

            // Wywołaj getRandomQuestion automatycznie po otwarciu strony
            getRandomQuestion();

            // Obsługa przycisku "Piję"
            $('#drinkButton').on('click', function () {
                handleButtonClick();
            });

            // Obsługa przycisku "Odpowiadam"
            $('#answerButton').on('click', function () {
                handleButtonClick();
            });
            // Obsługa przycisku "Inne pytanie"
            $('#Reload').on('click', function () {
                getRandomQuestion();
            });
            // Obsługa przycisku zmiany koloru
            $('#changeColorButton').on('click', function () {
                // Zmiana koloru tła strony na losowy kolor
                var randomColor = getRandomColor();
                $('body').css('background-color', randomColor);
            });

            // Funkcja do pobierania wartości ciasteczka CSRF
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            // Funkcja do generowania losowego koloru
            function getRandomColor() {
                var letters = '0123456789ABCDEF';
                var color = '#';
                for (var i = 0; i < 6; i++) {
                    color += letters[Math.floor(Math.random() * 16)];
                }
                return color;
            }
        });