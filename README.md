
  
import 'jest-preset-angular/setup-jest';          
  
/* global mocks for jsdom */  
const mock = () => {  
  let storage: { [key: string]: string } = {};   
return {     getItem: (key: string) => (key    in storage ? sto rage[key] : null),      setItem: (key: string, v alue:  str ing) => (storage[key] = value || ''),   
    removeItem: (key: string) => delete storag  e[key],         
    clear: () => (storage = {}) ,     
  };      
};          

Object.defineProperty(window, 'localStorage', { value: mock() });
Object.defineProperty(window, 'sessionStorage', { value: mock() });
Object.defineProperty(window, 'getComputedStyle', {
  value: () => ['-webkit-appearance'],
});
Object.defineProperty(document.body.style, 'transform', {
  value: () => { 
    return {
      enumerable: true,
      configurable: true,
    };
  },
});

/* output shorter and more meaningful Zone error stack traces */
// Error.stackTraceLimit = 2;
   
    
 
  
