import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { MappedTrailheadsComponent } from './mapped-trailheads.component';

describe('MappedTrailheadsComponent', () => {
  let component: MappedTrailheadsComponent;
  let fixture: ComponentFixture<MappedTrailheadsComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ MappedTrailheadsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MappedTrailheadsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
