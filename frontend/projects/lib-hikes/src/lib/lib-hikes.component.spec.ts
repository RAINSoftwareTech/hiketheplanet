import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { LibHikesComponent } from './lib-hikes.component';

describe('LibHikesComponent', () => {
  let component: LibHikesComponent;
  let fixture: ComponentFixture<LibHikesComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ LibHikesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LibHikesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
