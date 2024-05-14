<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Text Stress Classification</title>

</head>

<body>

    <h1>Text Stress Classification</h1>

    <form action="http://localhost:5000/classify" method="post">

        <label for="text">Enter your text:</label><br>

        <textarea id="text" name="text" rows="4" cols="50"></textarea><br>

        <input type="submit" value="Submit">

    </form>

 

    <?php

    if ($_SERVER["REQUEST_METHOD"] == "POST") {

        $data = array('text' => $_POST['text']);

        $url = 'http://localhost:5000/classify';

        $options = array(

            'http' => array(

                'header' => "Content-type: application/json\r\n",

                'method' => 'POST',

                'content' => json_encode($data)

            )

        );

        $context = stream_context_create($options);

        $result = file_get_contents($url, false, $context);

        if ($result === FALSE) {

            echo "Error: Unable to connect to the server.";

        } else {

            $response = json_decode($result, true);

            echo "<p><strong>Entered text:</strong> " . $response['text'] . "</p>";

            echo "<p><strong>Classification:</strong> " . $response['label'] . "</p>";

        }

    }

    ?>

</body>

</html>