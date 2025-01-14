import math
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma):
  
   
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return call_price, put_price

if __name__ == "__main__":
    # Taking user input
    S = float(input("Enter Current Asset Price: "))
    K = float(input("Enter Strike Price: "))
    T = float(input("Enter Time to Maturity (Years): "))
    sigma = float(input("Enter Volatility (σ): "))
    r = float(input("Enter Risk-Free Interest Rate: "))
    
    call_price, put_price = black_scholes(S, K, T, r, sigma)
    
    print(f"\nCall Option Price: {call_price:.4f}")
    print(f"Put Option Price: {put_price:.4f}")
