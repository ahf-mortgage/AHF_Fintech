from django.utils import timezone





def calculate_commission_for_level_0(node, total_commission, split):
    """
    Calculate the commission for level 0 based on the node's MLO agent.

    Parameters:
    - node: The node object containing the MLO agent.
    - total_commission: The total commission amount to be split.
    - split: The factor by which to multiply the total commission.

    Returns:
    - The calculated commission for level 0.

    Raises:
    - AttributeError: If the node does not have a valid MLO agent.
    - ValueError: If split is not a positive number.
    """
    # Validate the split parameter
    if split <= 0:
        raise ValueError("Split must be a positive number.")

    # Check if node has an MLO agent
    if not hasattr(node, 'mlo_agent') or node.mlo_agent is None:
        raise AttributeError("Node does not have a valid MLO agent.")

    mlo_agent = node.mlo_agent
    date_joined = mlo_agent.date_joined  # Currently unused, could be relevant for future logic
    now = timezone.now()  # Currently unused, could be relevant for future logic

    # Calculate and return the commission
    return split * total_commission









def calculate_commissions(levels, all_revenue_shares, starting_node, AD9, split):
    """
    Calculate the commission for each level based on revenue shares.

    Parameters:
    - levels: List of levels for which to calculate commissions.
    - all_revenue_shares: List of revenue share objects containing percentage data.
    - starting_node: The starting node for level 0 commission calculation.
    - AD9: The base amount for commission calculations.
    - split: Additional parameter needed for commission calculation.

    Returns:
    - Dictionary mapping levels to their respective calculated commissions.
    """
    level_to_commission = {}
    
    # Validate input lengths
    if len(levels) != len(all_revenue_shares):
        raise ValueError("Length of levels and all_revenue_shares must be equal.")

    for level, revenue_share in zip(levels, all_revenue_shares):
        # Ensure revenue_share has a valid percentage attribute
        if not hasattr(revenue_share, 'percentage'):
            raise AttributeError(f"Revenue share object at level {level} does not have 'percentage' attribute.")

        # Check for valid percentage value
        if not (0 <= revenue_share.percentage <= 100):
            raise ValueError(f"Percentage for level {level} must be between 0 and 100.")

        # Calculate commission for level 0
        if level == 0:
            level_to_commission[level] = calculate_commission_for_level_0(starting_node, AD9, split)

        # Calculate the commission based on revenue share percentage
        commission_earned = AD9 * revenue_share.percentage / 100

        # Store half of the commission in the level_to_commission dictionary
        level_to_commission[level] = commission_earned / 2

    return level_to_commission