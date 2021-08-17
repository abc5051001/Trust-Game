# Trust-Game
<h>Two players will face each other. They each decide independently to "cooperate" or "cheat". If they both cooperated, they each win two points. If they both cheated, nobody wins anything. If one cooperates and one cheats, the cheater gets +3 and the cooperator loses a point.</h>
  
<p>One turn is defined as each player making a choice, and winning or losing some points as a result.
Shared history against this player is available to players, and they may use this to guide their decision.
It costs one point to play a turn. A player's points may go negative, and yet they can still spend/lose
more points.</p>
• One game is defined as two players playing multiple turns together. Their increasingly shared history
will certainly affect their chosen behavior: will they keep cooperating even if their opponent doesn't?
Will they hold grudges? Between games, players will reset their history; perhaps this new person is
more trustworthy!
• A tournament involves multiple players. Each round, all players play each other once, accumulating
or losing points. At the end of the round, some lowest scorers are removed (and any others with
negative points), and some highest scorers are duplicated. After all rounds have been played, we see
the "evolved" population of who remains, as a summary dictionary of the count of each style of player
that survived.
Kinds of Players
There are five kinds of players in our version of the tournament. (they have unique first letters too…)
• previous starts by cooperating, then always copies the previous move of their opponent.
(this was the "copycat" in the shared link).
• friend always cooperates, no matter what. May be vulnerable to abuse!
(this was the "cooperator" in the shared link).
• cheater never cooperates. (this was the "cheater" in the shared link).
• grudger cooperates as long as the opponent does, but after one non-cooperation, never
cooperates ever again with this opponent. (this was the "grudger" in the shared link)
• detective starts with cooperate, cheat, cooperate, cooperate; then if they've never been betrayed,
they cheat. If ever they are betrayed, they behave like previous does. (this was the
"detective" in the shared link)
Required Classes
Working through the classes in the given order is the simplest path to assignment completion; but many
methods can be completed out of order if you get stuck on others. Many of the methods are quite simple, once
you get comfortable accessing the fields of the object. Just be sure to complete the init/str/repr/eq
definitions before moving on to other classes that use them!
Methods return None when no other return value is specified.
class Move: represents one move, indicating a choice to cooperate or not.
• def __init__( self, cooperate=True): constructor of a move: create/initialize the cooperate field.
• def __str__ (self): return "." for a cooperating move, "x" for a non-cooperating move
• def __repr__(self): create/return a string as in this example: "Move(True)"
• def __eq__ (self, other): return boolean: whether this move has same cooperate value as the other
• def change (self): change the cooperation status of this move.
• def copy (self): create/return a new Move object that has the same cooperation status.
Class PlayerException(Exception): Represents any exceptional situation for players, with a message
stored inside of it. Be sure to include the (Exception) portion of the signature, so our PlayerException
type is an exception type (and can thus be raised and excepted).
• def __init__(self, msg):create/initialize a msg field based on the parameter.
• def __str__ (self): return the msg.
• def __repr__(self): return a string like this: "PlayerException('message contents')"
class Player: Represents one player, whose style string will resolve their behavior. A Player object
keeps track of the needed internal state: previous moves of the opponent, their style, and their points.
• def __init__(self, style, points=0, history=None): create/initialize fields for each parameter.
o If history is None, then re-assign an empty list to it. Assume it's a list of moves otherwise.
o If style isn't one of our five accepted styles, raise a PlayerException with a message like
"no style 'copykitten'."
• def __str__(self): create/return a string (utilizing Move's str) like: "friend(12)x.x..xx.."
• def __repr__(self): create/return a string like: "Player('grudge', 12, [Move(True), Move(False)])"
• def reset_history(self): reset history to an empty list. Don't change points.
• def reset (self): reset history, and also reset points to zero.
• def update_points(self, amount): increase points by the parameter. Might go negative.
• def ever_betrayed(self): return whether an opponent ever cheated, based on the history.
• def record_opponent_move(self, move): add the given Move to the end of the history.
• def copy_with_style(self): create/return a Player with no history, and matching style to this one.
• def choose_move(self): determine/return what Move to do next, based on the given style and
opponent's move history. This doesn't perform the move though; that's the job of the run_turn function.
o See the previous pages' description for the five types of players and their behaviors; all of that decision
logic does in fact get implemented here!
Required Functions
These functions are not part of any of the previous classes, but they can use the class definitions to make
objects, call their methods, and interact with them. The classes gave us new types, now let's put them to use!
• def turn_payouts(move_a, move_b): return a tuple of the payouts players a and b get with those moves.
o if both cooperate, each gets +2. So you would return (2,2).
o if both cheat, each gets +0.
o if one cheats and the other cooperates, the cheater gets +3 and the cooperator gets -1.
• def build_players(initials): given a string of initials, create and return a list of Players of those
styles, with default values for all other parameters (points, history).
o If some other character is present, raise a PlayerException with the message like
"no style with initial 'q'."
o Example: build_players("pf") ⟶ [Player('friend', 0, []), Player('previous', 0, [])]
• def composition(players): given a list of players, create and return a dictionary of each player type (the
keys) and how many of that style were in the list of given players. Don't include styles with zero players.
o Example: {"friend":5, "previous":9, "grudger":1} # no detectives/cheaters
o Hint: you might want a helper function that prints this out nicely to help you debug other stuff.
• def run_turn(player_a, player_b): have the two players pay 1point to play; get them to choose
moves; record each other's move in history; determine their payouts; and adjust their points. Returns
nothing.
o If both players have the same id(), raise a PlayerException with the message
"players must be distinct."
• def run_game(player_a, player_b, num_turns=5): given two players, reset their histories first, and
then have them play a total of num_turns times together. Returns nothing, but we could inspect their
points/histories later on to see how it went.
o If the players were identical, handle the raised exception by returning prematurely (no other effects)
 <p>
