import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { LibToolsComponent } from './lib-tools.component';

describe('LibToolsComponent', () => {
  let component: LibToolsComponent;
  let fixture: ComponentFixture<LibToolsComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ LibToolsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LibToolsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
