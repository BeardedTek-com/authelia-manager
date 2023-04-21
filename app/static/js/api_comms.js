let formClass = "w-screen-lg mb-4"

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

let apiBase = origin + "/api/"

let forms = []

function createElement(parentid,index,value,data){
    var elementTag = "input";
    var elementType = "text";
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
    else if(value.includes("user")){
        elementTag = "input";
        elementType="text";
        elementDisable=true;
    }

    var element = document.createElement(elementTag);
    element.className = formFieldClass;
    element.name = value;
    element.disabled=elementDisable;
    if(elementTag == "input"){
        element.type = elementType;
        element.value = data;
    }
    else if(elementTag == "textarea"){
        element.innerHTML = data;
    }
    if (elementDisable){
        element.className += disabledClass;
    }
    else{
        element.className += enabledClass;
    }

    return element;
}



async function getJSONData(baseID,parentID) {
    source = apiBase + baseID;
    const response = await fetch(source);
    const jsonData = await response.json();
    console.log(source)
    console.log(response)
    console.log(jsonData)
    if(jsonData['Error'] === 'Invalid Request'){
        var message = "Cannot retrieve data from "+source;
        notify(message,"error","getDataError");
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
                    elements[value] = createElement(formID,index,value,jsonData[index][value]);
                }
            }
            for(let element in elements){
                var label = document.createElement("label");
                label.for = element;
                label.className = labelClass;
                label.innerHTML = element;
                form.appendChild(label);
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
            submit.innerHTML = "Update";
            submit.className = submitClass;
            submit.type="button";
            submit.onclick="submitformData(document.querySelector('#"+formID+"'))"
            form.appendChild(submit);
            forms.push(formID)
        }
        notify("Successfully retrieved data from API","success","dataRefreshed")
    }
}



async function submitFormData(form,apiEndpoint) {
    console.log(form)
    // Convert form data to JSON format
    const postForm = new FormData(form);
    const jsonObject = {};
    postForm.forEach((value, key) => jsonObject[key] = value);
    const jsonData = JSON.stringify(jsonObject);
    console.log(jsonObject)
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
        getJSONData('users','jsonDataContents')
    }
    else{
        msg = "ERROR: " + content['error'];
        notify(msg,'error')
        console.log(msg)
    }
  
  // Submit form data using Fetch API
  //  try {
  //    const response = await 
  //    const response = await fetch(postForm.action, {
  //      method: postForm.method,
  //      body: jsonData,
  //      headers: {
  //        'Content-Type': 'application/json'
  //      }
  //    });
  //    const data = await response.json();
  //    console.log(data); // Handle response data
  //  } catch (error) {
  //  }
  
    console.log(jsonData)
  }