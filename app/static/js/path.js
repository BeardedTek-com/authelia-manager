function replaceSrc(element) {
    var path = window.location.pathname;
    var origin = window.location.origin;
    if (path.includes('ui')){
        baseURL = origin + path.split('ui')[0];
    } else if (!path.includes('api')) {
        baseURL = origin + path.split('api')[0];
    } else {
        baseURL = origin + path;
    }
    imgPath = element.src;
    newImgPath = baseURL + imgPath;
    console.log(newImgPath);
    element.src = newImgPath;
}

function replaceAllImgSrc() {
    var path = window.location.pathname;
    if (path.includes('ui')){
        path = path.split('/ui')[0]
    }
    else if (path.includes('api')){
        path = path.split('/api')[0]
    }
    var origin = window.location.origin;
    var imgs = document.getElementsByTagName("img");
    for (var i=0; i < imgs.length; i++) {
        imgSrc = imgs[i].src
        console.log(imgSrc)
        if (!imgSrc.includes(path)) {
            console.log('Adding origin to ' + imgSrc)
            oldSrc = "/static/img"
            console.log('oldSrc: ' + oldSrc)
            newSrc = path + oldSrc
            console.log('newSrc: ' + newSrc)
            imgSrc = imgSrc.replace('/static/img',newSrc)
            imgs[i].src = imgSrc
            console.log(imgs[i])
        }
    }
}

replaceAllImgSrc();