import { Stack, TextField, Typography } from "@mui/material";

export default function AuthCheck({
  auth_method,
  setFormAuthValue,
  isError,
}: 
{
  auth_method: string;
  setFormAuthValue: any;
  isError: boolean;
}) {
  return (
    <>
      {auth_method == "phone" ? (
        <Stack>
          <Typography variant="h5" mb={3}>
            شماره تلفن خود را وارد کنید
          </Typography>
          <TextField onChange={(e) => setFormAuthValue(e.target.value)} />
          {isError && (
            <Typography fontSize={8} color="red" fontWeight={500}>
              شماره تلفن وارد شده صحیح نیست
            </Typography>
          )}
        </Stack>
      ) : auth_method == "email" ? (
        <Stack>
          <Typography variant="h5" mb={3}>
            ایمیل خود را وارد کنید
          </Typography>
          <TextField onChange={(e) => setFormAuthValue(e.target.value)} />
          {isError && (
            <Typography fontSize={12} color="red" fontWeight={500}>
              ایمیل وارد شده صحیح نیست
            </Typography>
          )}
        </Stack>
      ) : (
        <Typography>خوش آمدید</Typography>
      )}
    </>
  );
}
