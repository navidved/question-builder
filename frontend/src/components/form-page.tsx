import { Stack, Typography, Button, Box } from "@mui/material";
import { useMutation, useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import axios from "axios";
import { useState } from "react";
import AuthCheck from "./auth-check";

export default function FormPage() {
  let formId = useParams();
  const [formItem, setFormItem] = useState<number>(-1);
  const [formAuthValue, setFormAuthValue] = useState<string>("");

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

  const { form_items, auth_method } = data;

  console.log({ auth_method });
  console.log({ data });
  console.log({ formAuthValue });

  function handleStart() {
    setFormItem(0);
    // mutation.mutate({
    //   form: data.id,
    //   auth_type: auth_method,
    //   auth_value: formAuthValue,
    // });
  }

  // const mutation = useMutation({
  //   mutationFn: (visitor) => {
  //     return axios.post(`http://127.0.0.1:8000/api/visitor/create`, visitor);
  //   },
  // });

  return (
    <Stack justifyContent="space-between" height="50vh">
      <Stack justifyContent="start" spacing={8} direction="column">
        <Typography variant="h4">{data.title}</Typography>
        {formItem == -1 ? (
          <AuthCheck
            auth_method={auth_method}
            formItem={formItem}
            setFormItem={setFormItem}
            formAuthValue={formAuthValue}
            setFormAuthValue={setFormAuthValue}
          />
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
          </Box>
        )}
      </Stack>
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
        )}
      </Box>
    </Stack>
  );
}
