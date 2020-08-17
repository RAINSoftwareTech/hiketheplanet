import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TrailheadComponent } from './trailhead.component';

describe('TrailheadComponent', () => {
  let component: TrailheadComponent;
  let fixture: ComponentFixture<TrailheadComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TrailheadComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TrailheadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
