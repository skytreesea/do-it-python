import numpy_financial as npf

cf = [-750, -250, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

# Calculate the internal rate of return (IRR)
irr = npf.irr(cf)
print("Internal rate of return (IRR): {:.2%}".format(irr))

# Calculate the net present value (NPV)
discount_rate = 0.045  # Discount rate of 4.5%
npv = npf.npv(discount_rate, cf)
print("Net present value (NPV): {:.2f}".format(npv))