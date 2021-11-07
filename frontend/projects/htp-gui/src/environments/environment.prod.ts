import {environment as defaultEnvironment} from './environment.defaults';

export const environment = {
  ...defaultEnvironment,
  production: true,
  mapboxToken: '{{ mapbox_token }}',
  baseAPIURL: 'https://api.hiketheplanet.info'
};
// TODO: add defaults
