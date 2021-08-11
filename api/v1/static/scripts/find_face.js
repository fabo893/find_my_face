#!/usr/bin/nodejs

$("#btn").click(function () {

    $.ajax({
        url: '/upload',
        success: function(response) {
            console.log(response);
        }
    });

    /* let imagen = document.getElementById('img_one');
    let file = imagen.files[0];

    console.log(file);

    testing(file); */
})

/* 
function testing(data){

    let json1 = {
        name: `${data.name}`,
        type: `${data.type}`
    };

    let json = JSON.stringify(json1);

    $.ajax({
        type: 'POST',
        url: '/upload',
        contentType: 'application/json',
        data: json,
        success: function (response) {
            console.log(response);
        }
    });
} */