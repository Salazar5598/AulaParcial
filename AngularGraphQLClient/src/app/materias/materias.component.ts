import { Component, OnInit } from '@angular/core';
import { Apollo, QueryRef } from 'apollo-angular';
import gql from 'graphql-tag';

const LISTARMATERIAS_QUERY = gql`
query {
  materias {
    NombreMateria
    FechaIngreso
    }
  }
`;
const CREARMATERIAS_QUERY = gql`
mutation createMateria(
  $NombreMateria: String,
) {
  createMateria(input: {
    NombreMateria:$NombreMateria,
  }) {
    ok
  }
}

`;

@Component({
  selector: 'app-materias',
  templateUrl: './materias.component.html',
  styleUrls: ['./materias.component.css']
})
export class MateriasComponent implements OnInit {
  page = 1;
  materias: any[] = [];
  materia = {
    NombreMateria:"",

  };
  private query: QueryRef<any>;

  constructor(private apollo: Apollo) {}

  ngOnInit() {
    this.query = this.apollo.watchQuery({
      query: LISTARMATERIAS_QUERY
    });

    this.query.valueChanges.subscribe(result => {
      this.materias = result.data && result.data.materias;
    });
  }

  newPost() {
    this.apollo.mutate({
      mutation: CREARMATERIAS_QUERY,
      variables: {
        NombreMateria: this.materia.NombreMateria,
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