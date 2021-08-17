# Trust-Game
<link href="https://fonts.googleapis.com/css2?family=Baloo+Tammudu+2&display=swap" rel="stylesheet">


<h>Two players will face each other. They each decide independently to "cooperate" or "cheat". If they both cooperated, they each win two points. If they both cheated, nobody wins anything. If one cooperates and one cheats, the cheater gets +3 and the cooperator loses a point.</h>
  
<p>One turn is defined as each player making a choice, and winning or losing some points as a result.
Shared history against this player is available to players, and they may use this to guide their decision.
It costs one point to play a turn. A player's points may go negative, and yet they can still spend/lose
more points.</p>

<p>• One game is defined as two players playing multiple turns together. Their increasingly shared history
will certainly affect their chosen behavior.</p>
<p>• A tournament involves multiple players. Each round, all players play each other once, accumulating
or losing points. At the end of the round, some lowest scorers are removed (and any others with
negative points), and some highest scorers are duplicated. After all rounds have been played, we see
the "evolved" population of who remains, as a summary dictionary of the count of each style of player
that survived.</p>

<p>Kinds of Players
There are five kinds of players in our version of the tournament.</p>
<p>• <b>previous</b> starts by cooperating, then always copies the previous move of their opponent.</p>
<p>• <b>friend</b> always cooperates, no matter what. May be vulnerable to abuse!</p>
<p>• <b>cheater</b> never cooperates.</p>
<p>• <b>grudger</b> cooperates as long as the opponent does, but after one non-cooperation, never
cooperates ever again with this opponent.</p>
<p>• <b>detective</b> starts with cooperate, cheat, cooperate, cooperate; then if they've never been betrayed,
they cheat. If ever they are betrayed, they behave like previous does.</p>

