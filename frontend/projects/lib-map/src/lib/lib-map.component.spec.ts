import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LibMapComponent } from './lib-map.component';

describe('LibMapComponent', () => {
  let component: LibMapComponent;
  let fixture: ComponentFixture<LibMapComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LibMapComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LibMapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
