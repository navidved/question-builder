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
import useGetForm from "./custom-hooks/use-get-form";
import axios from "axios";

export default function FormPage() {
  let params = useParams();
  let { formId } = params;

  type VisitorAnswerType = {
    "multi-choice": string[];
    "radio-button": string;
    text: string;
  };
  type visitorAuthCheckType = {
    form: number;
    auth_type: string;
    auth_value: string;
  };

  if (formId == undefined) return null;
  const [formItem, setFormItem] = useState<number>(-1);
  const [formAuthValue, setFormAuthValue] = useState<string>("");
  const [visitorAuth, setVisitorAuth] = useState();
  const [visitorAnswer, setVisitorAnswer] = useState<VisitorAnswerType>({
    "multi-choice": [],
    "radio-button": "",
    text: "",
  });

  const { data, error, isFetching } = useGetForm(formId);
  if (isFetching) return "Loading...";
  if (error) return "An error has occurred: " + error.message;
  const { form_items, auth_method, title } = data;

  const createUser = async (userData: visitorAuthCheckType) => {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/visitor/auth/",
      userData
    );
    setVisitorAuth(response.data);
  };
  const createAnswer = async (userData) => {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/visitor/answer/create/",
      userData
    );
    return response.data;
  };

  const userData = {
    form: data.id,
    auth_type: data.auth_method,
    auth_value: formAuthValue,
  };
  function handleStart() {
    setFormItem(0);
    createUser(userData);
  }

  function handleNext() {
    setFormItem((prev) => prev + 1);
    createAnswer({
      visitor: visitorAuth != undefined ? visitorAuth?.visitor?.id : 0,
      form: data.id,
      form_item: form_items[formItem].id,
      answer: visitorAnswer,
    });
    setVisitorAnswer({ text: "", "radio-button": "", "multi-choice": [] });
  }
  function handleSubmit() {
    createAnswer({
      visitor: visitorAuth != undefined ? visitorAuth?.visitor?.id : 0,
      form: data.id,
      form_item: form_items[formItem].id,
      answer: visitorAnswer,
    });
    setVisitorAnswer({ text: "", "radio-button": "", "multi-choice": [] });
    setFormItem((prev) => prev + 1);
  }
  function handleAddAnswer(key, value) {
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
                {form_items[formItem].answer_type == "TX" && (
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
                {form_items[formItem].answer_type == "MC" && (
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
                {form_items[formItem].answer_type == "RB" && (
                  <>
                    <Typography>{form_items[formItem].description}</Typography>
                    <FormGroup>
                      <RadioGroup
                        onChange={(e) =>
                          handleAddAnswer("radio-button", e.target.value)
                        }
                      >
                        {form_items[formItem].options["radio-button"].map(
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
