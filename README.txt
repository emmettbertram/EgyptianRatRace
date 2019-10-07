Welcome to Egyptian Rat Race! Game by Emmett Bertram

Intro:
    This is a fast paced game that typically consists of people quickly putting down cards and slapping the deck
    on some occasions, hoping to win by gathering all of the cards!

Setup:
    Start by running the python game file from the console. Specify how many players you want (mostly in the range of
    2 to 8 players, but once you hit about 8 people you will probably want more than one deck). Give a unique name and
    keyboard character for each character. The keyboard character is used for 'slapping' the deck later on. Specify how
    many decks you want to play with, then the game will start!

Gameplay:
    The deck is split as evenly as possible between all players. The goal of the game is to be holding the entire deck.
    Gameplay consists of players placing down one card onto the card pile in the order that names were entered into
    the game. A player is not able to see their hand of cards, they just flip down the card from the top of their hand
    onto the pile (think like the game WAR where you just flip out one card, not knowing what it is until it is
    revealed on the pile). Cards are placed automatically by the system as gameplay progresses, all you have to worry
    about is slapping. Players want to slap the pile in two different circumstances:

        - A pair: when the last two cards played are the same value (as in the last two cards are Fours or the last two
        cards are Queens etc.)

        - A sandwich: when the last three played cards alternate ABA (as in the last three cards are Three-Five-Three or
        King-two-King etc.)

    When a player slaps the pile and there is a pair or sandwich on top, they get the entire pile! So, how do you slap
    in this console game? Simply press the letter that corresponds to you! After every card is placed, there is an
    opportunity for players to type. Whichever player's letter comes first is the one who gets the pile OR will have
    to burn a card (lose a card to the bottom of the pile) if it was not a pair or a sandwich. Note that there is an
    opportunity to slap every time a card is placed. After people have placed their slaps, make sure to press enter
    so that the slap can be processed. Even if no one is slapping, make sure to wait a second or two before pressing
    enter to give your opponents an opportunity to slap a pair, sandwich, or to make a mistake and have to burn a card!
    Whoever picks up the pile is the one who starts the next pile off.

    These simple slapping rules apply at all times in the game, even when it starts getting more complicated with
    the following rules!

    Face cards in this game have some special properties. When a face card is played by player A, the next player
    (player B) has a certain amount of chances to play another face card, or the entire pile goes to player A. This rule
    sounds confusing, but as you start playing it makes more sense.

    When the following face cards are played, the next player has a certain amount of chances to play another face card
        - Jack: the next player has 1 chance
        - Queen: the next player has 2 chances
        - King: the next player has 3 chances
        - Ace: the next player has 4 chances

    Note that this property doesn't stack, it resets every time someone plays another face card. So if play goes from
    player A placing a Queen to player B placing a King, player C has 3 chances to place a face card, not 2 + 3.

    Practical examples help explain the rule. Say normal gameplay without any face cards goes on until the following
    happens, which could happen in a real game:
        - Player A plays a King
            - the next player has 3 chances
        - Player B (the next in order) plays a 3
            - this is not a face card, B must try again
        - Player B plays a 7
            - not a face card, B must try one more time
        - Player B plays a 2
        - The pile goes to player A's hand
        - Player A starts the next round by starting a new pile

    Another example, that shows how the pile can really build up with a lot of face cards
        - Player A plays an Ace
            - the next player has 4 chances
        - Player B plays a Jack
            - the next player has 1 chance
        - Player C plays a Queen
            - the next player has 2 chances
        - Player D plays a Queen
            - SOMEONE SLAPS THE DECK
    REMEMBER that basic slapping rules apply at all times, even when a player is using their chances to try to get face
    cards.

    If at any time a player runs out of cards, they are out. Once one player is left, they win!