<h1>Projecte ${project}</h1>
<h2>Benvinguts</h2>
<p>Introdueix la data de naixament: </p>
<form name="form"action="elmeu" method="POST">
	Dia: <input type="text" name="dia" /><br/>
	Mes: <input type="text" name="mes" /><br/>
	<input type="submit" name="enviar" value="Enviar"/>
	
</form>
% if signe:
	<div style="background-color: yellow">Ets signe ${signe} </div>
	<img src="/static/${imatge}.png">
	<p>${frase}</p>
% endif
