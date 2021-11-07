import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HikeMinimalComponent } from './hike-minimal.component';

describe('HikeMinimalComponent', () => {
  let component: HikeMinimalComponent;
  let fixture: ComponentFixture<HikeMinimalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HikeMinimalComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HikeMinimalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
