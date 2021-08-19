#!/usr/bin/nodejs

$("#btn").click(function () {

    // Capturando las dos imagenes a traves de su id
    let imagen_uno = document.getElementById('img_one');
    let file_uno = imagen_uno.files[0];

    let imagen_dos = document.getElementById('img_two');
    let file_dos = imagen_dos.files[0];

    

    if (file_uno == undefined | file_dos == undefined) {
        alert('Upload 2 images');
    } else {

        /* PRIMERA IMAGEN */
    
        // Removiendo la extension de la imagen
        let nombreUnoNoExt = file_uno.name.split('.')[0];
    
        // Obteniendo el src path de la primera imagen y haciendo split para quitarle (data:image/...)
        let src_uno = document.getElementById('imagen_uno').getAttribute('src');
        let srcSub_uno = src_uno.split(',')[1];
    
    
    
        /* SEGUNDA IMAGEN */
    
        // Removiendo la extension de la imagen
        let nombreDosNoExt = file_dos.name.split('.')[0];
    
        // Obteniendo el src path de la segunda imagen y haciendo split para quitarle (data:image/...)
        let src_dos = document.getElementById('imagen_dos').getAttribute('src');
        let srcSub_dos = src_dos.split(',')[1];
    
    
    
        /* OBJETO DE IMAGENES */
    
        // Creando un objeto con las imagenes para enviarlas a flask server
        const imagesObj = {
            nombre_uno: file_uno.name,
            name_uno: nombreUnoNoExt,
            type_uno: file_uno.type,
            source_uno: srcSub_uno,
            
            nombre_dos: file_dos.name,
            name_dos: nombreDosNoExt,
            type_dos: file_dos.type,
            source_dos: srcSub_dos
        };
    
        // console.log(newObj.nombre);
    
        const newImage = JSON.stringify(imagesObj);
    
        $.ajax({
            url: '/respuesta',
            type: 'POST',
            data: newImage,
            contentType: 'application/json',
            success: function (respuesta) {
                console.log(respuesta);
    
                let respImage = document.getElementById('response');
                respImage.innerHTML = "<img src=data:image/jpg;base64," + respuesta + " class=\"resp_image\" id=\"response_image\">"
            }
        });
    }
});
