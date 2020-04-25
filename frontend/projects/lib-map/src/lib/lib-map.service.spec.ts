import { TestBed } from '@angular/core/testing';

import { LibMapService } from './lib-map.service';

describe('LibMapService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: LibMapService = TestBed.get(LibMapService);
    expect(service).toBeTruthy();
  });
});
