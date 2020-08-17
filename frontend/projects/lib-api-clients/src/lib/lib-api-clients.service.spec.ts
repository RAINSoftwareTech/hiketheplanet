import { TestBed } from '@angular/core/testing';

import { LibApiClientsService } from './lib-api-clients.service';

describe('LibApiClientsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: LibApiClientsService = TestBed.get(LibApiClientsService);
    expect(service).toBeTruthy();
  });
});
