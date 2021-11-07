import { TestBed } from '@angular/core/testing';

import { HtpClient } from './htp.client';

describe('HtpClient', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: HtpClient = TestBed.get(HtpClient);
    expect(service).toBeTruthy();
  });
});
