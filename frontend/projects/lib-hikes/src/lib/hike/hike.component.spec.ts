import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { HikeComponent } from './hike.component';

describe('HikeComponent', () => {
  let component: HikeComponent;
  let fixture: ComponentFixture<HikeComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ HikeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HikeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
