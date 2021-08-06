import { useState } from "react";
import { API_BASE_URL } from "../App";
import axios from "axios";
import DateTimePicker from "react-datetime-picker";

const createAppointment = async (startTime, endTime) => {
  try {
    const result = await axios.post(API_BASE_URL + "/appointments/", {
      start_time: startTime,
      end_time: endTime,
    });
    return result.data;
  } catch (e) {
    console.error(e);
    return null;
  }
};

const CreateAppointment = ({ refetchAppointments }) => {
  const [startTime, setStartTime] = useState(new Date());
  const [endTime, setEndTime] = useState(new Date());
  const [isLoading, setIsLoading] = useState(false);
  const [submitMessage, setSubmitMessage] = useState("");

  const handleSubmit = async (event) => {
    setIsLoading(true);
    event.preventDefault();
    setSubmitMessage("");
    const result = await createAppointment(startTime, endTime);
    if (!result) {
      setSubmitMessage("Unable to create Appointment");
      return;
    }
    await refetchAppointments();
    setSubmitMessage("Created Appointment: " + JSON.stringify(result));
    setIsLoading(false);
  };

  return (
    <>
      <h2>Create a new Appointment</h2>
      <form onSubmit={handleSubmit}>
        <label for="start-time">Starts at:</label>
        <br />
        <DateTimePicker
          id="start-time"
          onChange={(val) => setStartTime(val)}
          value={startTime}
        />
        <br />
        <label for="end-time">Ends at:</label>
        <br />
        <DateTimePicker
          id="end-time"
          onChange={(val) => setEndTime(val)}
          value={endTime}
        />
        <br />
        <button type="submit" disabled={isLoading}>
          Submit
        </button>
      </form>
      {submitMessage && (
        <p>
          <i>{submitMessage}</i>
        </p>
      )}
    </>
  );
};

export default CreateAppointment;
