            document.addEventListener("DOMContentLoaded", function () {
            var textElement = document.querySelector("#animatedText");
            var text = textElement.innerText;
            textElement.innerText = "";

            function animateText(index) {
                if (index < text.length) {
                    textElement.innerHTML += text.charAt(index);
                    index++;
                    setTimeout(function () {
                        animateText(index);
                    }, 30); // Ustaw dowolne opóźnienie między literami (w milisekundach)
                }
            }

            animateText(0);
        });