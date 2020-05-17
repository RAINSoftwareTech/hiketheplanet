import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MappedTrailheadsComponent } from './mapped-trailheads.component';

describe('MappedTrailheadsComponent', () => {
  let component: MappedTrailheadsComponent;
  let fixture: ComponentFixture<MappedTrailheadsComponent>;

  beforeEach(async(() => {
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
