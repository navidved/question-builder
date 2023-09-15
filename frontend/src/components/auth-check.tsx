import { Stack, TextField, Typography } from "@mui/material";

export default function AuthCheck({
  auth_method,
  setFormAuthValue,
}: {
  auth_method: string;
  setFormAuthValue: any;
}) {
  return (
    <>
      {auth_method == "PH" ? (
        <Stack>
          <Typography variant="h5" mb={3}>
            شماره تلفن خود را وارد کنید
          </Typography>
          <TextField onChange={(e) => setFormAuthValue(e.target.value)} />
        </Stack>
      ) : auth_method == "EM" ? (
        <Stack>
          <Typography variant="h5" mb={3}>
            ایمیل خود را وارد کنید
          </Typography>
          <TextField onChange={(e) => setFormAuthValue(e.target.value)} />
        </Stack>
      ) : (
        <Typography>خوش آمدید</Typography>
      )}
    </>
  );
}
