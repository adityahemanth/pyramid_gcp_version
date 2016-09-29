function set_data(data) {

	reset_table()
	var this_node = data
	$.get('/lcco', {
	 	request : data
	}, function(data, status) {
	    data = JSON.parse(data)

	    if(data.children.length > 0){

			for(i = 0; i < data.children.length; i++){
				//var stat = get_stats(data.children[i].LCCN)
				var row = $('<tr>')
				row.append(
					$('<td>').attr('class', 'node-target').append(
						$('<strong>').append(data.children[i].LCCN)
					),
					$('<td>').attr('class', 'node-item btn-default').append(data.children[i].description),
					$('<td>').append(STATS[data.children[i].LCCN]),
					$('<td>').append( 
						$('<a>').attr('class', 'word-link btn btn-primary').append(
							$('<p>').attr('class', 'hidden').append(data.children[i].LCCN),
							'words'
						)
					)
				)
				table.append(row)
			}
	    }

	    else {

	    	var row = $('<tr>').append(
	    			$('<h3>').append( this_node + 'has not children nodes')
	    		)
	    	table.append(row)
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


// resets the table 
function reset_table() {

	table.empty()
	table.append(
		$('<tbody>').append( 
			$('<tr>').append(
				$('<th>').append('LCCN'),
				$('<th>').append('Description'),
				$('<th>').append('MARC count'),
				$('<th>').append('Word Frequency')
			)
		)
	)
}


function get_stats() {
	$.get('/stats',
		function(stat, status){ 
			if (stat != null) {
				stat = JSON.parse(stat)
				STATS = stat
				set_data('1')
		        back.push('1')
		        set_back()
			}
			else {
				return 0
			}
		}
	)
}


function set_word_freq(node) {

	reset_word_table()
	$.get('/frequency', {
	 	node : node
	}, function(data, status){
		data = JSON.parse(data)
	    if(data != 0) {

	    	for(item in data) {
    			var row = $('<tr>')
    			row.append(
					$('<td>').append($('<strong>').append(item)),
					$('<td>').append(data[item])
				)
				word_table.append(row)
	    	}
	    }

	    else {

	    	word_table.empty()
    		var row = $('<tr>')
			row.append(
				$('<td>').append($('<strong>').append('No words in this category'))
			)
			word_table.append(row)
	    }

	});
}


function reset_word_table() {
	word_table.empty()
	word_table.append(
		$('<tbody>').append( 
			$('<tr>').append(
				$('<th>').append('Word'),
				$('<th>').append('Frequency')
			)
		)
	)
}




