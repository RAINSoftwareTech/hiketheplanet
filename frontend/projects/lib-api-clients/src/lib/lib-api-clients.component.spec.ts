import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LibApiClientsComponent } from './lib-api-clients.component';

describe('LibApiClientsComponent', () => {
  let component: LibApiClientsComponent;
  let fixture: ComponentFixture<LibApiClientsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LibApiClientsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LibApiClientsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
