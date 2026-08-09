# Economy / Pacing Pass 3

## Click revenue
- New-run base click revenue is now **$5.00**.
- Formula: `clickRevenue = 5 × technologyMultiplier × prestigeMultiplier`.

## Infrastructure revenue
Recurring network revenue is now explicitly infrastructure-led and calculated per region:

`regionRevenue = regionInfrastructureBase × technologyMultiplier × regionalMarketMultiplier × prestigeMultiplier`

Where:
- `regionInfrastructureBase` is the sum of each deployed asset's base $/s × quantity in that region.
- `technologyMultiplier = 1 + qualityScore / 100`.
- `regionalMarketMultiplier = footholdFraction × competitionMultiplier`.
- Company network income is the sum of all regional revenue.

The Infrastructure screen now shows the base, technology multiplier, market multiplier, and actual income for the selected region.

## Research pacing
- RP caps by era: `8 / 12 / 18 / 27 / 40 RP/s`.
- Infrastructure-derived revenue gives a gradual RP throughput bonus, but the era cap prevents runaway acceleration.
- Node RP values remain relative weights. Runtime cost is:

`nodeCost = nodeRPWeight × (eraRPCap × 7 hours / fastestLegalPathWeight)`

- Fastest legal route at the era RP cap: ~7.0 hours.
- At most 30 minutes of the next era's RP cap carries over after an era transition.
- Therefore the theoretical fastest eras after Era 1 remain ~6.5 hours, before considering player inefficiency or non-maxed RP production.

## Research UI
- The graph SVG is centered in its viewport.
- Node names are centered inside their cards.
