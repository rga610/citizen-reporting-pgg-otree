from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
Citizen Reporting Public Goods Game
Participants take the role of citizens who can contribute to reporting 
faulty public infrastructure. This follows a standard public goods game structure.
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods'
    players_per_group = 4  # Default, can be overridden in session config
    num_rounds = 10  # Standard PGG typically has multiple rounds

    instructions_template = 'public_goods/Instructions.html'

    # Amount allocated to each player (in points/tokens)
    endowment = c(100)
    multiplier = 2  # Public good multiplier
    
    # Treatment groups: 1, 2, 3, 4
    # Treatment will be assigned via session config


class Subsession(BaseSubsession):
    treatment = models.IntegerField(
        doc="Treatment group number (1, 2, 3, or 4)"
    )
    
    @classmethod
    def creating_session(cls, subsession):
        """Set treatment group from session config when session is created"""
        # Access session config to get treatment
        try:
            if hasattr(subsession.session, 'config') and 'treatment' in subsession.session.config:
                subsession.treatment = subsession.session.config['treatment']
            else:
                # Default to treatment 1 if not specified
                subsession.treatment = 1
        except:
            # Fallback to default
            subsession.treatment = 1
    
    def set_treatment_from_config(self):
        """Set treatment group from session config (fallback method)"""
        # Access session config to get treatment
        try:
            if hasattr(self.session, 'config') and 'treatment' in self.session.config:
                self.treatment = self.session.config['treatment']
            else:
                # Default to treatment 1 if not specified
                self.treatment = 1
        except:
            # Fallback to default
            self.treatment = 1
    
    def vars_for_admin_report(self):
        contributions = []
        for p in self.get_players():
            try:
                # Safely check if contribution field has a value
                if p.contribution is not None:
                    contributions.append(p.contribution)
            except (AttributeError, ValueError, TypeError):
                # Field is None or not accessible, skip this player
                pass
        
        if contributions:
            return {
                'avg_contribution': sum(contributions)/len(contributions),
                'min_contribution': min(contributions),
                'max_contribution': max(contributions),
                'treatment': self.treatment,
            }
        else:
            return {
                'avg_contribution': '(no data)',
                'min_contribution': '(no data)',
                'max_contribution': '(no data)',
                'treatment': self.treatment,
            }


class Group(BaseGroup):
    total_contribution = models.CurrencyField(
        doc="Total contributions from all group members"
    )

    individual_share = models.CurrencyField(
        doc="Each player's share of the public good earnings"
    )

    def set_payoffs(self):
        # Standard PGG payoff calculation
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        # Total public good value is multiplied, then split equally
        total_public_good = self.total_contribution * Constants.multiplier
        self.individual_share = total_public_good / Constants.players_per_group
        
        # Each player's payoff = (endowment - contribution) + share of public good
        for p in self.get_players():
            p.payoff = (Constants.endowment - p.contribution) + self.individual_share


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, 
        max=Constants.endowment,
        doc="The amount the player contributes to the public good (reporting infrastructure)"
    )
    
    def get_treatment(self):
        """Get the treatment group for this player"""
        return self.subsession.treatment
