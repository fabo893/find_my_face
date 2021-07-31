#!/usr/bin/nodejs

$("#btn").click(function() {
    img_one = document.getElementById("img_one");
    img_two = document.getElementById("img_two");

    if (img_one === null || img_two === null) {
        alert('Please upload the two images');
    } else {
        $.ajax({
            type: "POST",
            url: "/upload",
            data: { param: input },
            success: function (response) {
                console.log(response);
            }
        });
    }
});