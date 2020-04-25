import { TestBed } from '@angular/core/testing';

import { LibAlertsService } from './lib-alerts.service';

describe('LibAlertsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: LibAlertsService = TestBed.get(LibAlertsService);
    expect(service).toBeTruthy();
  });
});
