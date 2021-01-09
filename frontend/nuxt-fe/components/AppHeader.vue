<template >
  <header
    class="font-lix overflow-hidden"
    tabindex="0"
    @keydown.esc="toggleDropdownOff"
  >
    <nav
      class="bg-lix-main z-50 items-center justify-center shadow-lg grid grid-cols-5"
    >
      <div class="col-span-3 my-10 pl-5">
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

      <!-- Solutions  -->
      <div
        class="flex flex-row justify-center items-center z-10 py-3 outline-none col-span-1"
        tabindex="0"
        @keydown.esc="toggleDropdownOff"
        @click="changeDropdownVis"
        @mouseover="toggleDropdownOn"
        @mouseleave="toggleDropdownOff"
        v-if="this.$store.state.auth.loggedIn"
      >
        <div class="flex z-50 justify-center font-semibold text-gray-100">
          <p
            class="cursor-pointer border-2 border-transparent px-2 py-1 rounded-full hover:border-white"
          >
            Solutions
          </p>
        </div>

        <transition name="solutions">
          <div
            tabindex="0"
            class="fixed top-16 pt-4 w-4/12 h-auto flex flex-col justify-center items-center"
            v-show="this.$store.state.isDropdownVisible"
            @mouseover="toggleDropdownOn"
            @mouseleave="toggleDropdownOff"
            @keydown.esc="toggleDropdownOff"
          >
            <div class="h-6 w-8 -mb-3 shadow-md">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                class="text-white"
                stroke="currentColor"
                fill="currentColor"
                viewBox="0 0 30 18"
              >
                <path
                  d="M30,22,16,6,2,22Z"
                  transform="translate(-1 -5)"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                />
              </svg>
            </div>

            <div
              class="bg-white w-full h-full shadow-md rounded-sm inline-flex"
            >
              <div class="py-4 px-3 w-full">
                <nuxt-link to="/">
                  <div
                    class="flex flex-row pt-3 pb-3 hover:bg-gray-100 rounded-sm"
                  >
                    <div class="flex justify-start px-4">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        class="h-6 w-6 text-lix"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2"
                        />
                      </svg>
                    </div>
                    <div class="flex flex-col">
                      <p class="text-gray-700">Basic Onboarding</p>
                      <p class="text-xs text-gray-600 font-light leading-5">
                        Use the 4-week sprint methodology as your onboarding
                        guide and select the sprint slides you need.
                      </p>
                    </div>
                  </div>
                </nuxt-link>

                <nuxt-link to="/onboarding/modular">
                  <div
                    class="flex flex-row pt-3 pb-3 mb-4 hover:bg-gray-100 rounded-sm"
                  >
                    <div class="flex justify-start px-4">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        class="text-lix h-6 w-6"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"
                        />
                      </svg>
                    </div>
                    <div class="flex flex-col">
                      <p class="text-gray-700">Modular Onboarding</p>
                      <p class="text-xs text-gray-600 font-light leading-5">
                        Quickly assemble your onboarding deck to fit your
                        customer's needs.
                      </p>
                    </div>
                  </div>
                </nuxt-link>

                <nuxt-link to="/onboarding/downloads">
                  <div
                    class="flex flex-row pt-3 pb-3 mb-4 hover:bg-gray-100 rounded-sm"
                  >
                    <div class="flex justify-start px-4">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        class="text-lix h-6 w-6"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10"
                        />
                      </svg>
                    </div>
                    <div class="flex flex-col">
                      <p class="text-gray-700">Downloads</p>
                      <p class="text-xs text-gray-600 font-light leading-5">
                        Download your final Onboarding Slidedeck.
                      </p>
                    </div>
                  </div>
                </nuxt-link>
              </div>
            </div>
          </div>
        </transition>
      </div>

      <!-- Logout -->
      <div class="flex flex-row justify-center items-center py-3">
        <div
          class="text-gray-100 flex font-semibold border-2 border-transparent px-2 py-1 rounded-full hover:bg-gray-100 hover:text-lix cursor-pointer"
          @click="logUserOut"
          v-if="this.$store.state.auth.loggedIn"
        >
          Logout
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
    toggleDropdownOn() {
      this.$store.commit("toggleDropdownOn");
    },
    toggleDropdownOff() {
      this.$store.commit("toggleDropdownOff");
    },
    changeDropdownVis() {
      this.$store.commit("changeDropdownVis");
    },
    logUserOut() {
      this.$store.dispatch("auth/logUserOut");
    },
  },
  created() {},

  watch: {
    $route(to, from) {
      this.$store.commit("changeCurrentRoute", to.name);

      this.$store.commit("toggleDropdownOff");
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
.solutions-enter-active {
  animation: fadeIn;
  animation-duration: 0.3s ;
}
.solutions-leave-active{
  animation: fadeOut;
  animation-duration: 0.5s ;
}

</style>