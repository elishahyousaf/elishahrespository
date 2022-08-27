
        
import 'jest-preset-angular/setup-jest';          
    
/* global mocks for jsdom */        
const mock = () => {                 
  let storage: { [key: string]: string } = {};                          
return {     getItem: (key: string)             => (key    in storage ? sto rage[key] : nu ll),      setItem: (key: string, v alue:  str ing) => (storage[key] = value || ''),   
    removeItem: (key: string) => delete    stora   g  e[ke  y],           
    clear: () => (s       torage =      {}) ,                                          
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
  },         n   
});  

/* output shorter and more meaningful Zone erron    r stack traces */
// Error.stackTraceLimit = 2;   
    
       
                
       
   
