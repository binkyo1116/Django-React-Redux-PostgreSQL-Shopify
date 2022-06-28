import React, { useState } from "react";
import { Button, Form } from "react-bootstrap";
import { useNavigate } from "react-router";

const SearchBox = () => {
  const [keyword, setKeyword] = useState("");
  const navigate = useNavigate();

  const submitHandler = (e) => {
    e.preventDefault();
    if (keyword) {
      navigate(`/?keyword=${keyword}&pages=1`);
    } else {
      //redirects back itself if no query
      navigate(0);
    }
  };

  return (
    <Form
      onSubmit={submitHandler}
      className="d-flex"
      style={{ position: "absolute", right: "20%" }}
    >
      <Form.Control
        placeholder="Search products..."
        type="text"
        name="q"
        onChange={(e) => setKeyword(e.target.value)}
        className="mr-sm-2 ml-sm-5"
      ></Form.Control>

      <Button type="submit" variant="outline-success" className="p-2">
        Submit
      </Button>
    </Form>
  );
};

export default SearchBox;
