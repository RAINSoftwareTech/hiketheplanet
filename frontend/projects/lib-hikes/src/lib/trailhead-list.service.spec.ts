import { TestBed } from '@angular/core/testing';

import { TrailheadListService } from './trailhead-list.service';

describe('TrailheadListService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TrailheadListService = TestBed.get(TrailheadListService);
    expect(service).toBeTruthy();
  });
});
