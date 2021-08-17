#!/usr/bin/nodejs

$("#btn").click(function () {
    let imagen_uno = document.getElementById('img_one');
    let file_uno = imagen_uno.files[0];

    let imagen_dos = document.getElementById('img_two');
    let file_dos = imagen_dos.files[0];

    console.log(typeof(file_uno));
    console.log(file_dos.name);

    const img_uno = {
        nombre: file_uno.name,
        tipo: file_uno.type
    };
    console.log(typeof(img_uno));

    const img_dos = {
        nombre: file_dos.name,
        tipo: file_dos.type
    };
    console.log(img_dos);
})
