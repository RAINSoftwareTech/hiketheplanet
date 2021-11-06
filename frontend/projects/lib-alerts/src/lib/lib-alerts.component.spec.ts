import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { LibAlertsComponent } from './lib-alerts.component';

describe('LibAlertsComponent', () => {
  let component: LibAlertsComponent;
  let fixture: ComponentFixture<LibAlertsComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ LibAlertsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LibAlertsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
