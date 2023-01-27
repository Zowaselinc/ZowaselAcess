<template>
  <DefaultNav>
  <div class="left-content">
      <img
class="mobile-logo"
src="@/assets/images/logos/zowasel-logo.png"

alt=""
>       
<div class="welcome-text">
      <h1>Farmers</h1></div>
      <hr><br><br>
      <router-link
                :to="{ path: '/dashboard/farmer'}"
            ><button
  type="button"
  class="btn btn-success btn-sm"
  >
  Add Farmer
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
gender
</th>
            <th scope="col">
age
</th>
            <th scope="col">
              lands
</th>
            <th scope="col">
              farm size
</th>
            <th scope="col">
              years_cultivating
</th>
            <th scope="col">
crop
</th>
            <th scope="col">
              owner
</th>
            <th scope="col">
              multiple crops
</th>
            <th scope="col">
intercropping
</th>
            <th scope="col">
machines
</th>
            <th scope="col">
              monthly income
</th>
            <th scope="col">
              group
</th>
            <th scope="col">
              amount
</th>
              <th scope="col">
                  score
</th>
            <th scope="col">
              bin
</th>
            <th scope="col">
              date
</th>
            <th />
          </tr>
        </thead>
        <tbody>
          <tr
v-for="(farmer, index) in farmers"
:key="index"
>
            <td>{{ farmer.gender }}</td>
            <td>{{ farmer.age }}</td>
            <td>{{ farmer.number_of_land }}</td>
            <td>{{ farmer.size_of_farm }}</td>
            <td>{{ farmer.years_cultivating }}</td>
            <td>{{ farmer.crop }}</td>
            <td>{{ farmer.owner_caretaker }}</td>
            <td>{{ farmer.number_of_crops }}</td>
            <td>{{ farmer.intercropping }}</td>
            <td>{{ farmer.machines }}</td>
            <td>{{ farmer.estimate_monthly_income }}</td>
            <td>{{ farmer.is_in_a_cooperative }}</td>
            <td>{{ farmer.applyLoanAmount }}</td>
            <td>{{ farmer.score }}</td>
            <td>{{ farmer.bin }}</td>
            <td>{{ farmer.date_created }}</td>
            
            <td>
              <div
class="btn-group"
role="group"
>           
<router-link
                :to="{ name: 'Farmers', params: { id: farmer.id, farmerBvn: farmer } }"
            >
                <button
type="button"
class="btn btn-success btn-sm"
>
                  View Farmer
                </button></router-link>
<router-link
                :to="{ name: 'Transfer', params: { id: farmer.id, farmerBvn: farmer } }"
            >
                <button
type="button"
class="btn btn-warning btn-sm"
>
                  Offer Loan
                </button></router-link>

                <button
type="button"
class="btn btn-danger btn-sm"
@click="deleteTodo(todo.id)"
>
Delete Request
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
    axios.get(`${baseUrl}/scorecard/all`).then((response) => {
    this.farmers = response.data.farmers;
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
    axios.get(`${baseUrl}/scorecard/all`)
      .then((res) => {
          this.farmers = res.data.farmers;
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
                    //axios.delete(`${baseUrl}/scorecard/bvn=${todoId}`)
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