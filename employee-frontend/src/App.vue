<template>
  <div id="app">
    <header class="header">
      <h1>Employee Management System</h1>
    </header>

    <main class="main-content">
      <EmployeeList />
    </main>
  </div>
</template>

<script>
import EmployeeList from "./components/EmployeeList.vue";

export default {
  name: "App",
  components: {
    EmployeeList,
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Arial", sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  padding-top: 2rem;
}

.header {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 2rem 2rem;
  text-align: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
}

.header h1 {
  color: white;
  font-size: 2.5rem;
  font-weight: 300;
  letter-spacing: 2px;
}

.main-content {
  flex: 1;
  padding-top: 2rem;
}
</style>

