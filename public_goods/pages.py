from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class CitizenReportingIntro(Page):
    """Introduction page framing the experiment as citizen reporting"""
    
    def is_displayed(self):
        # Show only in first round
        return self.round_number == 1
    
    def before_next_page(self):
        # Ensure treatment is set from config
        self.subsession.set_treatment_from_config()
    
    def vars_for_template(self):
        # Ensure treatment is set from config (fallback if creating_session didn't run)
        try:
            # Try to access treatment - if it fails, set it
            _ = self.subsession.treatment
        except (AttributeError, ValueError, TypeError):
            # Field doesn't exist or is None, set it
            self.subsession.set_treatment_from_config()
        
        # Set it again to be safe
        self.subsession.set_treatment_from_config()
        
        # Get treatment value - should be set now
        try:
            treatment_value = self.subsession.treatment
        except:
            treatment_value = 1
            
        return {
            'treatment': treatment_value,
        }


class Introduction(Page):
    """Standard PGG instructions"""
    
    def is_displayed(self):
        # Show only in first round
        return self.round_number == 1


class Contribute(Page):
    """Player: Choose how much to contribute to reporting infrastructure"""

    form_model = 'player'
    form_fields = ['contribution']
    
    timeout_submission = {'contribution': c(Constants.endowment / 2)}
    
    def vars_for_template(self):
        return {
            'round_number': self.round_number,
            'total_rounds': Constants.num_rounds,
            'contribution_label': f'Your contribution (from 0 to {Constants.endowment} points):',
            'endowment_value': float(Constants.endowment),  # For JavaScript
        }


class ResultsWaitPage(WaitPage):
    """Wait for all players to contribute before calculating payoffs"""
    
    def after_all_players_arrive(self):
        self.group.set_payoffs()
    
    body_text = "Waiting for other participants to make their decisions."


class Results(Page):
    """Show results for this round"""

    def vars_for_template(self):
        points_kept = Constants.endowment - self.player.contribution
        return {
            'total_earnings': self.group.total_contribution * Constants.multiplier,
            'round_number': self.round_number,
            'total_rounds': Constants.num_rounds,
            'is_final_round': self.round_number == Constants.num_rounds,
            'points_kept': points_kept,
        }


class FinalResults(Page):
    """Show final results after all rounds"""
    
    def is_displayed(self):
        # Show only after the last round
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        # Calculate total payoff across all rounds
        total_payoff = sum([p.payoff for p in self.player.in_all_rounds()])
        return {
            'total_payoff': total_payoff,
            'num_rounds': Constants.num_rounds,
        }


page_sequence = [
    CitizenReportingIntro,
    Introduction,
    Contribute,
    ResultsWaitPage,
    Results,
    FinalResults
]
