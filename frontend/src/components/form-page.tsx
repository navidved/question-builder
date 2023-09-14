import { Stack, Typography, Button, Box } from "@mui/material";
import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import axios from "axios";
import { useState } from "react";

export default function FormPage() {
  let formId = useParams();
  const [formItem, setFormItem] = useState<number>(-1);

  const getFormById = async (formId: string): Promise<any> => {
    const { data } = await axios.get(
      `http://127.0.0.1:8000/api/visitor/${formId}`
    );
    return data;
  };

  function useForm(formId: string) {
    return useQuery({
      queryKey: ["form", formId],
      queryFn: () => getFormById(formId),
      enabled: !!formId,
    });
  }
  const { status, data, error, isFetching } = useForm(formId.formId);
  if (isFetching) return "Loading...";
  if (error) return "An error has occurred: " + error.message;

  const { form_items } = data;

  console.log({ form_items });
  console.log({ data });

  function handleStart() {
    setFormItem(0);
  }

  return (
    <Stack justifyContent="space-between" alignItems="center">
      <Typography variant="h4">{data.title}</Typography>
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          gap: "10px",
          marginTop: "40px",
        }}
      >
        {formItem == -1 ? (
          <Button
            onClick={() => handleStart()}
            variant="contained"
            sx={{ width: "25%", borderRadius: "12px", fontSize: "20px" }}
          >
            شروع
          </Button>
        ) : (
          <Box
            sx={{
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
              gap: "10px",
              marginTop: "40px",
            }}
          >
            <Typography>{form_items[formItem].title}</Typography>
            {form_items[formItem].options.text != null && (
              <Typography>Text Input Question</Typography>
            )}
            {form_items[formItem].options["multi-choice"] != null && (
              <Typography>Multi Choice Question</Typography>
            )}
            {form_items[formItem].options["radio-button"] != null && (
              <Typography>Radio Button Question</Typography>
            )}
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
                sx={{
                  width: "content-fit",
                  borderRadius: "12px",
                  fontSize: "20px",
                }}
                onClick={() => setFormItem((prev) => prev + 1)}
                disabled={formItem == form_items.length - 1}
              >
                مرحله بعد
              </Button>
              <Button
                variant="contained"
                sx={{
                  width: "content-fit",
                  borderRadius: "12px",
                  fontSize: "20px",
                }}
                onClick={() => setFormItem((prev) => prev - 1)}
                disabled={formItem == 0}
              >
                مرحله قبل
              </Button>
              <Button
                variant="contained"
                sx={{
                  width: "content-fit",
                  borderRadius: "12px",
                  fontSize: "20px",
                }}
              >
                ذخیره سازی و ارسال
              </Button>
            </Box>
          </Box>
        )}
      </Box>
    </Stack>
  );
}
