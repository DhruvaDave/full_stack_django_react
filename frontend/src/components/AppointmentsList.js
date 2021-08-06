const AppointmentsList = ({ appointments }) => {
  return (
    <>
      <h2>Appointments</h2>
      <p>{appointments.length} appointment(s)</p>
      <p>
        <ul>
          {appointments.map((patient) => {
            return <li>{JSON.stringify(patient)}</li>;
          })}
        </ul>
      </p>
    </>
  );
};

export default AppointmentsList;
