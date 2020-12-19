<template>
  <div class="w-full h-full sortable bg-gray-100">
    <div class="fixed w-full pt-5">
      <alertJob
        v-for="(task, id) in this.$store.state.tasksAlerts"
        :key="task.id"
        :pkey="id"
        :taskname="task"
      />
    </div>
    <Section />
  </div>
</template>

<script>
import Section from "../components/Section";
import alertJob from "../components/alertJob";


export default {
  components: {
    Section,
    alertJob,
  },
  computed: {},

  methods: {
    findTask: function(taskList, taskID){
      var index = taskList.findIndex(x => x.taskID === taskID)

      return index
    }
  },

  data() {
    return {};
  },
  mounted() {
    
    this.ws_success = new WebSocket('ws://localhost:3333/tasks') 
    console.log('connected to WS')
    
    this.ws_success.onmessage = function(event){
      var data = JSON.parse(event.data)
      var taskID = data.taskID
      var status = data.data.status
      var tList = this.$store.state.taskList
      

      var index = this.findTask(tList, taskID)

      var payload = {
        index: index,
        status: status
      }
        
      
      this.$store.dispatch('updateTask', payload)
      
      
    }.bind(this)
    
    
    
  },
  async created() {
    const res = await this.$axios.$get("/v1/sections").then((response) => {
      this.$store.commit("updateList", response.data);
    });
  },
};
</script>

<style>
</style>
