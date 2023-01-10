<script>
    setInterval(function() {
        $.ajax({
            type : 'get',
            url : '/get_sensor',

            success: function(centimeters) {
                let max = 30;
                let depth = max - centimeters;
                let percent = (depth > 0) ? depth / max : 0;
                let message = (percent > 0) ? (percent * 100).toFixed(0) + '%' : 'EMPTY!';

                $('#output').html(message);
                $('div.water').css({height: 'calc(9rem * ' + percent + ')'});
            },
            error: function(response){
                console.log(response);
            }
        });
    }, 1000);
</script>

