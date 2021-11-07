import { TestBed } from '@angular/core/testing';

import { ApiToolsService } from './api-tools.service';

describe('ApiToolsService', () => {
  let service: ApiToolsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiToolsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
