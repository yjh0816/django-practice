jQuery(document).ready(function() {
    $(".list-group-item-action").click(function() {
        // alert("Hello");
        let product_id = $(this).attr("id")
        $.get("http://127.0.0.1:8000/product/"+ product_id + "/")
            .then(function(result){
                $("#detailModalUsername").text(result.username);
                $("#detailModalTitle").text(result.title);
                $("#detailModalLocation").text(result.location);
                $("#detailModalPrice").text(result.price);
                $("#detailModalContent").html(result.content);
                $("#detailModalImage").attr('src',result.image);
                $("#detailModal").modal("show");    
        });
    });
});