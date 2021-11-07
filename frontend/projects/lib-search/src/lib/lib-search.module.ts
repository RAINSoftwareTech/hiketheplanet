import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { MatFormFieldModule } from '@angular/material/form-field';

import { VendorsModule } from 'vendors';

import { SearchBarComponent } from './search-bar/search-bar.component';



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
