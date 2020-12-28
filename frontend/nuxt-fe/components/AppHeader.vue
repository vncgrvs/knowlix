<template >
  <header class="font-lix">
    <nav
      class="bg-lix-main flex items-center flex-wrap justify-around p-6 shadow-lg"
    >
      <div class="w-2/12">
        <nuxt-link to="/">
          <svg
            width="139"
            height="33"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
          >
            <defs>
              <circle id="a" cx="14" cy="14" r="14" />
              <filter
                x="-31.3%"
                y="-31.3%"
                width="162.5%"
                height="162.5%"
                filterUnits="objectBoundingBox"
                id="b"
              >
                <feGaussianBlur stdDeviation="3" in="SourceGraphic" />
              </filter>
            </defs>
            <g fill="none" fill-rule="evenodd">
              <path
                d="M56.61 25V7.855h3.85v13.48h8.538V25H56.61zm26.54-6.658c0 .51-.046 1.02-.116 1.53h-9.35c.395 1.393 1.486 2.39 3.458 2.39 1.368 0 2.946-.533 3.967-1.23l1.438 2.483c-1.23.928-3.201 1.763-5.568 1.763-4.756 0-6.96-3.201-6.96-6.658 0-3.782 2.668-6.658 6.705-6.658 3.642 0 6.426 2.343 6.426 6.38zm-6.426-3.434c-1.485 0-2.645.882-3.062 2.366h5.985c-.325-1.438-1.392-2.366-2.923-2.366zm18.12-2.622h3.433V25h-3.434v-1.3c-.928.929-2.18 1.625-3.92 1.625-3.666 0-6.265-2.97-6.265-6.751 0-3.805 2.668-6.612 6.264-6.612 1.717 0 2.993.719 3.921 1.67v-1.346zm-3.295 9.721c1.925 0 3.294-1.554 3.294-3.387 0-1.81-1.369-3.34-3.294-3.34-1.926 0-3.248 1.53-3.248 3.34 0 1.856 1.345 3.387 3.248 3.387zM101.084 25V12.286h3.55v1.764c.626-1.137 2.088-2.112 4.013-2.112 2.529 0 4.942 1.694 4.942 5.29V25h-3.643v-6.82c0-1.88-.997-2.9-2.482-2.9-1.624 0-2.738 1.206-2.738 2.992V25h-3.642zm15.544-17.145h3.851V25h-3.851V7.855zM122.358 25l5.406-8.654-5.011-8.49h4.431l3.062 5.59 3.248-5.59h4.478l-5.313 8.49L137.926 25h-4.432l-3.294-5.754L126.836 25h-4.478z"
                fill="#FFF"
                fill-rule="nonzero"
              />
              <g transform="translate(14.4 2.8)">
                <mask id="c" fill="#fff"><use xlink:href="#a" /></mask>
                <use fill="#FFF" opacity=".6" xlink:href="#a" />
                <path
                  fill-opacity=".55"
                  fill="#166BFF"
                  filter="url(#b)"
                  mask="url(#c)"
                  d="M-9.8 16.8L4.6 2.4 19 16.8 4.6 31.2z"
                />
              </g>
              <path
                fill="#FFF"
                opacity=".6"
                d="M0 16.8L14.4 2.4l14.4 14.4-14.4 14.4z"
              />
              <path
                d="M18.703 26.897A13.96 13.96 0 0 1 14.4 16.8c0-3.968 1.65-7.55 4.303-10.097L28.8 16.8 18.703 26.897z"
                fill="#FFF"
              />
            </g>
          </svg>
        </nuxt-link>
      </div>

      <p
        class="text-3xl text-gray-100 antialiased font-bold pt-1 flex justify-center w-5/12"
      >
        
      </p>

      <div class="flex w-2/12 justify-center items-center py-3">
        <nuxt-link to="/downloads">
          <p class="text-gray-100 flex font-semibold items-center">Downloads</p>
        </nuxt-link>
      </div>

      <div class="flex justify-end">
        <div
          class="flex items-center w-full justify-center rounded-full py-3 px-6 bg-gray-100 text-black shadow-xl font-bold mr-8 cursor-pointer ml-20"
          @click="downloadPptx"
          v-if="this.$store.state.currentRoute != 'downloads'"
          :class="{
            'cursor-not-allowed': this.$store.state.isFetchingPptx,
            'hover:bg-lix-second': !this.$store.state.isFetchingPptx,
            'hover:text-gray-200': !this.$store.state.isFetchingPptx,
          }"
          :disabled="this.$store.state.isFetchingPptx"
          id="downloadButton"
        >
          <svg
            class="-ml-1 mr-3 h-5 w-5"
            :class="{
              'animate-spin': this.$store.state.isFetchingPptx,
              hidden: !this.$store.state.isFetchingPptx,
            }"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              class="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="4"
            ></circle>
            <path
              class="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            ></path>
          </svg>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            class="h-8 w-8 mr-2"
            :class="{ hidden: this.$store.state.isFetchingPptx }"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M8 13v-1m4 1v-3m4 3V8M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"
            />
          </svg>
          <p :class="{ hidden: this.$store.state.isFetchingPptx }">
            Create Slides
          </p>
          <p :class="{ hidden: !this.$store.state.isFetchingPptx }">
            Building pptx ...
          </p>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "AppHeader",

  data() {
    return {};
  },

  methods: {
    downloadPptx() {
      this.$store.commit("changeDownloadStatus");
      this.$store.dispatch("sendTask");
    },
  },
  created() {
    
  },
  watch: {
    $route(to, from) {
      this.$store.commit("changeCurrentRoute", to.name);

      if (to.name == "downloads") {
        this.$store.dispatch("clearAlertList");
      }
    },
  },
};
</script>

<style>
fontLIX {
  font-family: "Axiforma", sans-serif;
}
</style>