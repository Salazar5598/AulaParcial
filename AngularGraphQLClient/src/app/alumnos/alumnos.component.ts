import { Component, OnInit } from '@angular/core';
import { Apollo, QueryRef } from 'apollo-angular';
import gql from 'graphql-tag';


const LISTARALUMNOS_QUERY = gql`
query {
  alumnos {
    	Codigo
      Nombre
      Apellido
      Email
      Grado
      Seccion
      Genero
      nacimiento
      direccion
    }
  }
`;

const CREARALUMNOS_QUERY = gql`
mutation createAlumno(
  $Codigo: String,
  $Nombre: String,
  $Apellido: String,
  $Email: String,
  $Grado: String,
  $Seccion: String,
  $Genero: String,
  $nacimiento: String,
  $direccion: String
) {
  createAlumno(input: {
      Codigo:$Codigo,
      Nombre:$Nombre,
      Apellido:$Apellido,
      Email:$Email,
      Grado: $Grado,
      Seccion:$Seccion,
      Genero:$Genero,
      nacimiento:$nacimiento,
      direccion:$direccion,
  }) {
    ok
  }
}

`;

@Component({
  selector: 'app-alumnos',
  templateUrl: './alumnos.component.html',
  styleUrls: ['./alumnos.component.css']
})
export class AlumnosComponent implements OnInit {
  page = 1;
  alumnos: any[] = [];
  alumno = {
    Codigo:"",
    Nombre:"",
    Apellido:"",
    Email:"",
    Grado:"",
    Seccion:"",
    Genero:"",
    nacimiento:"",
    direccion:"",

  };
  private query: QueryRef<any>;

  constructor(private apollo: Apollo) {}

  ngOnInit() {
    this.query = this.apollo.watchQuery({
      query: LISTARALUMNOS_QUERY
      
    });

    this.query.valueChanges.subscribe(result => {
      console.log(result)
      this.alumnos = result.data && result.data.alumnos;
    });
  }
  
  newPost() {
    this.apollo.mutate({
      mutation: CREARALUMNOS_QUERY,
      variables: {
        Codigo: this.alumno.Codigo,
        Nombre: this.alumno.Nombre,
        Apellido: this.alumno.Apellido,
        Email:this.alumno.Email,
        Grado: this.alumno.Grado,
        Seccion:this.alumno.Seccion,
        Genero:this.alumno.Genero,
        nacimiento:this.alumno.nacimiento,
        direccion:this.alumno.direccion,
      }
    }).subscribe(data => {
      console.log('New post created!', data);
    });
  }
  update() {
    this.query.refetch();
  }

  nextPage() {
    this.page++;
    this.update();
  }

  prevPage() {
    if (this.page > 0) this.page--;
    this.update();
  }
}