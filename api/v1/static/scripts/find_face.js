#!/usr/bin/nodejs

$("#btn").click(function () {
    let imagen_uno = document.getElementById('img_one');
    let file_uno = imagen_uno.files[0];

    let imagen_dos = document.getElementById('img_two');
    let file_dos = imagen_dos.files[0];

    console.log(file_uno);

    if (file_uno == undefined || file_dos == undefined) {
        alert('Sube las dos imagenes');
    } else {
        comparar(file_uno);
    }
})


function comparar(img_uno){

    let json_parse = img_uno;

    //console.log(json_parse);

    //let json = JSON.stringify(json_parse);

    $.ajax({
        type: 'POST',
        url: 'comparar',
        data: json_parse,
        contentType: false,
        processData: false,
        success: function (response) {
            console.log(response);
        }
    });
}