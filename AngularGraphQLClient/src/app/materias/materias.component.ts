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

@Component({
  selector: 'app-materias',
  templateUrl: './materias.component.html',
  styleUrls: ['./materias.component.css']
})
export class MateriasComponent implements OnInit {
  page = 1;
  materias: any[] = [];

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