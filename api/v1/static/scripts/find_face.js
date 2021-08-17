#!/usr/bin/nodejs

$("#btn").click(function () {
    let imagen_uno = document.getElementById('img_one');
    let file_uno = imagen_uno.files[0];

    let imagen_dos = document.getElementById('img_two');
    let file_dos = imagen_dos.files[0];

    //console.log(file_uno);
    //console.log(file_dos);

    const file = new FileReader();

    /* file.addEventListener("load", function () {
        let st = this.result;
    }); */

    console.log(file.result);

    const newObj = {
        nombre: file_uno.name,
        tipo: file_uno.type,
        size: file_uno.size,
        lastModified: file_uno.lastModified,
        lasModifiedDate: file_uno.lasModifiedDate
    };

    const newImage = JSON.stringify(newObj);

    $.ajax({
        url: '/respuesta',
        type: 'POST',
        data: newImage,
        contentType: 'application/json',
        success: function (respuesta) {
            console.log(respuesta);
        }
    });
});
