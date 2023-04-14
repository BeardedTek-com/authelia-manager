// set the target element that will be collapsed or expanded (eg. navbar menu)
const $targetEl = document.getElementById('navbar-sticky');

// optionally set a trigger element (eg. a button, hamburger icon)
const $triggerEl = document.getElementById('hamburger');

// optional options with default values and callback functions
const options = {
  onCollapse: () => {
      console.log('element has been collapsed')
  },
  onExpand: () => {
      console.log('element has been expanded')
  },
  onToggle: () => {
      console.log('element has been toggled')
  }
};

import { Collapse } from 'flowbite';

/*
* $targetEl: required
* $triggerEl: optional
* options: optional
*/
const collapse = new Collapse($targetEl, $triggerEl, options);