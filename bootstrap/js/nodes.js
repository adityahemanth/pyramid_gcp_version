function set_data(data) {


	list.empty()
	$.get('/lcco', {
	 	request : data
	}, function(data, status){
	    data = JSON.parse(data)
	    if(data != null){

			list.empty()
			for(i = 0; i < data.children.length; i++){
				list.append(
					$('<li>').attr('class', 'list-group-item btn btn-default text-left').append(
						$('<p>').attr('class', 'node-item').append(data.children[i].LCCN , ' : ', data.children[i].description)
					)
				)
			}
	    }
	});
}


function set_back(){

$('#back_list').empty()
	for(i = 0; i < back.length; i++){
	  $('#back_list').append(
	    $('<li>').attr('class', 'back-item btn btn-primary').attr('style', 'margin:3px').append(back[i])
	    )
	}
}

