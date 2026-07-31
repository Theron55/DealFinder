# DealWise
An app that can find you the best deals on sites like Ebay
# Used-Deal Assistant — Validation Brief

## Working Product Name

**Dealwise**

Temporary alternatives:

* DealScout
* WorthIt
* Secondhand Scout
* BuySmart
* TrueDeal

The name can change later. The product concept matters more than branding right now.

---

## 1. The Problem

Buying used products can save people a significant amount of money, but finding a genuinely good deal is difficult and time-consuming.

A buyer may need to:

* Search several marketplaces separately
* Compare products with different specifications
* Research the normal used-market price
* Determine whether included accessories add real value
* Evaluate the seller’s reliability
* Identify missing information or suspicious wording
* Understand whether a cheaper alternative would meet the same need
* Repeatedly check for new listings

Most marketplaces provide many search results but little decision support. They help users find listings, but they do not reliably tell users which listing is the best purchase for their specific needs.

The cheapest listing may not be the best deal. It could have hidden damage, missing accessories, poor seller protection, expensive shipping, or specifications that do not fit the buyer’s intended use.

---

## 2. Target User

The initial target user is:

> A budget-conscious beginner or intermediate buyer searching for used electronics who does not have enough product knowledge to confidently compare models and evaluate listings.

Initial product categories may include:

* Cameras and lenses
* Laptops
* Gaming computers
* Computer components
* Phones
* Audio equipment
* Gaming consoles

The product could eventually support additional used-item categories, but the first version should focus on products where specifications, condition, and accessories meaningfully affect value.

---

## 3. The Frustrating Situation

The user often knows what they want to accomplish but may not know the exact product model they should buy.

For example, the user may say:

> “I need a compact camera for cinematic travel videos. My budget is $700, used is fine, and I want a lens included.”

The user must currently perform several separate tasks:

1. Research which camera models fit the use case.
2. Search multiple marketplaces for each model.
3. Compare body-only listings with bundles.
4. Evaluate condition and seller reliability.
5. Research normal market prices.
6. Understand the value of included accessories.
7. Look for hidden risks or compatibility issues.
8. Continue checking for new listings.

This process can take hours and still leave the buyer uncertain.

---

## 4. Core Product Promise

> **Describe what you need and your budget. Dealwise finds the used listings most worth considering and explains their price, benefits, tradeoffs, and risks in plain language.**

The product should reduce dozens of listings into a small number of understandable recommendations.

Instead of showing the user fifty results, Dealwise should identify:

* Best overall value
* Lowest-risk purchase
* Cheapest acceptable option
* Best upgrade opportunity
* Listings that should probably be avoided

---

## 5. Main Differentiator

### Need-Based Deal Matching

Most marketplace searches assume the buyer already knows the exact product model they want.

Dealwise begins with the buyer’s actual need.

Instead of requiring:

> “Sony ZV-E10”

The user can enter:

> “A beginner-friendly camera for travel video under $700. It needs good autofocus, a lens, and better image quality than my phone.”

Dealwise would then:

1. Translate the request into product requirements.
2. Identify suitable models.
3. Search supported listings.
4. Compare complete purchase costs.
5. Rank listings based on value and suitability.
6. Explain why each recommendation fits.
7. Identify risks and missing information.
8. Suggest questions to ask the seller.
9. Notify the user when a stronger deal appears.

The goal is not merely to find the lowest price.

The goal is to identify the purchase that offers the strongest combination of:

* Price
* Condition
* Seller trust
* Buyer protection
* Included accessories
* Product suitability
* Compatibility
* Listing completeness

---

## 6. Current Competitor Landscape

Several existing products solve parts of this problem.

### YrdSale

YrdSale searches multiple secondhand marketplaces and uses AI to assess value, condition, and potential listing risks.

**Strength:** Cross-marketplace discovery.

**Possible opportunity:** Create a clearer need-based recommendation experience instead of primarily helping users browse listings.

### Deal Scout

Deal Scout analyzes listings across marketplaces, compares prices, detects possible scams, and assists with negotiation.

**Strength:** Detailed listing analysis.

**Possible opportunity:** Recommend the correct product model before analyzing individual listings.

### Spottable

Spottable provides marketplace alerts, fair-price estimates, condition analysis, and deal scoring.

**Strength:** Alerts and Facebook Marketplace support.

**Possible opportunity:** Provide broader product comparisons and clearer explanations of why one model fits the user better than another.

### PricePath

PricePath lets users paste a used listing and receive price guidance, seller-risk analysis, and negotiation assistance.

**Strength:** Simple listing analysis.

**Possible opportunity:** Search for better alternatives rather than analyzing only the listing submitted by the user.

### JDMarket

JDMarket monitors several marketplaces and alerts users when potentially underpriced items appear.

**Strength:** Automated listing monitoring.

**Possible opportunity:** Rank deals based on personal suitability and purchase risk rather than price alone.

---

## 7. Competitive Position

The broad concept already exists, but the current market appears fragmented.

Existing products tend to specialize in one or more of the following:

* Marketplace aggregation
* Price tracking
* Listing analysis
* Scam detection
* Alerts
* Negotiation assistance

Dealwise should combine these ideas around one clearer promise:

> **Help the user decide what to buy, not merely where to find it.**

The product will differentiate itself through:

* Natural-language need descriptions
* Alternative model recommendations
* Transparent deal scoring
* Plain-language tradeoff explanations
* Category-specific risk checks
* Personalized alerts
* A small number of ranked recommendations

---

## 8. Initial Product Scope

The long-term product may support many used-item categories, but the first version should be intentionally narrow.

### Initial category

Used cameras, lenses, and selected consumer electronics.

### Initial automated marketplace

eBay or another marketplace with an accessible and permitted developer API.

### Manually supported marketplaces

For marketplaces without suitable public APIs, the user can paste:

* Listing title
* Price
* Description
* Seller information
* Listing URL
* Screenshots or product photos in a later version

The application can then analyze the information without automatically scraping the marketplace.

---

## 9. Minimum Viable Product

The first usable version will contain two main features.

### Feature One: Need-Based Search

The user provides:

* What they want to use the product for
* Maximum budget
* New or used preference
* Required features
* Location or shipping preference
* Acceptable level of risk

Example:

> “I want a compact used camera for travel videos. My maximum budget is $700. I need a lens included and good autofocus.”

The system returns:

* Recommended product models
* Matching active listings
* Total price
* Estimated fair-market range
* Deal score
* Important tradeoffs
* Seller-risk information
* Explanation of why each listing was selected

### Feature Two: Analyze a Listing

The user pastes a listing or enters its details.

The system returns:

* Identified product and model
* Estimated fair-price range
* Deal score
* Positive signs
* Potential red flags
* Missing information
* Questions to ask the seller
* Suggested offer price
* Comparable alternatives

---

## 10. Initial Deal Score

The score should be transparent and should not be decided entirely by an AI model.

A first scoring model could be:

* **35% — Price relative to estimated market value**
* **20% — Match with the user’s requirements**
* **15% — Seller reliability**
* **10% — Product condition**
* **10% — Returns and buyer protection**
* **5% — Included accessories**
* **5% — Listing completeness**

The application should display an explanation such as:

> **Deal Score: 8.4/10**

> This listing is approximately 16% below the normal used price and includes a lens and two batteries. The seller has strong feedback and accepts returns. The main concern is that the shutter count is not provided.

The scoring weights can later be adjusted using user feedback and purchase outcomes.

---

## 11. Example User Request

> “Find a compact used camera under $700 for cinematic travel videos. It must include a lens, have reliable autofocus, and be meaningfully better than an iPhone 12.”

### Ideal Result Format

#### Best Overall Value

**Sony ZV-E10 with 16–50mm lens — $575**

**Deal Score:** 8.7/10

**Why it fits:**

* Good autofocus
* Compact body
* Strong video quality
* Lens included
* Fits comfortably within budget

**Potential concerns:**

* No in-body stabilization
* Battery condition is unknown
* Shutter count is not listed

**Questions for the seller:**

* Has the camera ever been dropped or exposed to water?
* Are there scratches on the sensor or lens?
* Is the original battery and charger included?
* Are all buttons, ports, and autofocus functions working?

#### Lowest-Risk Option

**Used retailer listing with warranty — $640**

**Deal Score:** 8.2/10

**Why it fits:**

* Warranty included
* Clearly graded condition
* Return protection
* Lower risk than a private seller

**Tradeoff:**

* Approximately $65 more expensive than the best-value option

#### Cheapest Acceptable Option

**Sony a6000 bundle — $430**

**Deal Score:** 7.3/10

**Why it fits:**

* Significantly cheaper
* Lens included
* Good image quality for the price

**Tradeoffs:**

* Older autofocus
* Weaker video features
* Less suitable for cinematic travel video

#### Avoid

**Sony ZV-E10 body only — $510**

**Reason:**

After purchasing a suitable lens and accessories, the total price would exceed stronger bundle options.

---

## 12. Rough Results Screen

```text
------------------------------------------------------------
DEALWISE
Find the used purchase most worth making
------------------------------------------------------------

What are you looking for?
[ A compact camera for cinematic travel videos             ]

Maximum budget
[ $700 ]

Required features
[ Lens included, good autofocus, compact                    ]

Condition
[ Used is fine ]

Location
[ Shipped or within 75 miles ]

[ FIND THE BEST DEALS ]
------------------------------------------------------------

TOP RECOMMENDATIONS

1. BEST OVERALL VALUE
Sony ZV-E10 + 16–50mm Lens
Total Price: $575
Deal Score: 8.7/10

Why it fits:
✓ Strong autofocus
✓ Compact
✓ Lens included
✓ Below average market price

Risks:
! No shutter count listed
! Battery health unknown

[ VIEW LISTING ] [ FULL ANALYSIS ] [ SAVE ALERT ]

------------------------------------------------------------

2. LOWEST-RISK OPTION
Sony ZV-E10 Retailer-Certified Bundle
Total Price: $640
Deal Score: 8.2/10

Why it fits:
✓ Warranty
✓ Return protection
✓ Condition verified

Tradeoff:
! Costs $65 more

[ VIEW LISTING ] [ FULL ANALYSIS ] [ SAVE ALERT ]

------------------------------------------------------------

3. CHEAPEST ACCEPTABLE OPTION
Sony a6000 + Kit Lens
Total Price: $430
Deal Score: 7.3/10

Why it fits:
✓ Low price
✓ Lens included

Tradeoffs:
! Older video features
! Weaker autofocus

[ VIEW LISTING ] [ FULL ANALYSIS ]

------------------------------------------------------------

WHY THESE WERE SELECTED
[ View comparison table ]

LISTINGS TO AVOID
[ View rejected listings and explanations ]
------------------------------------------------------------
```

---

## 13. First Validation Test

Before building the full application, manually test the product idea with five people.

Ask each person to describe a used product they are considering.

For each person:

1. Gather their budget and intended use.
2. Research suitable products manually.
3. Find several listings.
4. Rank the three strongest options.
5. Explain the tradeoffs and risks.
6. Ask whether the result saved them time or increased their confidence.

Important questions:

* Was the recommendation useful?
* Did the user trust the deal score?
* What information was missing?
* Would the user return for another purchase?
* Would the user want an alert for future listings?
* Would the user pay for this or tolerate affiliate links?
* Which part was most valuable: discovery, price analysis, risk analysis, or model recommendations?

The results of these conversations should guide the first version.

---

## 14. First Success Metrics

The initial project will be considered successful when:

* Five people use it for a real purchase decision.
* At least three users say it saved them meaningful research time.
* At least one user returns to analyze another product.
* One user acts on a recommendation or creates an alert.
* The application successfully analyzes at least 50 listings.
* The system produces understandable reasons for every deal score.

The first goal is not revenue or thousands of users.

The first goal is proof that people find the result genuinely useful.

---

## 15. Technical Skills Demonstrated

This project can demonstrate:

* API integration
* Python backend development
* Frontend development
* SQL and database design
* Data normalization
* Scheduled background jobs
* Search and filtering
* Product recommendation logic
* AI-assisted information extraction
* Structured LLM outputs
* Transparent scoring systems
* User authentication
* Email alerts
* Analytics
* Deployment
* User research
* Product iteration

---

## 16. Initial Technical Stack

A practical first stack:

* **Backend:** Flask or FastAPI
* **Frontend:** React or simple server-rendered HTML
* **Database:** SQLite initially, PostgreSQL after deployment
* **Marketplace data:** Official marketplace API
* **AI:** LLM used for requirement extraction and listing-description analysis
* **Scheduled searches:** Cron job or background task
* **Deployment:** Render, Railway, Fly.io, or a similar service
* **Version control:** GitHub

The AI should assist with interpreting language, but important calculations such as price comparisons and deal scores should remain rule-based and explainable.

---

## 17. Product Risks

### Marketplace access

Not every marketplace provides a public API. The product should avoid relying on unauthorized scraping.

### Inconsistent listing information

Listings may contain incorrect, vague, or missing information. The application must clearly communicate uncertainty.

### AI hallucinations

The system should not invent specifications, accessories, condition details, or seller information.

### Category complexity

The factors that define a good camera deal are different from those that define a good laptop or furniture deal. Expansion should happen category by category.

### User trust

The app must explain why it recommends a listing. A score without supporting evidence will not be trusted.

### Affiliate bias

If the product later earns affiliate revenue, recommendations must remain independent and clearly disclose any financial relationships.

---

## 18. Long-Term Vision

Dealwise becomes a personal buying assistant for the secondhand economy.

A user describes what they need, and the product:

1. Identifies suitable products.
2. Searches supported marketplaces.
3. Normalizes inconsistent listings.
4. Calculates true purchase cost.
5. Estimates fair value.
6. evaluates condition and seller risk.
7. Explains product tradeoffs.
8. Ranks the best choices.
9. Monitors future listings.
10. Alerts the user when a meaningfully better option appears.

The long-term product could support categories such as:

* Electronics
* Cameras
* Tools
* Outdoor equipment
* Musical instruments
* Furniture
* Appliances
* Sporting goods
* Collectibles

Expansion should be driven by actual user demand.

---

## 19. One-Sentence Pitch

> **Dealwise helps people find the used products most worth buying by comparing price, condition, seller trust, product fit, and purchase risk across marketplace listings.**

---

## 20. First GitHub Commit

**Repository name:**

`dealwise`

**Commit message:**

`Add initial product vision and competitor analysis`

**Recommended initial files:**

```text
dealwise/
├── README.md
├── docs/
│   ├── validation-brief.md
│   ├── competitor-notes.md
│   └── interface-sketch.md
└── .gitignore
```

---

## 21. Tomorrow’s Next Step

The next development task is:

> Build a basic page where the user enters what they are looking for, their maximum budget, and required features.

The page does not need to search marketplaces yet.

Its only purpose is to:

1. Collect the user’s request.
2. Display the request in a structured format.
3. Establish the first working version of the interface.

The first milestone is not a complete deal engine.

The first milestone is a working page that makes the idea real.
