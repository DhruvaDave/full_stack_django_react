import { useState } from "react";
import { API_BASE_URL } from "../App";
import axios from "axios";

const createPatient = async (firstName, lastName) => {
  try {
    const result = await axios.post(API_BASE_URL + "/patients/", {
      first_name: firstName,
      last_name: lastName,
    });
    return result.data;
  } catch (e) {
    console.error(e);
    return null;
  }
};

const CreatePatient = ({ refetchPatients }) => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [submitMessage, setSubmitMessage] = useState("");

  const handleSubmit = async (event) => {
    setIsLoading(true);
    event.preventDefault();
    setSubmitMessage("");
    const result = await createPatient(firstName, lastName);
    if (!result) {
      setSubmitMessage("Unable to create Appointment");
      return;
    }
    await refetchPatients();
    setSubmitMessage("Created Patient: " + JSON.stringify(result));
    setIsLoading(false);
  };

  return (
    <>
      <h2>Create a new Patient</h2>
      <form onSubmit={handleSubmit}>
        <label for="first-name">First Name:</label>
        <br />
        <input
          id="first-name"
          value={firstName}
          placeholder="First name"
          onChange={(e) => setFirstName(e.target.value)}
        />
        <br />
        <label for="last-name">Ends at:</label>
        <br />
        <input
          value={lastName}
          placeholder="Last name"
          onChange={(e) => setLastName(e.target.value)}
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

export default CreatePatient;
