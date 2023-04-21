function fadeNotification(id) {
    var notification = document.getElementById(id);
    if (notification){
    setTimeout(
    function() {
        notification.classList.add('transition-opacity', 'duration-1000', 'ease-out');
        notification.classList.add('opacity-0', 'hidden');
    }, 4000);
    }
}

function notify(message,alertType="success",notifyId="notification"){
  // remove old notification before posting a new one
  var alertsDiv = document.getElementById(notifyId)
  if (alertsDiv){
      alertsDiv.remove()
  }
  // create alerts div
  var alertDiv = document.getElementById('alerts');
  alertDiv.className = "flex flex-col items-end w-full fixed top-20";
  alertDiv.id = "alerts"
  // create notify div
  var notifyDiv = document.createElement("div");
  notifyDiv.id = notifyId
  // define base classes
  var notifyBaseClasses = "ring-2 hover:opacity-100 transition-opacity duration-200 opacity-80 w-11/12\
                          flex p-2 m-4 mt-0 rounded-lg lg:w-1/3 md:w-1/2 ";
  // define colors
  var notifyRed = "ring-red-800 dark:ring-red-400 hover:bg-red-800 hover:text-sky-100\
                  dark:hover:bg-red-400 dark:hover-text-sky-100 bg-red-50 dark:bg-gray-800\
                  dark:text-red-400 text-red-800";
  var notifyGreen="ring-green-800 dark:ring-green-400 hover:bg-green-800 hover:text-sky-100\
                  dark:hover:bg-green-400 dark:hover-text-sky-100 bg-green-50 dark:bg-gray-800\
                  dark:text-green-400 text-green-800";
  var notifyBlue="ring-blue-800 dark:ring-blue-400 hover:bg-blue-800 hover:text-sky-100\
                  dark:hover:bg-blue-400 dark:hover-text-sky-100 bg-blue-50 dark:bg-gray-800\
                  dark:text-blue-400 text-blue-800";
  // set role to alert
  notifyDiv.role = "alert";
  // set info SVG
  var infoSVG = "<svg aria-hidden='true' class='flex-shrink-0 w-5 h-5' fill='currentColor'\
              viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'><path fill-rule='evenodd'\
              d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1\
              1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z' clip-rule='evenodd'></path></svg>\
              <span class='sr-only'>Info</span>";
  var notifyClasses = notifyBaseClasses;
  switch(alertType){
      case "error":
          notifyClasses += notifyRed;
      case "success":
          notifyClasses += notifyGreen;
      case "info":
          notifyClasses += notifyBlue;
      default:
          notifyClasses += notifyGreen;
  }
  notifyDiv.classList = notifyClasses;
  var notifyMsg = document.createElement("div");
  notifyMsg.ClassList = "opacity-100 ml-3 text-sm font-medium";
  if (alertType === "info"){
      notifyMsg.innerHTML = infoSVG;
  }
  notifyMsg.innerHTML += message;

  // start building
  alertDiv.appendChild(notifyDiv);
  notifyDiv.appendChild(notifyMsg);

  // add auto fade script
  var autoFade = document.createElement("script");;
  autoFade.innerHTML = "fadeNotification('"+notifyId+"')";
  alertDiv.appendChild(autoFade);
}

let formClass = "w-screen-lg mb-4";

let labelClass = "block mt-4 mb-1 text-sm font-medium text-gray-900 dark:text-white";

let formFieldClass = "text-sm border block p-2.5 w-full rounded-lg\
    border-gray-300 dark:border-gray-600 focus:border-primary-500 dark:focus:border-primary-500\
    focus:ring-primary-500 dark:focus:ring-primary-500 dark:placeholder-gray-400";

let submitClass = "lg:col-span-2 inline-flex items-center px-5 text-sm font-medium text-center\
    text-white bg-blue-800 rounded-lg focus:ring-4 focus:ring-primary-200\
    dark:focus:ring-primary-900 hover:bg-primary-800 mt-2 px-5 py-2.5";

let enabledClass = " bg-gray-50 dark:bg-gray-700 dark:text-white text-gray-900";

let disabledClass = " bg-slate-500 text-black";

let origin = window.location.origin;

let apiBase = origin + "/api/";

let forms = [];

function createInput(value,data,inputType="text"){
    var elementTag = "input";
    var elementType = inputType;
    var elementDisable = false;
    if(value.includes("email")){
        elementTag = "input";
        elementType = "email";
        elementDisable=false;
    }
    else if(value.includes("groups") || value.includes("display")){
        elementTag = "input";
        elementType="text";
        elementDisable=false;
    }
    else if(value.includes("user") || value.includes("id")){
        elementTag = "input";
        elementType="text";
        elementDisable=true;
    }

    var element = document.createElement(elementTag);
    element.name = value;
    element.className = formFieldClass;
    element.readOnly=elementDisable;

    if (elementDisable){
        element.className += disabledClass;
    }
    else{
        element.className += enabledClass;
    }
    if(elementTag == "input"){
        element.type = elementType;
        element.value = data;
    }
    else if(elementTag == "textarea"){
        element.innerHTML = data;
    }
    

    return element;
}



async function apiGetData(baseID,parentID) {
    source = apiBase + baseID;
    const response = await fetch(source);
    const jsonData = await response.json();
    console.log(source)
    console.log(response)
    console.log(jsonData)
    if(jsonData['Error'] === 'Invalid Request'){
        var message = "Cannot retrieve data from "+source;
        notify(message,alertType="error",notifyId="getDataError");
    }
    else{
        parent = document.getElementById(parentID)
        parent.innerHTML = "";
        for (let index in jsonData){
            var div = document.createElement("div");
            divID = baseID+"-"+index+"-container";
            div.id=divID;
            div.className=formClass;
            parent.appendChild(div);
            var form = document.createElement("form");
            formID = baseID+"-"+index;
            form.name=formID;
            form.id=formID;
            form.className = formClass;
            div.appendChild(form);
            var elements = {};
            var textareaExists = false;
            var loopIndex = 1;
            for (let value in jsonData[index]){
                elements['id'] = createInput('id',index)
                if (value.includes("hash")){
                }
                else if(value.includes("note")){
                    textareaExists = true;
                    textareaID = "note";
                    var textarea = document.createElement("textarea");
                    textarea.id = textareaID;
                    textarea.name = textareaID;
                    textarea.cols = "2";
                    textarea.className = formFieldClass + enabledClass;
                    textarea.innerHTML = jsonData[index][value];
                }
                else{
                    elements[value] = createInput(value,jsonData[index][value]);
                }
            }
            for(let element in elements){
                if (elements[element].type !== 'hidden'){
                    var label = document.createElement("label");
                    label.for = element;
                    label.className = labelClass;
                    label.innerHTML = element;
                    form.appendChild(label);
                }
                form.appendChild(elements[element]);
            }
            if (textareaExists){
                var label = document.createElement("label");
                label.for = textareaID;
                label.className = labelClass;
                label.innerHTML = textareaID;
                form.appendChild(label);
                form.appendChild(textarea);
            }
            var submit = document.createElement("button");
            submitID = baseID+"-"+index+"-submit";
            submit.id = submitID;
            submit.innerHTML = "Save";
            submit.className = submitClass;
            submit.type="button";
            submit.setAttribute("onclick","apiPostData(document.querySelector('#"+formID+"'),'"+baseID+"')");
            form.appendChild(submit);
            forms.push(formID);
        }
        notify("Successfully retrieved data from API",alertType="success",notifyId="dataRefreshed")
    }
}



async function apiPostData(form,apiEndpoint) {
    console.log(form)
    // Convert form data to JSON format
    const postForm = new FormData(form);
    const jsonObject = {};
    postForm.forEach((value, key) => jsonObject[key] = value);
    const jsonData = JSON.stringify(jsonObject);
    console.log("JSON OBJECT: "+jsonObject)
    var postURL = apiBase + apiEndpoint;
    console.log(postURL)
    
    const rawResponse = await fetch(postURL,{
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: jsonData
    });
    const content = await rawResponse.json();
    console.log(content);
    if (content['return'] === 0){
        console.log('OKAY')
        notify("SUCCESS: "+apiEndpoint+" saved",alertType='success',notifyId="apiPost")
        apiGetData(apiEndpoint,'apiDataForms')
    }
    else{
        msg = "ERROR: " + content['error'];
        notify(msg,alertType='error',notifyId="apiPost")
        console.log(msg)
    }
    console.dir(jsonData)
  }