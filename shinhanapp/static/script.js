jQuery(document).ready(function() {
    $(".list-group-item-action").click(function() {
        // alert("Hello");
        let product_id = $(this).attr("id")
        $.get("http://127.0.0.1:8000/product/"+ product_id + "/")
            .then(function(result){
                $("#detailModalTitle").text(result.title);
                $("#detailModalLocation").text(result.location);
                $("#detailModalPrice").text(result.price);
                $("#detailModalContent").html(result.content);
                $("#detailModalImage").attr('src',result.image);
                // $("#detailModalImage").attr('src'); // 이렇게 쓰면 값을 가져옴
                $("#detailModal").modal("show");    
        });
    });
});