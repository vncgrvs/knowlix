<template>
  <div class="">
    <landingpage />
  </div>
</template>

<script>
import landingpage from "../components/landingpage";

export default {
  components: {
    landingpage,
  },
  middleware: 'auth',
  computed: {},

  methods: {},

  data() {
    return {};
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
  async created() {},
};
</script>

<style>
</style>
