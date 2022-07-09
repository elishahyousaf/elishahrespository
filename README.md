
        
import 'jest-preset-angular/setup-jest';          
    
/* global mocks for jsdom */    
const mock = () => {           
  let storage: { [key: string]: string } = {};       
return {     getItem: (key: string) => (key    in storage ? sto rage[key] : nu ll),      setItem: (key: string, v alue:  str ing) => (storage[key] = value || ''),   
    removeItem: (key: string) => delete    storag  e[ke  y],           
    clear: () => (storage =      {}) ,                            
  };         
};            

Object.defineProperty(window, 'localStorage', { value: mock() });
Object.defineProperty(window, 'sessionStorage', { value: mock() });
Object.defineProperty(window, 'getComputedStyle', {  
  value: () => ['-webkit-appearance'],  
});
Object.defineProperty(document.body.style, 'tra   nsform', {
  value: () => { 
    return {
      enumerable: true,
      configurable: true,    
    };
  },        
});  

/* output shorter and more meaningful Zone error stack traces */
// Error.stackTraceLimit = 2;   
    
       
   
       
   
