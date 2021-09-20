$('#make_post').submit(function(e){
    e.preventDefault()
    $.ajax({
        url:$(this).attr('action'),
        method:'POST',
        data: $(this).serialize(),
        success:function(response){
            $('#posts_container').html(response)
        }
    })
})

$('#like_post').submit(function(e){
    e.preventDefault()
    $.ajax({
        url:$(this).attr('action'),
        method:$(this).attr('method'),
        data: $(this).serialize(),
        success:function(response){
            $('#likes_container').html(response)
        }
    })
})
