/*============================== 
	- MAP JS (ICON MARKER)
	- Template: MARRY - Responsive HTML Wedding Template
	- Author: DoubleEight
	- Version: 1.0.0
	- Website: themeforest.net/user/doubleeight/portfolio
================================= */
	

function initializeMap(data) {
	
	// CHECK WINDOW RESIZE
	var is_windowresize = false;
	$(window).resize(function(){
		is_windowresize = true;
	});
	
	
	//INITIALIZE MAP
	function initialize() {
		
		// Create an array of styles
		//=======================================================================================
  		var styles = [
    		{
      			stylers: [
        			{ hue: "#956267" },
        			{ saturation: -50 }
      			]
    		}
  		];
		
		// Create a new StyledMapType object, passing it the array of styles,
  		// as well as the name to be displayed on the map type control.
  		var styledMap = new google.maps.StyledMapType(styles,
   			{name: "Styled Map"});
			
		
		//DEFINE MAP OPTIONS
		//=======================================================================================
  		var mapOptions = {
			mapTypeId: google.maps.MapTypeId.ROADMAP,	
			panControl: true,
  			zoomControl: true,
  			mapTypeControl: false,
  			streetViewControl: true,
  			overviewMapControl: true,
			scrollwheel: false,
  		};

		//CREATE NEW MAP
		//=======================================================================================
  		var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
		
		//Associate the styled map with the MapTypeId and set it to display.
		map.mapTypes.set('map_style', styledMap);
		map.setMapTypeId('map_style');

		const bounds = new google.maps.LatLngBounds()
		const markersWindows = new Array();
		  
        for (let i=0; i < data.length; i++) {
			var place = data[i];

			const marker = new MarkerWithLabel({
				position: new google.maps.LatLng(place.lat, place.long),
				draggable: false,
				raiseOnDrag: false,
				icon: ' ',
				map: map, 
			  	labelContent: (
					'<div id="gift-marker" class="de-icon circle medium-size" style="background-color:' + 
					place.color + '"><i class="de-icon-' + place.icon + '"></i></div>'
				),
				labelAnchor: new google.maps.Point(27, 27),
				labelClass: "labels" // the CSS class for the label
			});

			const contentString = ''+
			'<div class="info-window-wrapper">'+
				'<h6>' + place.name + '</h6>'+
				'<div class="info-window-desc">' + place.details + '</div>'+
				'<div class="info-window-link">' +
					'<a href="' + place.link + '" target="_blank" class="grey-link with-underline">More Info</a>' +
				'</div>'+
			'</div>';
		
			const marker_infowindow = new google.maps.InfoWindow({
				content: contentString,
				maxWidth: 300,
			});

			markersWindows.push(marker_infowindow);
		
			if (place.open_on_load) {
				marker_infowindow.open(map, marker);
			}

			marker.addListener('click', function() {
				markersWindows.forEach(function(m) {
					m.close();
				});
				marker_infowindow.open(map, marker);	
			});
			bounds.extend({ lat: place.lat, lng: place.long });
		}

		map.fitBounds(bounds);
	}

	// LOAD GMAP
	google.maps.event.addDomListener(window, 'load', initialize);
}