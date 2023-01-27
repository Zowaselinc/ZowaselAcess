<template>
    <AuthSharedLayout>
    <div class="big-container">
        <img
class="mobile-logo"
src="@/assets/images/logos/zowasel-logo.png"

alt=""
>       <div class="left-content">
        
  <div class="container">

    <div class="row">
      <div class="col-sm-10">
        <h1>Farmers</h1>
        <hr><br><br>
        <button
type="button"
class="btn btn-success btn-sm"
>
Add Farmer
</button>
        <br><br>
        <table
id="datatable"
class="table table-hover"
>
          <thead>
            <tr>
              <th scope="col">
firstname
</th>
              <th scope="col">
surname
</th>
              <th scope="col">
firstname
</th>
              <th scope="col">
surname
</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr
v-for="(farmer, index) in farmers"
:key="index"
>
              <td>{{ farmer.firstname }}</td>
              <td>{{ farmer.surname }}</td>
              <td>{{ farmer.firstname }}</td>
              <td>{{ farmer.surname }}</td>
              
              <td>
                <div
class="btn-group"
role="group"
>           
                  <button
type="button"
class="btn btn-warning btn-sm"
@click="editTodo(todo.id)"
>
Update
</button>
                  <button
type="button"
class="btn btn-danger btn-sm"
@click="deleteTodo(todo.id)"
>
Delete
</button>
                  <a
href="/farmer"
target="_blank"
style="color:black"
>
                  <button
type="button"
class="btn btn-warning btn-sm"
>
                    View
                  </button></a>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>



      
        
        </div>      
    </div>
    </AuthSharedLayout>
</template>

<script>
import "jquery/dist/jquery.min.js";
import "bootstrap/dist/css/bootstrap.min.css";
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import $ from "jquery";
import {baseUrl} from "@/pages/dashboard/tables/constants.js";
import AuthSharedLayout from "@/layouts/shared/AuthSharedLayout.vue";
import axios from 'axios';
export default {
    
    name: "Example",
    components : {
        AuthSharedLayout
    },
    data(){
        return {
      farmers: [],
    };
    },
    mounted() {
      axios.get(`${baseUrl}/farmer/all`).then((response) => {
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
      axios.get(`${baseUrl}/farmer/all`)
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
    async editTodo(todoId) {
                // Push to the edit todo page
                this.$router.push({
                    path: `/edit-todo/${todoId}`,
                });
                return;
            },
    // deleting a todo
    async deleteTodo(todoId) {
                // confirm with the user
                let confirmation = confirm("Do you want to delete this todo?");

                if (confirmation) {
                    try {
                        await this.$http.delete(`http://localhost:5000/api/todo/${todoId}`);
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