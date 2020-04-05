<template>
  <v-app>
    <v-app-bar color="primary" dark app class='title'>
      <v-toolbar-title>Hmcomm Data Science Competition #1</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn x-large color="success" >Submmit</v-btn>
    </v-app-bar>
    <v-content>
      <v-container>
        <v-list-item-title class="title grey--text text--darken-2" align='center' style='margin-top: 30px'>
          Leaderboard
        </v-list-item-title>
        <v-data-table
          :headers="headers" 
          :items="desserts" 
          :items-per-page="5" 
          :sort-by.sync='sortBy' 
          :sort-desc.sync='sortDesc' 
          class="elevation-1 category-table"
          style="margin-left: 300px; margin-right: 300px; margin-top: 50px" >
        </v-data-table>
      </v-container>
    </v-content>
  </v-app>
</template>
<script>
  export default {
    data () {
      return {
        sortBy: 'rank',
        sortDesc: false,
        headers: [
          {
            text: '#',
            align: 'center',
            sortable: false,
            value: 'rank',
          },
          { text: 'Name', value: 'name'},
          { text: 'Score', value: 'score'},
          { text: 'N_Submission', value: 'n_submission' },
          { text: 'Date', value: 'date' },
        ],
        desserts: [
          {
            rank: 1,
            name: 'A',
            score: 159,
            n_submission: 6.0,
            date: 24,
          },
          {
            rank: 2,
            name: 'B',
            score: 237,
            n_submission: 9.0,
            date: 37,
          },
          {
            rank: 3,
            name: 'C',
            score: 262,
            n_submission: 16.0,
            date: 23,
          },
          {
            rank: 4,
            name: 'D',
            score: 505,
            n_submission: 3.7,
            date: 67,
          },
          {
            rank: 5,
            name: 'E',
            score: 356,
            n_submission: 16.0,
            date: 49,
          },
        ],
      }
    },
  }
</script>
