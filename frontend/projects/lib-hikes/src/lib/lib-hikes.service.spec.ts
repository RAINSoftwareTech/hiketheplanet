import { TestBed } from '@angular/core/testing';

import { LibHikesService } from './lib-hikes.service';

describe('LibHikesService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: LibHikesService = TestBed.get(LibHikesService);
    expect(service).toBeTruthy();
  });
});
