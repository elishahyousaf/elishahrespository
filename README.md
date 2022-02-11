
  
import 'jest-preset-angular/setup-jest';

/* global mocks for jsdom */
const mock = () => {
  let storage: { [key: string]: string } = {};
