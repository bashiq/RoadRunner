//js file for our web page
//this file will take images captured by the system and display them using this script
//creators Bilal & Kireh

<?php
	header("Content-type: application/javascript");
?>
var $ = function (id) { return document.getElementById(id); };

//directory where images should be stored
var dir = 'imgs/'; // reflect changes on line 17 too

var imageList;

var getImages = function (){
	imageList = [<?php
        $dir='imgs/';
        $files = scandir($dir);

        foreach((array)$files as $file){
		if($file=='.'||$file=='..') continue;
		$fileList[]=$file;
        }

        echo "'".implode("','", $fileList)."'";

	?>];
};

 
var loadImgs = function(){
	getImages();
	var html="<div class=\"row\">";
	for(var i=0; imageList.length > i; i++){	
		html += (" <div class=\"column\"><img src='" + dir + imageList[i] +"' alt=\"road\" style=\"width:100%\"></div>");
	}
	html+= "</div>";
	$("photos").innerHTML= html; 
};



window.onload = function () {
	$("refresh").onclick = loadImgs;
};
