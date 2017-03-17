var newImage = new Image();
newImage.src = imgSrc;
function updateImage(){
    if(newImage.complete){
	document.getElementById("frame").src = newImage.src;
	newImage = new Image();
	newImage.src = imgSrc + "?time=" + new Date().getTime();
    }
    setTimeout(updateImage, 2000);
}

updateImage();
