import {
  Stack,
  Typography,
  Button,
  Box,
  TextField,
  Checkbox,
  FormGroup,
  FormControlLabel,
  RadioGroup,
  Radio,
} from "@mui/material";
import { useParams } from "react-router-dom";
import { useState } from "react";
import AuthCheck from "./auth-check";
import { QuestionAnswerType } from "../api/types";
import {
  useCheckVisitorAuth,
  useCreateVisitorAnswer,
  useGetForm,
} from "../api/hooks";

export default function FormPage() {
  let params = useParams();
  let { formId } = params;

  if (formId == undefined) return null;
  const [formItem, setFormItem] = useState<number>(-1);
  const [formAuthValue, setFormAuthValue] = useState<string>("");
  const [visitorAnswer, setVisitorAnswer] = useState<QuestionAnswerType>({
    "multi-choice": [],
    "single-choice": "",
    text: "",
  });

  const [authError, setAuthError] = useState<boolean>(false);

  const { data: formData, isFetching } = useGetForm(formId);
  const { mutate: checkVisitor, data: visitorAuth } = useCheckVisitorAuth();
  const { mutate: createAnswer } = useCreateVisitorAnswer();

  function handleStart() {
    const visitorCheckData = {
      form_id: formData?.id,
      auth_type: formData?.auth_method,
      auth_value: formAuthValue,
    };
    checkVisitor(visitorCheckData, {
      onSuccess: () => {
        setFormItem(0);
      },
      onError: () => {
        setAuthError(true);
      },
    });
  }

  function handleNext() {
    setFormItem((prev) => prev + 1);
    createAnswer({
      visitor: visitorAuth != undefined ? visitorAuth?.visitor?.id : 0,
      form: formData?.id,
      form_item: formData?.form_items
        ? formData?.form_items[formItem]?.id
        : null,
      answer: visitorAnswer,
    });
    setVisitorAnswer({ text: "", "single-choice": "", "multi-choice": [] });
  }

  function handleSubmit() {
    createAnswer({
      visitor: visitorAuth != undefined ? visitorAuth?.visitor?.id : 0,
      form: formData?.id,
      form_item: formData?.form_items
        ? formData?.form_items[formItem]?.id
        : null,
      answer: visitorAnswer,
    });
    setVisitorAnswer({ text: "", "single-choice": "", "multi-choice": [] });
    setFormItem((prev) => prev + 1);
  }

  function handleAddAnswer(
    key: "multi-choice" | "single-choice" | "text",
    value: string
  ) {
    if (key == "multi-choice") {
      setVisitorAnswer((prev) => ({
        ...prev,
        "multi-choice": prev["multi-choice"].includes(value)
          ? [...prev["multi-choice"].filter((v) => v != value)]
          : [...prev["multi-choice"].filter((v) => v != value), value],
      }));
    } else {
      setVisitorAnswer((prev) => ({
        ...prev,
        [key]: value,
      }));
    }
  }

  if (isFetching) return "Loading...";
  const { form_items, auth_method, title } = formData;

  return (
    <Stack justifyContent="space-between" height="50vh">
      {formItem >= form_items.length ? (
        <Typography variant="h2" textAlign="center" mt={20}>
          آفرین 😁
        </Typography>
      ) : (
        <>
          <Stack justifyContent="start" spacing={8} direction="column">
            <Typography variant="h4">{title}</Typography>
            {formItem == -1 ? (
              <AuthCheck
                auth_method={auth_method}
                setFormAuthValue={setFormAuthValue}
                isError={authError}
              />
            ) : (
              <Box
                sx={{
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "start",
                  gap: "10px",
                  marginTop: "40px",
                }}
              >
                <Typography variant="h5">
                  {form_items[formItem].title}
                </Typography>
                {form_items[formItem].answer_type == "text" && (
                  <>
                    <Typography>{form_items[formItem].description}</Typography>
                    <TextField
                      onChange={(e) => handleAddAnswer("text", e.target.value)}
                      fullWidth
                      placeholder={form_items[formItem].options.text}
                      multiline
                      rows={4}
                    />
                  </>
                )}
                {form_items[formItem].answer_type == "multi-choice" && (
                  <>
                    <Typography>{form_items[formItem].description}</Typography>
                    <FormGroup>
                      {form_items[formItem].options["multi-choice"].map(
                        (item: string) => (
                          <FormControlLabel
                            control={
                              <Checkbox
                                name={item}
                                onChange={(e) =>
                                  handleAddAnswer(
                                    "multi-choice",
                                    e.target.value
                                  )
                                }
                              />
                            }
                            label={item}
                            value={item}
                          />
                        )
                      )}
                    </FormGroup>
                  </>
                )}
                {form_items[formItem].answer_type == "single-choice" && (
                  <>
                    <Typography>{form_items[formItem].description}</Typography>
                    <FormGroup>
                      <RadioGroup
                        onChange={(e) =>
                          handleAddAnswer("single-choice", e.target.value)
                        }
                      >
                        {form_items[formItem].options["single-choice"].map(
                          (item: string) => (
                            <FormControlLabel
                              control={<Radio />}
                              label={item}
                              value={item}
                              key={item}
                            />
                          )
                        )}
                      </RadioGroup>
                    </FormGroup>
                  </>
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
                  onClick={() => handleNext()}
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
                  onClick={() => handleSubmit()}
                >
                  ذخیره سازی و ارسال
                </Button>
              </Box>
            )}
          </Box>
        </>
      )}
    </Stack>
  );
}
