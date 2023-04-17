    // create an array of objects with the id, trigger element (eg. button), and the content element
    const accordionItems = [
        {
            id: 'config-main-heading',
            triggerEl: document.querySelector('#config-main-heading'),
            targetEl: document.querySelector('#config-main-body'),
            active: true
        },
        {
            id: 'config-totp-heading',
            triggerEl: document.querySelector('#config-totp-heading'),
            targetEl: document.querySelector('#config-totp-body'),
            active: false
        },
        {
            id: 'accordion-example-heading-3',
            triggerEl: document.querySelector('#config-auth_backend-heading'),
            targetEl: document.querySelector('#config-auth_backend-body'),
            active: false
        }
        ];
    
        // options with default values
        const options = {
        alwaysOpen: false,
        activeClasses: 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white',
        inactiveClasses: 'text-gray-500 dark:text-gray-400',
        onOpen: (item) => {
            console.log('accordion item has been shown');
            console.log(item);
        },
        onClose: (item) => {
            console.log('accordion item has been hidden');
            console.log(item);
        },
        onToggle: (item) => {
            console.log('accordion item has been toggled');
            console.log(item);
        },
        };
    
        import { Accordion } from 'flowbite';
    
        /*
        * accordionItems: array of accordion item objects
        * options: optional
        */
        const accordion = new Accordion(accordionItems, options);