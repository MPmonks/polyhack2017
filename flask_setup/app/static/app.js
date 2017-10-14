var x = {};

$("#button1").click(function()
{
	x.text = $("input[name=calendar]").val();
});

$("#button2").click(function()
{
	$.ajax({
	type: "POST",
	url: "http://localhost:3333/give",
	data: x
	});
	
});
