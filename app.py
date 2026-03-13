import streamlit as st

def calculate_mortgage_gap():
    st.title("🇨🇦 Ontario Mortgage Protection Analyzer")
    st.subheader("See if your family is actually protected or just your bank.")

    # User Inputs
    mortgage_balance = st.number_input("Current Mortgage Balance ($)", value=500000)
    monthly_payment = st.number_input("Monthly Mortgage Payment ($)", value=3000)
    interest_rate = st.slider("Interest Rate (%)", 1.0, 10.0, 5.0)

    # Simple Math for the "Gap" (educational, not a real quote)
    # Assumptions:
    # - Bank coverage ≈ remaining mortgage only
    # - Private coverage ≈ mortgage + 2 years of mortgage payments as an income buffer
    private_buffer_years = 2
    bank_coverage = mortgage_balance
    private_coverage = mortgage_balance + (monthly_payment * 12 * private_buffer_years)
    family_gap = max(private_coverage - bank_coverage, 0)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Bank Mortgage Insurance")
        st.error(f"Coverage Today: CAD {bank_coverage:,.0f}")
        st.caption("Beneficiary: The Bank")
        st.caption("Coverage shrinks as you pay off your home.")

    with col2:
        st.write("### Private Policy (For Your Family)")
        st.success(f"Target Coverage: CAD {private_coverage:,.0f}")
        st.caption("Beneficiary: Your Family")
        st.caption(f"Includes approx. {private_buffer_years} years of mortgage payments as extra protection.")

    st.divider()

    st.write("### Your Family Protection Gap (Educational Only)")
    st.metric(
        label="Extra money your family could receive vs. typical bank insurance",
        value=f"${family_gap:,.0f}",
    )
    st.caption(
        "This is a simple illustration only. Real quotes depend on age, health, underwriting, "
        "and exact product design."
    )

    st.write("### Rough Private Policy Cost (Illustrative)")
    st.write(
        "For many families with similar coverage amounts, a typical range for fully underwritten "
        "private coverage might be somewhere around **$20–$100 per month**, depending on age, health, "
        "smoking status, and the exact product."
    )
    st.caption(
        "This is *not* a real quote or guarantee. It's a broad educational range so the numbers feel concrete — "
        "your actual price could be lower or higher."
    )

    if st.button("Get a Custom Comparison & Quote"):
        st.success("I can run a proper quote with real pricing for your age and health.")
        st.write(
            f"Based on a mortgage of **CAD {mortgage_balance:,.0f}** and a monthly payment of **CAD {monthly_payment:,.0f}**."
        )
        st.write(
            "Book 60 minutes with **Akshay** here: "
            "[calendly.com/akshayreddy1024/30min](https://calendly.com/akshayreddy1024/30min)."
        )


if __name__ == "__main__":
    calculate_mortgage_gap()
