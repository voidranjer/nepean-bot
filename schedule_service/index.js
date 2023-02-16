import schedule from "node-schedule";
import executor from "./executor.js";

// const job = schedule.scheduleJob("55 59 17 ? * WED *", () => {
const job = schedule.scheduleJob("* * * * * *", () => {
  executor();
});
