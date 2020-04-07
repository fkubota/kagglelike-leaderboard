<template>
  <v-app>
    <v-app-bar color="primary" dark app class='title'>
      <v-toolbar-title>Hmcomm Data Science Competition #1</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn x-large color="success" >Submit</v-btn>
    </v-app-bar>
    <v-content>
      <v-container>
        <v-list-item-title class="title grey--text text--darken-2" align='center' style='margin-top: 30px'>
          Leaderboard {{msg}}
        </v-list-item-title>
        <v-file-input @change='to_api' label='submission' accept='.csv' ></v-file-input>
        <v-data-table
          :headers="headers" 
          :items="desserts" 
          :items-per-page="5" 
          :sort-by.sync='sortBy' 
          :sort-desc.sync='sortDesc' 
          class="elevation-1 category-table"
          style="margin-left: 100px; margin-right: 100px; margin-top: 50px" >
        </v-data-table>
      </v-container>
    </v-content>
  </v-app>
</template>
<script>
import axios from 'axios'
  export default {
    data () {
      return {
        msg: '',
        csvData: '',
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
        ],
      }
    },
    methods: {
      readFileAsync (file) {
        return new Promise((resolve, reject) => {
          const reader = new FileReader()
          reader.onload = () => {
            resolve(reader.result)
          }
          reader.onerror = reject
          reader.readAsText(file)
        })
      },
      async to_api(file){
        console.log('---- in vue ----')
        try {
          const csv = await this.readFileAsync(file)
          this.csvData = csv
        } catch (e) {
          console.log(e)
        }

        // POST
        axios.post('http://127.0.0.1:5003/myapi', {
          arg01: this.csvData
        })
        .then((response) => {
          this.msg = response.data.score
        })
        console.log('---- out vue ----')
      }
    }
  }
</script>
