<template>
  <div class="w-full h-full sortable bg-gray-100">
    <div class="fixed w-full pt-5">
      <alert
        v-for="(alert, id) in this.$store.state.taskAlerts"
        :key="id"
        :pkey="id"
        :alertID="alert.alertID"
        :alertType="alert.alertType"
      />
    </div>
    <div class="mx-auto w-10/12 h-auto mt-2">
      <div class=" py-3 px-10 flex justify-around rounded-">
        <p class="text-gray-900 font-lix font-light text-6xl tracking-wide">
          Slidedeck
        </p>
        <span class="flex items-center ">
          <button
            type="button"
            class="inline-flex  items-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            <!-- Heroicon name: pencil -->
            <svg
              class="-ml-1 mr-2 h-5 w-5 text-gray-500 "
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              aria-hidden="true"
            >
              <path
                d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"
              />
            </svg>
            Edit
          </button>
        </span>
      </div>
      <Section />
    </div>
  </div>
</template>

<script>
import Section from "../../components/Section";
import alert from "../../components/alert";

export default {
  components: {
    Section,
    alert,
  },
  async created() {
    this.$store.dispatch("getSections");
    this.$store.dispatch("getDownloads");
  },
  mounted() {
    this.ws_success = new WebSocket("ws://localhost:3333/tasks");

    this.ws_success.onmessage = function (event) {
      var data = JSON.parse(event.data);

      var operationType = data.operation;

      if (
        operationType == "insert" ||
        operationType == "replace" ||
        operationType == "delete"
      ) {
        this.$store.dispatch("getDownloads");
      }
    }.bind(this);
  },
};
</script>

<style>
</style>