#!/usr/bin/nodejs

$("#btn").click(function () {
    let img1 = $(".preview_image_one").attr("src");

    json_img = {'name': 'testing1', 'image': img1};

    json_par = JSON.stringify(json_img);

    $.ajax({
        type: 'POST',
        url: '/upload',
        data: json_par,
        contentType: 'application/json',
        success: function() {
            console.log("Good");
        }
    });
});