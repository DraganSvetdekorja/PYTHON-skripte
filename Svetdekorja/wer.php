<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../../../favicon.ico">
    <title>Starter Template · Bootstrap</title>
    
    <!--Template based on URL below-->
    <link rel="canonical" href="https://getbootstrap.com/docs/4.3/examples/starter-template/">

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <!-- Place your stylesheet here-->
    <link href="/css/stylesheet.css" rel="stylesheet" type="text/css">
</head>

<body>



<main role="main" class="container">
<div class="page-title-wrapper">
    <h1 class="page-title">
        <span class="base" data-ui-id="page-title-wrapper">Kalkulator števila potrebnih rol tapet</span>    </h1>
    </div>
<div class="page messages"><div data-placeholder="messages"></div>
<div data-bind="scope: 'messages'">
    <!-- ko if: cookieMessages && cookieMessages.length > 0 --><!-- /ko -->

    <!-- ko if: messages().messages && messages().messages.length > 0 --><!-- /ko -->
</div>

</div><div class="columns"><div class="column main"><input name="form_key" type="hidden" value="RyeRcHCx64ehXrz8">


<!-- /ko -->
        
</div>



<div class="container">
<div class="row">
<div class="col">
	<p>Kalkulator rol je enostaven način za izračun števila potrebnih rol tapet za vašo steno. Kalkulator upošteva vse ključne podatke za natančen izračun.</p>
	<p>&nbsp;</p>
	<p><strong>- Dimenzija stene</strong>; vnesite širino in višino stene na katero lepite tapeto</p>
	<p><strong>- Dimenzija tapete</strong>; vnesite širino in dolžino tapete. Podatek najdete v podrobnostih artikla (npr. 10,05 m x 0,53 m)</p>
	<p><strong>- Ima tapeta ujemanje vzorca/zamik</strong>; tapeta je lahko brez ujemanja vzorca ali z ujemanjem vzorca, kar pomeni, da je potrebno pri polaganju pravilno postaviti vsak naslednji pas, tako da se vzorec na steni lepo sestavi. Ujemanje vzorca je lahko navadno (npr: n<span>aravnost - 28 cm) ali ujemanje z zamikom (npr: z zamikom 64/32 cm) kjer je prva številka (64 cm) ujemanje vzorca in druga (32 cm) zamik. Podatke o ujemanju vzorca in zamiku najdete v podrobnostih artikla.</span></p>
	<p><strong>- Dodatek k obrezovanju robov</strong>; pri polaganju pasov tapet, pasove obrežemo na zgornjem in spodnjem robu. Ponavadi pustimo za odrez 2 cm zgoraj in 2 cm spodaj. Ta podatek upošteva skupen odrez na pas, v našem primeru 4 cm (2 cm zgoraj in 2 cm spodaj). Podatek je pomemben za natančen izračun števila potrebnih rol tapet.</p>
	<p><strong>- Rezervna rola</strong>; za tiste, ki želijo biti na varni strani.</p>
	<p><strong>- Rezultat</strong>; Izračun števila potrebni rol glede na vnešene podatke (*izračun je informativen)</p>
</div>
<div class="col">

	<div id="kalkulator-rol-ccc">

	<script type="text/javascript" src="./pub/media/kalkulator.js"></script>

	<div id="kalkulator-rol" style="max-width: 500px;">
	<div class="kalkulator-content">
		<div class="section-title">Kalkulator števila potrebnih rol</div>
		<ul class="section">
		<li>
			<h4>Dimenzija stene</h4>
			<div class="col">
				<label>Širina stene</label>
				<div class="input-text"><input type="text" class="roll-input" id="wall-width" name="wall-width" placeholder="300"> cm</div>
			</div>
			<div class="col">
				<label>Višina stene</label>
				<div class="input-text"><input type="text" class="roll-input" id="wall-height" name="wall-height" placeholder="250"> cm</div>
			</div>
			<div class="clear"></div>
		</li>
		<li>
			<h4>Dimenzija tapete</h4>
			<div class="col">
				<label>Širina tapete</label> 
				<div class="input-text"><input type="text" class="roll-input" id="roll-width" name="roll-width" placeholder="53"> cm</div>
			</div>
			<div class="col">
				<label>Dolžina tapete</label> 
				<div class="input-text"><input type="text" class="roll-input" id="roll-length" name="roll-length" placeholder="1005"> cm</div>
			</div>
			<div class="clear"></div>
		</li>
		<li>
			<h4>Ima tapeta ujemanje vzorca/zamik?</h4>
			<input type="radio" class="roll-radio match" name="match" value="no" id="match_no" checked="checked">
			<label for="match_no">Ne, tapeta nima ujemanja vzorca</label>
			<div class="clear"></div>
			<input type="radio" class="roll-radio match" name="match" value="yes" id="match_yes">
			<label for="match_yes">Da, tapeta ima ujemanje vzorca</label>
			<div class="clear"></div>
			<div class="match_yes" style="display: none;">
				<label>Ujemanje vzorca</label>
				<div class="input-text"><input type="text" class="roll-input" id="matching" name="matching" placeholder="64"> cm</div>
				<div class="clear"></div>
			</div>
			<input type="radio" class="roll-radio match" name="match" value="yes_delay" id="match_yes_delay">
			<label for="match_yes_delay">Da, tapeta ima ujemanje vzorca in zamik</label>
			<div class="match_yes_delay" style="display: none;">
				<label>Ujemanje vzorca</label>
				<div class="input-text"><input type="text" class="roll-input" id="matching" name="matching" placeholder="64"> cm</div>
				<label>Zamik</label>
				<div class="input-text"><input type="text" class="roll-input" id="delay" name="delay" placeholder="32"> cm</div>
			</div>
		</li>
		<li>
			<h4>Dodatek k obrezovanju robov</h4>
			<label>Odrez na pas</label>
			<div class="input-text"><input type="text" class="roll-input" id="trimming" name="trimming" placeholder="4"> cm</div>
			<small>(max 10 cm)</small>
		</li>
		<li>
			<h4>Želite biti na varni strani (rezervna rola)?</h4>
			<input type="radio" class="roll-radio spare" name="spare" value="no" id="spare_no" checked="checked">
			<label for="spare_no">Ne</label>
			<input type="radio" class="roll-radio spare" name="spare" value="yes" id="spare_yes">
			<label for="spare_yes">Da (+1 rola)
		</label></li>
		</ul>
		<div class="results">
			<h3>Rezultat</h3>
			<div class="result">Število potrebnih rol:   <div id="required-rolls">2</div></div>
			<small>* Izračun je zgolj informativen</small>
		</div>
	</div>
	</div>


	</div>

</div>
</div></div></div></div></main>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>
</html>