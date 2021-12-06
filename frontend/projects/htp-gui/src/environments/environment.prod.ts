import {environment as defaultEnvironment} from './environment.defaults';

export const environment = {
  ...defaultEnvironment,
  production: true,
  mapboxToken: '{{ mapbox_token }}',
  baseAPIURL: 'https://hiketheplanet.info/api'
};
// TODO: add defaults
