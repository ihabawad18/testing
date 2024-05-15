<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Stress Classification</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
    <h1>Text Stress Classification</h1>
    <form id="textForm">
        <label for="text">Enter your text:</label><br>
        <textarea id="text" name="text" rows="4" cols="50"></textarea><br>
        <input type="submit" value="Submit">
    </form>

    <div id="result"></div>

    <script>
        $(document).ready(function(){
            $('#textForm').submit(function(e){
                e.preventDefault();

                var formData = {
                    'text' : $('#text').val()
                };

                $.ajax({
                    type: 'POST',
                    url: 'https://testing-mb1z.onrender.com/predict',
                    data: JSON.stringify(formData),
                    contentType: 'application/json',
                    success: function(response) {
                        console.log(response);
                        $('#result').html('<p><strong>Entered text:</strong> ' + formData['text'] + '</p>' +
                                          '<p><strong>Classification:</strong> ' + response.label + '</p>');
                    },
                    error: function() {
                        $('#result').html('<p>Error: Unable to connect to the server.</p>');
                    }
                });
            });
        });
    </script>
</body>
</html>
