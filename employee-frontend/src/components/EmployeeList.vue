<template>
  <div class="employee-list">
    <!-- Employee Cards Grid -->
    <div class="cards-container">
      <div class="pagination-info">
        <h2>Employees (Page {{ currentPage }} of {{ totalPages }})</h2>
        <p>
          Showing
          {{ Math.min(currentPage * cardsPerPage, employees.length) }} of
          {{ employees.length }} employees
        </p>
      </div>

      <div class="cards-grid">
        <EmployeeCard
          v-for="(employee, index) in paginatedEmployees"
          :key="employee.id"
          :employee="employee"
          :index="index"
          @edit="openEditModal"
        />
      </div>

      <!-- Pagination Controls -->
      <div class="pagination" v-if="totalPages > 1">
        <button
          @click="prevPage"
          :disabled="currentPage === 1"
          class="pagination-btn"
        >
          Previous
        </button>
        <span class="page-info"
          >Page {{ currentPage }} of {{ totalPages }}</span
        >
        <button
          @click="nextPage"
          :disabled="currentPage === totalPages"
          class="pagination-btn"
        >
          Next
        </button>
      </div>
    </div>

    <!-- Bar Chart -->
    <div class="chart-container">
      <h2>📊 Employee Name vs Age Distribution</h2>
      <p class="chart-description">
        Interactive bar chart showing all employees and their ages
      </p>
      <BarChart :employees="employees" />
    </div>

    <!-- Edit Modal -->
    <div v-if="showEditModal" class="modal-overlay" @click="closeEditModal">
      <div class="modal" @click.stop>
        <div class="modal-header">
          <h3>Select Employee</h3>
          <button @click="closeEditModal" class="close-btn">&times;</button>
        </div>

        <div class="modal-body">
          <div class="employee-list-modal">
            <div
              v-for="employee in employees"
              :key="employee.id"
              class="employee-item"
              @click="selectEmployee(employee)"
            >
              <img
                :src="getImageUrl(employee)"
                :alt="employee.name"
                class="employee-avatar"
              />
              <div class="employee-info">
                <h4>{{ employee.name }}</h4>
                <p>ID: {{ employee.employee_id }}</p>
                <p>Age: {{ employee.age }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import EmployeeCard from "./EmployeeCard.vue";
import BarChart from "./BarChart.vue";

export default {
  name: "EmployeeList",
  components: {
    EmployeeCard,
    BarChart,
  },
  data() {
    return {
      employees: [],
      currentPage: 1,
      cardsPerPage: 3,
      showEditModal: false,
      selectedCardIndex: null,
      loading: false,
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.employees.length / this.cardsPerPage);
    },
    paginatedEmployees() {
      const start = (this.currentPage - 1) * this.cardsPerPage;
      const end = start + this.cardsPerPage;
      return this.employees.slice(start, end);
    },
  },
  async mounted() {
    await this.fetchEmployees();
  },
  methods: {
    async fetchEmployees() {
      this.loading = true;
      try {
        const response = await axios.get(
          "http://localhost:8000/api/employees/"
        );
        this.employees = response.data;
      } catch (error) {
        console.error("Error fetching employees:", error);
        // Fallback to mock data if API is not available
        this.employees = [
          {
            id: 1,
            name: "John Smith",
            employee_id: "EMP001",
            age: 28,
            photo: "/media/employee1.jpg",
          },
          {
            id: 2,
            name: "Sarah Johnson",
            employee_id: "EMP002",
            age: 32,
            photo: "/media/employee2.jpg",
          },
          {
            id: 3,
            name: "Michael Brown",
            employee_id: "EMP003",
            age: 29,
            photo: "/media/employee3.jpg",
          },
          {
            id: 4,
            name: "Emily Davis",
            employee_id: "EMP004",
            age: 26,
            photo: "/media/employee4.jpg",
          },
          {
            id: 5,
            name: "David Wilson",
            employee_id: "EMP005",
            age: 35,
            photo: "/media/employee5.jpg",
          },
          {
            id: 6,
            name: "Lisa Anderson",
            employee_id: "EMP006",
            age: 31,
            photo: "/media/employee6.jpg",
          },
        ];
      }
      this.loading = false;
    },
    openEditModal(cardIndex) {
      this.selectedCardIndex = cardIndex;
      this.showEditModal = true;
    },
    closeEditModal() {
      this.showEditModal = false;
      this.selectedCardIndex = null;
    },
    selectEmployee(employee) {
      if (this.selectedCardIndex !== null) {
        // Find the actual index in the full employees array
        const pageStart = (this.currentPage - 1) * this.cardsPerPage;
        const actualIndex = pageStart + this.selectedCardIndex;

        // Update the employee at the selected card position
        this.employees[actualIndex] = { ...employee };
      }
      this.closeEditModal();
    },
    getImageUrl(employee) {
      // Check if it's a Django media URL
      if (employee.photo && employee.photo.startsWith("/media/")) {
        return `http://localhost:8000${employee.photo}`;
      }
      // Otherwise use local media folder
      return employee.photo || "/media/employee1.jpg";
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
  },
};
</script>

<style scoped>
.employee-list {
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.cards-container {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2rem;
  margin-bottom: 2rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.pagination-info {
  text-align: center;
  margin-bottom: 2rem;
  color: white;
}

.pagination-info h2 {
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
  font-weight: 300;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin-top: 2rem;
}

.pagination-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s ease;
}

.pagination-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  color: white;
  font-weight: 500;
}

.chart-container {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  margin-top: 2rem;
}

.chart-container h2 {
  color: white;
  text-align: center;
  margin-bottom: 1rem;
  font-weight: 300;
  font-size: 2rem;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.chart-description {
  color: rgba(255, 255, 255, 0.8);
  text-align: center;
  margin-bottom: 2rem;
  font-size: 1.1rem;
  font-style: italic;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background: white;
  border-radius: 20px;
  max-width: 600px;
  width: 90%;
  max-height: 80%;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.modal-header h3 {
  margin: 0;
  font-weight: 300;
}

.close-btn {
  background: none;
  border: none;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  line-height: 1;
}

.modal-body {
  padding: 1.5rem 2rem;
  max-height: 400px;
  overflow-y: auto;
}

.employee-list-modal {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.employee-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.employee-item:hover {
  background: #f5f5f5;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.employee-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 1rem;
}

.employee-info h4 {
  margin: 0 0 0.25rem 0;
  color: #333;
}

.employee-info p {
  margin: 0.125rem 0;
  color: #666;
  font-size: 0.9rem;
}
</style>
