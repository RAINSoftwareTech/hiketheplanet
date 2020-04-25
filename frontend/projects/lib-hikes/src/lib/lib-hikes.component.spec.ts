import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LibHikesComponent } from './lib-hikes.component';

describe('LibHikesComponent', () => {
  let component: LibHikesComponent;
  let fixture: ComponentFixture<LibHikesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LibHikesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LibHikesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
