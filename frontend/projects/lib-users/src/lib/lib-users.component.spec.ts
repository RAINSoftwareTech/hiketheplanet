import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { LibUsersComponent } from './lib-users.component';

describe('LibUsersComponent', () => {
  let component: LibUsersComponent;
  let fixture: ComponentFixture<LibUsersComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ LibUsersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LibUsersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
