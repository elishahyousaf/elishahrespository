
  
import 'jest-preset-angular/setup-jest';

/* global mocks for jsdom */
const mock = () => {
  let storage: { [key: string]: string } = {};
return {
    getItem: (key: string) => (key in storage ? storage[key] : null),
    setItem: (key: string, value: string) => (storage[key] = value || ''),
    removeItem: (key: string) => delete storage[key],
    clear: () => (storage = {}),
  };
};
