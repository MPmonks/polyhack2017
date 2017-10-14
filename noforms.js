//reference for sending input without forms
//forms are built to fire off request!
//design choice: use jquery/js button callback instead

//TO INCLUDE IN HTML: (includes jquery)
// <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

//stores input values in list
dataList = {};

//button to click to input data
//temp id name - change to class
$("#b").click(function() {
    //TO DO: make sure button is only clicked once
    //or when clicked, only overrides element at previous index, doesn't add to list
    //must make design implementation decisions ofc
    dataList.push($("input[name=event]").val())
});

//button to send all info at once to python server
//temp id name
$("#b2").click(function() {
    $.ajax({
        url: "localhost:3000/path/",
        data: dataList;
        dataType: "json";
    )
});
