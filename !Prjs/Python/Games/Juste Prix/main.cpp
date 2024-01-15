#include <SFML/Graphics.hpp>
#include <iostream>
#include <cstdlib>
#include <ctime>

int main()
{
    sf::RenderWindow window(sf::VideoMode(800, 600), "Juste Prix");

    // Initialisation
    std::srand(static_cast<unsigned int>(std::time(0)));
    int targetPrice = std::rand() % 1000; // Prix cible aléatoire entre 0 et 999
    int guess = 0;
    bool hasWon = false;

    // Texte d'instruction
    sf::Font font;
    if (!font.loadFromFile("arial.ttf"))
    {
        std::cout << "Erreur lors du chargement de la police de caractères." << std::endl;
        return -1;
    }
    sf::Text instructionText("Devinez le prix (entre 0 et 999) :", font, 24);
    instructionText.setPosition(20, 20);

    // Champ de saisie
    sf::RectangleShape inputBox(sf::Vector2f(200, 40));
    inputBox.setFillColor(sf::Color::White);
    inputBox.setOutlineThickness(2);
    inputBox.setOutlineColor(sf::Color::Black);
    inputBox.setPosition(20, 70);

    // Texte de résultat
    sf::Text resultText("", font, 24);
    resultText.setPosition(20, 130);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();

            if (event.type == sf::Event::TextEntered && !hasWon)
            {
                if (event.text.unicode >= '0' && event.text.unicode <= '9')
                {
                    guess = guess * 10 + (event.text.unicode - '0');
                    inputBox.setSize(sf::Vector2f(inputBox.getSize().x + 20, inputBox.getSize().y));
                }
                else if (event.text.unicode == '\b' && guess > 0)
                {
                    guess /= 10;
                    inputBox.setSize(sf::Vector2f(inputBox.getSize().x - 20, inputBox.getSize().y));
                }
                else if (event.text.unicode == '\r')
                {
                    if (guess == targetPrice)
                    {
                        resultText.setString("Félicitations, vous avez trouvé le juste prix !");
                        hasWon = true;
                    }
                    else if (guess < targetPrice)
                    {
                        resultText.setString("Le prix est plus grand que " + std::to_string(guess) + ".");
                    }
                    else
                    {
                        resultText.setString("Le prix est plus petit que " + std::to_string(guess) + ".");
                    }
                }
            }
        }

        window.clear(sf::Color::White);
        window.draw(instructionText);
        window.draw(inputBox);
        window.draw(resultText);
        window.display();
    }

    return 0;
}