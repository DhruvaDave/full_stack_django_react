import dayjs from "dayjs";

const AppointmentsList = ({ appointments, patients }) => {
  return (
    <>
      <h2>Appointments</h2>
      <p>{appointments.length} appointment(s)</p>
      <p>
        <ul>
          {appointments.map((appointment) => {
            const patient = patients.find(
              ({ pk }) => appointment.patient_pk === pk
            );
            return (
              <li>
                {dayjs(appointment.start_time).format("DD/MM/YYYY HH:MM")} to{" "}
                {dayjs(appointment.end_time).format("DD/MM/YYYY HH:MM")}
                {patient && (
                  <span>
                    {" "}
                    Wtih {patient.first_name} {patient.last_name}
                  </span>
                )}
              </li>
            );
          })}
        </ul>
      </p>
    </>
  );
};

export default AppointmentsList;
