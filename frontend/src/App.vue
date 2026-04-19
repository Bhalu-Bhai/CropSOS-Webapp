<template>
  <div id="app">
    <nav class="navbar-home">
      <div class="nav-main">
        <div class="nav-logo">CropSOS</div>
        <ul class="home-nav-links">
          <li :class="{ bottomLine: activeTap === 'home' }">
            <router-link to="/" @click.native="activeTap = 'home'">Home</router-link>
          </li>
          <li :class="{ bottomLine: activeTap === 'detect' }">
            <router-link to="/detect" @click.native="activeTap = 'detect'">Detect</router-link>
          </li>
          <li :class="{ bottomLine: activeTap === 'history' }">
            <router-link to="/history" @click.native="activeTap = 'history'">History</router-link>
          </li>
        </ul>
        <div class="nav-icons">
          <span class="material-symbols-outlined"><router-link to="/notifications" @click.native="activeTap = 'notifications'">notifications</router-link></span>
          <span class="material-symbols-outlined"><router-link to="/account" @click.native="activeTap = 'account'">account_circle</router-link></span>
        </div>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>


export default {
  data() {
    return {
      activeTap: 'home'
    }
  }
}
</script>
<style>
@import "./assets/HomeView.css";
</style>
