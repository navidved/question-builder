import { Stack, Typography, Button, Box } from "@mui/material";
import { useParams } from "react-router-dom";
import { useState } from "react";
import AuthCheck from "./auth-check";
import useGetForm from "./custom-hooks/use-get-form";
import useCreateVisitor from "./custom-hooks/use-create-visitor";

export default function FormPage() {
  let params = useParams();
  let { formId } = params;
  const [formItem, setFormItem] = useState<number>(-1);
  const [formAuthValue, setFormAuthValue] = useState<string>("");

  const { status, data, error, isFetching } = useGetForm(formId);
  if (isFetching) return "Loading...";
  if (error) return "An error has occurred: " + error.message;
  const { form_items, auth_method } = data;

  const { mutate: createVisitor } = useCreateVisitor();

  function handleStart() {
    // setFormItem(0);
    console.log({ formAuthValue, auth_method });
    createVisitor({
      form: data.id,
      auth_type: auth_method,
      auth_value: formAuthValue,
    });
  }

  // const mutation = useMutation({
  //   mutationFn: (visitor) => {
  //     return axios.post(`http://127.0.0.1:8000/api/visitor/create`, visitor);
  //   },
  // });

  // const mutation = useMutation((newPost) =>
  //   axios.post("https://jsonplaceholder.typicode.com/posts", newPost)
  // );

  // const submitData = () => {
  //   mutation.mutate({ title, body });
  // };

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
