<template>
  <div class="chart-wrapper">
    <div v-if="loading" class="loading">Loading chart data...</div>
    <canvas v-else ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  BarController,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import axios from "axios";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  BarController,
  Title,
  Tooltip,
  Legend
);

export default {
  name: "BarChart",
  props: {
    employees: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      chart: null,
      loading: true,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Age",
            backgroundColor: [
              "rgba(102, 126, 234, 0.8)",
              "rgba(118, 75, 162, 0.8)",
              "rgba(255, 99, 132, 0.8)",
              "rgba(54, 162, 235, 0.8)",
              "rgba(255, 206, 86, 0.8)",
              "rgba(75, 192, 192, 0.8)",
            ],
            borderColor: [
              "rgba(102, 126, 234, 1)",
              "rgba(118, 75, 162, 1)",
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
            ],
            borderWidth: 2,
            borderRadius: 8,
            data: [],
          },
        ],
      },
    };
  },
  watch: {
    employees: {
      handler(newEmployees) {
        if (newEmployees && newEmployees.length > 0) {
          this.updateChart(newEmployees);
        }
      },
      deep: true,
    },
  },
  async mounted() {
    console.log("✅ BarChart component mounted");
    await this.fetchChartData();
    this.createChart();
  },
  beforeUnmount() {
    if (this.chart) {
      this.chart.destroy();
    }
  },
  methods: {
    async fetchChartData() {
      this.loading = true;
      try {
        // If employees prop is provided, use it
        if (this.employees && this.employees.length > 0) {
          this.updateChartData(this.employees);
        } else {
          // Otherwise fetch from API
          const response = await axios.get(
            "http://localhost:8000/api/employees/chart_data/"
          );
          const data = response.data;
          this.updateChartData(data);
        }
      } catch (error) {
        console.error("Error fetching chart data:", error);
        // Fallback data
        const fallbackData = [
          { name: "Sarah Johnson", age: 32 },
          { name: "Michael Brown", age: 29 },
          { name: "Emily Davis", age: 26 },
          { name: "David Wilson", age: 35 },
          { name: "Lisa Anderson", age: 31 },
        ];
        this.updateChartData(fallbackData);
      }
      this.loading = false;
    },
    updateChartData(data) {
      this.chartData.labels = data.map((item) => item.name);
      this.chartData.datasets[0].data = data.map((item) => item.age);
    },
    updateChart(employees) {
      if (this.chart && employees && employees.length > 0) {
        this.chartData.labels = employees.map((emp) => emp.name);
        this.chartData.datasets[0].data = employees.map((emp) => emp.age);
        this.chart.update();
      }
    },
    createChart() {
      if (this.loading || !this.$refs.chartCanvas) return;

      const ctx = this.$refs.chartCanvas.getContext("2d");

      this.chart = new ChartJS(ctx, {
        type: "bar",
        data: this.chartData,
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: true,
              labels: {
                color: "white",
                font: {
                  size: 14,
                },
              },
            },
            title: {
              display: true,
              text: "Employee Name vs Age",
              color: "white",
              font: {
                size: 18,
                weight: "bold",
              },
            },
            tooltip: {
              backgroundColor: "rgba(0, 0, 0, 0.8)",
              titleColor: "white",
              bodyColor: "white",
              callbacks: {
                label: function (context) {
                  return `${context.label}: ${context.parsed.y} years old`;
                },
              },
            },
          },
          scales: {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: "Age (Years)",
                color: "white",
                font: {
                  size: 14,
                  weight: "bold",
                },
              },
              ticks: {
                color: "white",
                font: {
                  size: 12,
                },
              },
              grid: {
                color: "rgba(255, 255, 255, 0.2)",
              },
            },
            x: {
              title: {
                display: true,
                text: "Employee Names",
                color: "white",
                font: {
                  size: 14,
                  weight: "bold",
                },
              },
              ticks: {
                color: "white",
                font: {
                  size: 11,
                },
                maxRotation: 45,
                minRotation: 0,
              },
              grid: {
                color: "rgba(255, 255, 255, 0.2)",
              },
            },
          },
          animation: {
            duration: 1000,
            easing: "easeInOutQuart",
          },
        },
      });
    },
  },
};
</script>

<style scoped>
.chart-wrapper {
  height: 450px;
  width: 100%;
  position: relative;
}

.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  color: white;
  font-size: 1.2rem;
  font-weight: 300;
}

canvas {
  max-height: 100%;
  width: 100% !important;
  height: 100% !important;
}
</style>
