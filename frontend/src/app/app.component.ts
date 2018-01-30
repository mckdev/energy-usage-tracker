import { Component, isDevMode } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  static = 'static/assets';

  constructor() {
	if(isDevMode()) {
	  this.static = 'assets';
	}
  }
}
