import { TestBed } from '@angular/core/testing';

import { LibToolsService } from './lib-tools.service';

describe('LibToolsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: LibToolsService = TestBed.get(LibToolsService);
    expect(service).toBeTruthy();
  });
});
