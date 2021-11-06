import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { TrailheadListComponent } from './trailhead-list.component';

describe('TrailheadListComponent', () => {
  let component: TrailheadListComponent;
  let fixture: ComponentFixture<TrailheadListComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ TrailheadListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TrailheadListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
