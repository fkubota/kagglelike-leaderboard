<template>
  <v-app>
    <v-app-bar color="primary" dark app class='title'>
      <v-toolbar-title>Data Science Competition #1</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn x-large icon dark @click='getRankingTable'>
        <v-icon dark>mdi-cached</v-icon>
      </v-btn>
    </v-app-bar>
    <v-content>
      <v-container>
        <v-row>
          <v-col>
            <v-select v-model="selection_name" :items='names' label='select your name'> </v-select>
          </v-col>
          <v-col>
            <v-file-input @change='fileSelect' show-size label='selec your submission file' accept='.csv' ></v-file-input>
          </v-col>
        </v-row>
        <v-row justify='end'>
            <v-btn x-large color='primary' @click='getScore' outlined target='#de'>submit</v-btn>
        </v-row>
        <v-list-item-title class="title grey--text text--darken-2" align='center' style='margin-top: 30px'>
          your submission score is <h2><font color='blue'>{{score}}</font></h2>
        </v-list-item-title>
        <v-divider></v-divider>
        <v-list-item-title class="title grey--text text--darken-2" align='center' style='margin-top: 30px'>
          Leaderboard
        </v-list-item-title>
        <v-data-table
          :headers="headers" 
          :items="participants" 
          :items-per-page="10" 
          class="elevation-1 category-table"
          style="margin-left: 100px; margin-right: 100px;" >
          <template slot="items" slot-scope="props">
            <td class="text-xs-right">{{ props.item.code }}</td>
            <td class="text-xs-right">{{ props.item.name }}</td>
            <td class="text-xs-right">{{ props.item.workerType }}</td>
          </template>
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
        score: '...',
        hello: '',
        subData: '',
        rankingTable: '',
        sortBy: 'rank',
        sortDesc: false,
        selection_name: '',
        names: ['A', 'B', 'C'],
        dropdown_font: ['Arial', 'Calibri', 'Courier', 'Verdana'],
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
        ],
        participants: [
          {
            rank: 1,
            name: 'A',
            score: 159,
            n_submission: 6.0,
          },
          {
            rank: 2,
            name: 'B',
            score: 237,
            n_submission: 9.0,
          },
          {
            rank: 3,
            name: 'C',
            score: 262,
            n_submission: 16.0,
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
      async fileSelect(file){
        console.log('func-↓fileSelect')
        try {
          const csv = await this.readFileAsync(file)
          this.subData = csv
        } catch (e) {
          console.log(e)
        }
      },
      async getScore(){
        console.log('func-↓getScore')
        // POST
        await axios.post('http://127.0.0.1:5003/get_score', {
          arg_subData: this.subData,
          arg_selection_name: this.selection_name,
        })
        .then((response) => {
          this.score = response.data.score
          this.getRankingTable()
        })
      },
      async getRankingTable(){
        console.log('func-↓getRankingTable')
        // POST
        await axios.post('http://127.0.0.1:5003/get_ranking_table', {
        })
        .then((response) => {
          this.rankingTable = response.data.ranking_table
        })
        console.log(this.rankingTable)
        this.updateRankingTable()
      },
      updateRankingTable() {
        console.log('func-↓updateRankingTable')
        const participants = [];
        const lines = this.rankingTable.split("\n");
        lines.forEach(element => {
          const participantsData = element.split(",");
          const participant = {
            rank: participantsData[0],
            name: participantsData[1],
            score: participantsData[2],
            n_submission: participantsData[3]
          };
          participants.push(participant);
        this.participants = participants
        });
      },
    },
    // mounted () {
    created () {
      console.log('func-↓mounted')
      console.log(this.participants)
      this.getRankingTable()
    }
  }
</script>
