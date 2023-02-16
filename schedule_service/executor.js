import child_process from "child_process";
import { collection, getDocs } from "firebase/firestore";
import { db } from "./firebase.js";

const collection_name = "jobs";
const script_path = "../job_service/main.py";

async function fetch_all_jobs() {
  const querySnapshot = await getDocs(collection(db, collection_name));
  const jobs = [];
  querySnapshot.forEach((doc) => {
    jobs.push(doc.data());
  });
  return jobs;
}

export default async function execute() {
  const jobs = await fetch_all_jobs();
  for (const job of jobs) {
    if (job.enabled) {
      const spawn = child_process.spawn;
      const process = spawn("python", [
        script_path,
        job.seed,
        job.court_name,
        job.time_aria,
        job.telephone,
        job.email,
        job.name,
      ]);
      process.stdout.on("data", (data) => {
        console.log(data.toString());
      });
    }
  }
}
