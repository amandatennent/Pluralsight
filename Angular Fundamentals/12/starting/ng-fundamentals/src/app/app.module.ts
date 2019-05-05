import { NgModule } from '@angular/core'
import { BrowserModule } from '@angular/platform-browser'
import { RouterModule, ActivatedRouteSnapshot } from '@angular/router'
import { FormsModule, ReactiveFormsModule } from '@angular/forms'

import {
  EventsListComponent,
  EventThumbnailComponent,
  EventService,
  EventDetailsComponent,
  CreateEventComponent,
  EventRouteActivator,
  EventListResolver,
  CreateSessionComponent,
  SessionListComponent,
  DurationPipe
} from './events/index'
import { EventsAppComponent } from './events-app.component'
import { NavBarComponent } from './nav/nav-bar.component'
import { TOASTR_TOKEN, Toastr } from './common/toastr.service'
import { appRoutes } from './routes'
import { Error404Component } from './errors/404.component'
import { AuthService } from './user/auth.service'
import { CollapsibleWellComponent } from './common/collapsible-well.component';

// declare let toastr:Toastr
let toastr:Toastr = window['toastr'];

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot(appRoutes)
  ],
  declarations: [
    EventsAppComponent,
    EventsListComponent,
    EventThumbnailComponent,
    EventDetailsComponent,
    NavBarComponent,
    CreateEventComponent,
    Error404Component,
    CreateSessionComponent,
    SessionListComponent,
    CollapsibleWellComponent,
    DurationPipe
  ],
  providers: [
    EventService, 
    { provide: TOASTR_TOKEN, useValue: toastr },
    EventRouteActivator,
    EventListResolver,
    AuthService,
    { 
      provide: 'canDeactivateCreateEvent', 
      useValue: checkDirtyState 
    }
  ],
  bootstrap: [EventsAppComponent]
})
export class AppModule {}

export function checkDirtyState(component:CreateEventComponent) {
  if (component.isDirty)
    return window.confirm('You have not saved this event, do you really want to cancel?')
  return true
}