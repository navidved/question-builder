import { Stack, Typography, Button, TextField, Box } from "@mui/material";
import { useState } from "react";
import { useQuery } from "@tanstack/react-query";

export default function Home() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");

  const { isLoading, error, data } = useQuery({
    queryKey: ["repoData"],
    queryFn: () =>
      fetch("https://api.github.com/repos/TanStack/query").then((res) =>
        res.json()
      ),
  });

  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;

  console.log({ data });

  return (
    <Stack>
      <Typography variant="h4">سلام دانشپذیر عزیز ...</Typography>
      <Typography variant="h4">
        به نظر سنجی دانشکار خوش آمدین این پرسش نامه شامل ۵ سوال تستی و تشریحی می
        باشد و توجه کنید با دقت به تمام سوالات پاسخ دهید و در نهایت دکمه ذخیره و
        ارسال را بزنید
      </Typography>
      <Typography variant="h4" color="#46D1FC">
        لطفا نام و نام خانوادگی خود را وارد کنید
      </Typography>

      <form autoComplete="off" onSubmit={() => console.log("here")}>
        <TextField
          id="visitor_first_name"
          onChange={(e) => setFirstName(e.target.value)}
          fullWidth
        />

        <TextField
          id="visitor_last_name"
          onChange={(e) => setLastName(e.target.value)}
          fullWidth
        />
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            gap: "10px",
            marginTop: "40px",
          }}
        >
          <Button
            variant="contained"
            sx={{ width: "25%", borderRadius: "12px", fontSize: "20px" }}
          >
            مرحله بعد
          </Button>
          <Button
            variant="contained"
            sx={{ width: "25%", borderRadius: "12px", fontSize: "20px" }}
          >
            مرحله قبل
          </Button>
          <Button
            variant="contained"
            sx={{ width: "25%", borderRadius: "12px", fontSize: "20px" }}
          >
            ذخیره و ارسال
          </Button>
        </Box>
      </form>
    </Stack>
  );
}
