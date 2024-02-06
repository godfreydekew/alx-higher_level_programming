#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
      Perform matrix multiplication using NumPy.

      Parameters:
      - m_a (numpy.ndarray): The first matrix for multiplication.
      - m_b (numpy.ndarray): The second matrix for multiplication.

      Returns:
      numpy.ndarray: The result of the matrix multiplication.

      """
    return np.matmul(m_a, m_b)
