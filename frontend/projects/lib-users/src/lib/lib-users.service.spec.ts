import { TestBed } from '@angular/core/testing';

import { LibUsersService } from './lib-users.service';

describe('LibUsersService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: LibUsersService = TestBed.get(LibUsersService);
    expect(service).toBeTruthy();
  });
});
