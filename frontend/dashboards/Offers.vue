<template>
    <DefaultNav>
    <div class="left-content">
        <img
  class="mobile-logo"
  src="@/assets/images/logos/zowasel-logo.png"
  
  alt=""
  >       
  <div class="welcome-text">
        <h1>Offers</h1></div>
        <hr><br><br>
        <router-link
                :to="{ path: '/dashboard/scorecard'}"
            ><button
  type="button"
  class="btn btn-success btn-sm"
  >
  Add Offer
  </button></router-link>
          <br><br>
        <div
  class="table-responsive"
  width="100%"
  >
        <table
  id="datatable"
  class="table table-hover"
  cellspacing="0"
  >
          <thead>
            <tr>
              <th scope="col">
                id
  </th>   
        <th scope="col">
                bvn
  </th>
        <th scope="col">
                score
  </th>
              <th scope="col">
                bin
  </th>
              <th scope="col">
                type
  </th>
              <th scope="col">
                company
  </th>
              <th scope="col">
                amount
  </th>
              
              <th scope="col">
                repayment_amount
  </th>
              <th scope="col">
                status
  </th>

              <th scope="col">
                repayment_months
  </th>
              <th scope="col">
              due_date
  </th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr
  v-for="(farmer, index) in farmers"
  :key="index"
  >
              <td>{{ farmer.id }}</td>
              <td>{{ farmer.bvn }}</td>
              <td>{{ farmer.scpre }}</td>
              <td>{{ farmer.bin }}</td>
              <td>{{ farmer.type }}</td>
              <td>{{ farmer.company }}</td>
              <td>{{ farmer.amount }}</td>
              <td>{{ farmer.repayment_amount }}</td>
              <td>{{ farmer.status }}</td>
              <td>{{ farmer.repayment_months }}</td>
              <td>{{ farmer.due_date }}</td>
      
              
              <td>
                <div
  class="btn-group"
  role="group"
  >           
  
                <button
  type="button"
  class="btn btn-success btn-sm"
  @click="editTodo(todo.id)"
  >
                    Accept Loan
                  </button>
  
  
                 <button
  type="button"
  class="btn btn-danger btn-sm"
  @click="deleteTodo(todo.id)"
  >
  Reject Loan
  </button>
                  
                </div>
              </td>
            </tr>
          </tbody>
        </table>
    </div>
  </div>
  
  </DefaultNav>
  </template>
  
  <script>
  import "jquery/dist/jquery.min.js";
  import "bootstrap/dist/css/bootstrap.min.css";
  import "datatables.net-dt/js/dataTables.dataTables";
  import "datatables.net-dt/css/jquery.dataTables.min.css";
  import $ from "jquery";
  import {baseUrl} from "@/pages/dashboard/tables/constants.js";
  import DefaultNav from "@/layouts/DefaultNav.vue";
  import axios from 'axios';
  export default {
    
    name: "Scorecard",
    components : {
      DefaultNav,
      
  },
    data(){
        return {
      farmers: [],
    };
    },
    mounted() {
      axios.get(`${baseUrl}/transfer/status=Pending`).then((response) => {
      this.farmers = response.data.transfers;
      $("#datatable").DataTable();
    })
    .catch((error) => {
          console.error(error);
        });
    },
  
  // Fetch the todos on load
  created() {
    this.getFarmers();
    },
    methods: {
        getFarmers() {
      axios.get(`${baseUrl}/transfer/status=Pending`)
        .then((res) => {
            this.farmers = res.data.transfers;
        //    $("#datatable").DataTable();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  
    // editing a todo
    editTodo(todoId) {
                // Push to the edit todo page
                //farmer = Farmer.query.get_or_404(name)
                this.$router.push({
                    path: `/dashboard/transfer`,
                    //path: `/edit-todo/${todoId}`,
                    //farmer=res.data
                });
                return;
            },
    // deleting a todo
    deleteTodo(todoId) {
                // confirm with the user
                let confirmation = confirm("Do you want to delete this todo?");
  
                if (confirmation) {
                    try {
                      //axios.delete(`${baseUrl}/scorehistory/bvn=${todoId}`)
                         //this.$http.delete(`http://localhost:5000/api/todo/${todoId}`);
                        // refresh the todos
                        this.getData();
                    } catch (error) {
                        console.log(error);
                    }
                }
            },
  }
  }
  </script>
  
  <style lang="scss" scoped>
  @import "@/assets/scss/main.scss";
  </style>