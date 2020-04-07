<template>
  <v-app>
    <v-app-bar color="primary" dark app class='title'>
      <v-toolbar-title>Data Science Competition #1</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn x-large color="success"  @click='getRankingTable'>Submit</v-btn>
    </v-app-bar>
    <v-content>
      <v-container>
        <v-list-item-title class="title grey--text text--darken-2" align='center' style='margin-top: 30px'>
          Leaderboard {{msg}}
        </v-list-item-title>
        <v-file-input @change='to_api' label='submission' accept='.csv' ></v-file-input>
        <v-data-table
          :headers="headers" 
          :items="participants" 
          :items-per-page="10" 
          class="elevation-1 category-table"
          style="margin-left: 100px; margin-right: 100px; margin-top: 50px" >
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
        msg: '',
        hello: '',
        csvData: '',
        rankingTable: '',
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
      async to_api(file){
        console.log('---- in vue ----')
        try {
          const csv = await this.readFileAsync(file)
          this.csvData = csv
        } catch (e) {
          console.log(e)
        }
        // POST
        axios.post('http://127.0.0.1:5003/get_score', {
          arg01: this.csvData
        })
        .then((response) => {
          this.msg = response.data.score
        })
        console.log('---- out vue ----')
      },
      getRankingTable(){
        console.log('func-↓rankingTable')
        // POST
        axios.post('http://127.0.0.1:5003/get_ranking_table', {
        })
        .then((response) => {
          this.rankingTable = response.data.ranking_table
        })
        console.log(this.rankingTable)
        // console.log(this.rankingTable)
        this.rankingUpdate()
      },
      rankingUpdate() {
        console.log('func-↓rankingUpdate')
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
        });
        this.participants = participants;
      }
    }
  }
</script>