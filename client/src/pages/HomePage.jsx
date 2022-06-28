import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router";
import { useSearchParams } from "react-router-dom";
import Paginate from "../components/Paginate";
import { Row, Col, InputGroup } from "react-bootstrap";
import Product from "../components/Product";
import SpinnerComponent from "../components/SpinnerComponent";
import Message from "../components/Message";
import ProductCarousel from "../components/ProductCarousel";
import { listProducts } from "../actions/productActions";

const HomePage = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();
  const keyword = searchParams.get("keyword");
  const pageQuery = searchParams.get("page");
  const productList = useSelector((state) => state.productList);
  const { error, loading, products, page, pages } = productList;

  useEffect(() => {
    dispatch(listProducts(keyword, pageQuery));
  }, [dispatch, keyword, pageQuery]);

  return (
    <div>
      {!keyword && <ProductCarousel />}
      <h1>Latest Products UPDATED</h1>
      {loading ? (
        <SpinnerComponent />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <Row>
            {products.map((product) => (
              <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
                <Product product={product} />
              </Col>
            ))}
          </Row>
          <Paginate pages={pages} page={page} keyword={keyword} />
        </div>
      )}
    </div>
  );
};

export default HomePage;
