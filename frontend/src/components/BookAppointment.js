import { useState } from "react";
import axios from "axios";
import dayjs from "dayjs";
import { API_BASE_URL } from "../App";

const bookAppointmentForUser = async (patient_pk, appointmentId) => {
  try {
    const result = await axios.patch(
      API_BASE_URL + `/appointments/${appointmentId}/book/`,
      {
        patient_pk,
      }
    );
    return result.data;
  } catch (e) {
    // console.log(e.response.status);
    return e.response.status;
  }
};

export default function BookAppointment({ patients, appointments, refetchAppointments }) {
  const [selectedUser, setSelectedUser] = useState();
  const [selectedSlot, setSelectedSlot] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const [submitMessage, setSubmitMessage] = useState("");

  const onSubmit = async (event) => {
    setIsLoading(true);
    event.preventDefault();
    setSubmitMessage("");
    const result = await bookAppointmentForUser(selectedUser, selectedSlot);
    if (result === 400) {
      setSubmitMessage("Overlapping appointment");
      return;
    }
    if (result === 405) {
      setSubmitMessage("Not allowed, In case if appointment is already booked with patient");
      return;
    }
    await refetchAppointments();
    setSubmitMessage(
      "Booked Appointment for an user: " + JSON.stringify(result)
    );
    setIsLoading(false);
  };
  return (
    <div>
      <h1>Book Appointment</h1>
      <div>
        <select
          onChange={(e) => {
            setSelectedUser(e.target.value);
          }}
          value={selectedUser}
        >
          <option disabled selected value>
            {" "}
            -- select an option --{" "}
          </option>
          {patients.map(({ pk, first_name, last_name }) => (
            <option value={pk}>
              {first_name} {last_name}
            </option>
          ))}
        </select>
        <select
          onChange={(e) => {
            setSelectedSlot(e.target.value);
          }}
          value={selectedSlot}
        >
          <option disabled selected value>
            {" "}
            -- select an option --{" "}
          </option>
          {appointments.map(({ pk, start_time, end_time }) => (
            <option value={pk}>
              {dayjs(start_time).format("DD/MM/YYYY HH:MM")} to{" "}
              {dayjs(end_time).format("DD/MM/YYYY HH:MM")}
            </option>
          ))}
        </select>
        <button onClick={onSubmit} disabled={isLoading}>
          Submit
        </button>
      </div>
      {submitMessage && (
        <p>
          <i>{submitMessage}</i>
        </p>
      )}
    </div>
  );
}
