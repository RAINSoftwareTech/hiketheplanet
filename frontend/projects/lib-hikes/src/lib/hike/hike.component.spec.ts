import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HikeComponent } from './hike.component';

describe('HikeComponent', () => {
  let component: HikeComponent;
  let fixture: ComponentFixture<HikeComponent>;

  beforeEach(async(() => {
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
