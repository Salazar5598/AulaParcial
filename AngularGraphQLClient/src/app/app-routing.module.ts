import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AlumnosComponent } from './alumnos/alumnos.component';
import { MateriasComponent } from './materias/materias.component';
import { AsignacionesComponent } from './asignaciones/asignaciones.component';

const routes: Routes = [
  {
    path: '',
    component: AlumnosComponent
  },
  {
    path: 'materias',
    component: MateriasComponent
  },
  {
    path: 'notas',
    component: AsignacionesComponent
  }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
