# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .competitions import competition_views
from .ranking import rank_views
from .results import result_views
from .notification import notification_views  


views = [user_views, index_views, auth_views, competition_views, rank_views, result_views, notification_views] 
# blueprints must be added to this list