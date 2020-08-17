import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { VendorsModule } from 'vendors';

import { SearchBarComponent } from './search-bar/search-bar.component';
import { MatFormFieldModule } from '@angular/material/form-field';



@NgModule({
  declarations: [ SearchBarComponent],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    VendorsModule,
    MatFormFieldModule,
  ],
  exports: [SearchBarComponent]
})
export class LibSearchModule { }
