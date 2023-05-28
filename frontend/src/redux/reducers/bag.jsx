import { useEffect, useState } from 'react';
import axios from 'axios';
import React from 'react';

let bag=[
    {
      id:1,
      Quantity:1,
      Memory:'260',
      Color:'Black'
    },
    {
      id:2,
      Quantity:1,
      Memory:'260',
      Color:'Black'
    },
    {
      id:3,
      Quantity:2,
      Memory:'260',
      Color:'Black'
    },
  ]

export default (state = bag, acion) => {
    switch (acion.type) {
        default: return state
    }
}
