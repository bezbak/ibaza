import React from 'react'

export default function Result() {
  return (
    <div className='Result Fav-Ins-block'>
        <p className="h4">Результаты предварительного расчёта</p>
        <div className="ResiltMain">
            <p>
                <span>Сумма кредита</span>
                <span className='big'>51 605 сом</span>
            </p><hr />
            <p>
                <span>Первоначальный взнос</span>
                <span className='big'>20 сом</span>
            </p><hr />
            <p>
                <span>Срок кредита</span>
                <span className='big'>3 месяца</span>
            </p><hr />
            <p>
                <span>Ежемесячный платеж</span>
                <span className='big'>18 066 сом</span>
            </p><hr />
            <p>
                <span>Общая выплата</span>
                <span className='big'>54 218 сом</span>
            </p><hr />
            <p>
                <span>Наценка</span>
                <span className='big'>2 593сом</span>
            </p><hr />
            <p>
                <span>Сумма кредита</span>
                <span className='big'>51 625сом</span>
            </p><hr />
        </div>
        <input type="submit" value="Заполнить заявку" />
    </div>
  )
}
