<template>
  <div class="w-full h-full sortable bg-gray-100">
    <div
      class="fixed z-0 w-5/12 pt-3 right-0"
      v-if="this.$store.state.taskAlerts.length != 0"
    >
      <alert
        v-for="(alert, id) in this.$store.state.taskAlerts"
        :key="id"
        :pkey="id"
        :alertID="alert.alertID"
        :alertType="alert.alertType"
        :alertColor="alert.alertColor"
      />
    </div>

    <div class="mx-auto pt-5 z-10 w-full h-auto">
      <div class="grid grid-cols-2 py-3 px-52">
        <p
          class="flex items-center justify-center text-lix-second col-span-2 font-lix font-semibold text-6xl tracking-normal mb-4"
        >
          Slidedeck Manager
        </p>

        <div class="flex items-center justify-end col-span-1 mr-4">
          <div class="flex justify-center font-lix">
            <span class="">
              <button
                type="button"
                class="inline-flex items-center px-4 py-2 border-2 border-gray-300 rounded-md shadow-md text-sm font-medium bg-white text-lix-second"
                :class="{
                  'cursor-not-allowed': this.$store.state.isFetchingPptx,
                  'hover:bg-lix-main': !this.$store.state.isFetchingPptx,
                  'hover:text-white': !this.$store.state.isFetchingPptx,
                }"
                :disabled="this.$store.state.isFetchingPptx"
                @click="downloadPptx"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  class="h-5 w-5 -mt-0 mr-2"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
                  />
                </svg>
                <p
                  class="cursor-pointer"
                  :class="{
                    hidden: this.$store.state.isFetchingPptx,
                    'cursor-pointer': !this.$store.state.isFetchingPptx,
                  }"
                >
                  Create Slides
                </p>
                <p :class="{ hidden: !this.$store.state.isFetchingPptx }">
                  Building pptx ...
                </p>
              </button>
            </span>
          </div>
        </div>
        <div class="flex items-center justify-start col-span-1 ml-4">
          <nuxt-link to="/onboarding/downloads">
            <div class="flex justify-end font-lix">
              <span class="">
                <button
                  type="button"
                  class="inline-flex items-center px-4 py-2 border-2 border-gray-300 rounded-md shadow-md text-sm font-medium bg-white text-lix-second"
                  :class="{
                    'cursor-not-allowed': this.$store.state.isFetchingPptx,
                    'hover:bg-lix-main': !this.$store.state.isFetchingPptx,
                    'hover:text-white': !this.$store.state.isFetchingPptx,
                  }"
                  :disabled="this.$store.state.isFetchingPptx"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    class="h-5 w-5 -mt-0 mr-2"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"
                    />
                  </svg>
                  <p
                    class="cursor-pointer"
                    :class="{
                      hidden: this.$store.state.isFetchingPptx,
                      'cursor-pointer': !this.$store.state.isFetchingPptx,
                    }"
                  >
                    Downloads
                  </p>
                  <p :class="{ hidden: !this.$store.state.isFetchingPptx }">
                    Building pptx ...
                  </p>
                </button>
              </span>
            </div>
          </nuxt-link>
        </div>
      </div>
    </div>

    <Section />
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
  middleware: 'auth',
  methods: {
    downloadPptx() {
      this.$store.commit("changeDownloadStatus");
      this.$store.dispatch("sendTask");
    },
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