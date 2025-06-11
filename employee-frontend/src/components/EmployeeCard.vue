<template>
  <div class="employee-card">
    <div class="card-image">
      <img :src="getImageUrl(employee)" :alt="employee.name" />
    </div>

    <div class="card-content">
      <h3 class="employee-name">{{ employee.name }}</h3>
      <p class="employee-id">ID: {{ employee.employee_id }}</p>
      <p class="employee-age">Age: {{ employee.age }}</p>

      <button @click="handleEdit" class="edit-btn">
        <svg
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"
          ></path>
          <path
            d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"
          ></path>
        </svg>
        Edit
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "EmployeeCard",
  props: {
    employee: {
      type: Object,
      required: true,
    },
    index: {
      type: Number,
      default: 0,
    },
  },
  methods: {
    handleEdit() {
      this.$emit("edit", this.index);
    },
    getImageUrl(employee) {
      // Check if it's a Django media URL
      if (employee.photo && employee.photo.startsWith("/media/")) {
        return `http://localhost:8000${employee.photo}`;
      }
      // Otherwise use local media folder
      return employee.photo || "/media/employee1.jpg";
    },
  },
};
</script>

<style scoped>
.employee-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.employee-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.card-image {
  height: 200px;
  overflow: hidden;
  position: relative;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.employee-card:hover .card-image img {
  transform: scale(1.1);
}

.card-content {
  padding: 1.5rem;
  text-align: center;
}

.employee-name {
  font-size: 1.4rem;
  font-weight: bold;
  color: #333;
  margin: 0 0 0.5rem 0;
}

.employee-id,
.employee-age {
  color: #666;
  margin: 0.25rem 0;
  font-size: 0.95rem;
}

.edit-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  cursor: pointer;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 1rem;
  transition: all 0.3s ease;
}

.edit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.edit-btn svg {
  width: 16px;
  height: 16px;
}
</style>
